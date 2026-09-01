from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import User
from rest_framework.views import APIView
from .serializers import UserSerializer, UserCreateSerializer, LoginSerializer
from apps.immeubles.permissions import IsAdminOrGestionnaire
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        old_pwd = request.data.get('old_password', '')
        new_pwd = request.data.get('new_password', '')

        if not request.user.check_password(old_pwd):
            return Response(
                {'old_password': 'Mot de passe actuel incorrect.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if len(new_pwd) < 6:
            return Response(
                {'new_password': 'Minimum 6 caractères.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        request.user.set_password(new_pwd)
        request.user.save()
        return Response({'message': 'Mot de passe mis à jour.'})



@api_view(['GET'])
@permission_classes([AllowAny])
def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})

class ResetUserPasswordView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrGestionnaire]

    def post(self, request, user_id):
        new_pwd = request.data.get('new_password', '')
        reason = request.data.get('reason', '')

        if not new_pwd:
            return Response({'new_password': 'Ce champ est requis.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(new_pwd) < 4:
            return Response({'new_password': 'Minimum 4 caractères.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'Utilisateur introuvable.'}, status=status.HTTP_404_NOT_FOUND)

        user.set_password(new_pwd)
        user.save()

    
        if user.locataire_profile:
            user.locataire_profile.mot_de_passe_temp = new_pwd
            user.locataire_profile.save(update_fields=['mot_de_passe_temp'])
        elif user.proprietaire_profile:
            user.proprietaire_profile.mot_de_passe_temp = new_pwd
            user.proprietaire_profile.save(update_fields=['mot_de_passe_temp'])

        return Response({'message': f'Mot de passe réinitialisé pour {user.username}.', 'reason': reason})

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    s = LoginSerializer(data=request.data)
    if not s.is_valid():
        return Response(s.errors, status=400)
    user = s.validated_data['user']
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token':           token.key,
        'user_id':         user.pk,
        'username':        user.username,
        'fullname':        user.full_name,
        'role':            user.role,
        'peutEcrire':      user.peut_ecrire,
        'estAdmin':        user.est_admin,
        'locataire_id':    user.locataire_profile_id,
        'proprietaire_id': user.proprietaire_profile_id,
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        request.user.auth_token.delete()
    except Exception:
        pass
    return Response({'detail': 'Déconnecté.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    return Response(UserSerializer(request.user).data)


class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserCreateSerializer if self.request.method == 'POST' else UserSerializer

    def get_queryset(self):
        qs = User.objects.all().order_by('-date_joined')
        role = self.request.query_params.get('role') 
        if role:
            qs = qs.filter(role=role)                 
        return qs

    def create(self, request, *args, **kwargs):
        s = UserCreateSerializer(data=request.data)
        if not s.is_valid():
            return Response(s.errors, status=400)
        user = s.save()
        return Response(UserSerializer(user).data, status=201)


# ── DÉTAIL / MODIFICATION / SUPPRESSION ──────────────────────
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserCreateSerializer if self.request.method in ('PUT', 'PATCH') else UserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        s = UserCreateSerializer(instance, data=request.data, partial=partial)
        if not s.is_valid():
            return Response(s.errors, status=400)
        user = s.save()
        return Response(UserSerializer(user).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lier_locataire(request, user_id):
    from apps.locataires.models import Locataire
    try:
        user = User.objects.get(pk=user_id)
        loca = Locataire.objects.get(pk=request.data.get('locataire_id'))
        user.locataire_profile = loca
        user.role = 'locataire'
        user.save()
        return Response({'ok': True, 'message': f'{user.username} lié à {loca.nom_prenom}'})
    except Exception as e:
        return Response({'error': str(e)}, status=400)
 
 
from .serializers import RegisterSerializer  # à côté des autres imports de serializers

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    s = RegisterSerializer(data=request.data)
    if not s.is_valid():
        return Response(s.errors, status=400)
    user = s.save()
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token':      token.key,
        'user_id':    user.pk,
        'username':   user.username,
        'fullname':   user.full_name,
        'role':       user.role,
        'peutEcrire': user.peut_ecrire,
        'estAdmin':   user.est_admin,
    }, status=201)
 
 
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lier_proprietaire(request, user_id):
    from apps.proprietaires.models import Proprietaire
    try:
        user = User.objects.get(pk=user_id)
        prop = Proprietaire.objects.get(pk=request.data.get('proprietaire_id'))
        user.proprietaire_profile = prop
        user.role = 'proprietaire'
        user.save()
        return Response({'ok': True, 'message': f'{user.username} lié à {prop.nom}'})
    except Exception as e:
        return Response({'error': str(e)}, status=400)