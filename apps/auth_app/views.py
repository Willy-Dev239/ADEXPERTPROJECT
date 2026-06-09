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



# Import depuis immeubles/permissions.py
from apps.immeubles.permissions import IsAdminOrGestionnaire

# views.py
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
class ResetUserPasswordView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrGestionnaire]

# ── CSRF (Feature 9) ─────────────────────────────────────────
@api_view(['GET'])
@permission_classes([AllowAny])
def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})

class ResetUserPasswordView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrGestionnaire]
# ── LOGIN ─────────────────────────────────────────────────────
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


# ── LOGOUT ────────────────────────────────────────────────────
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        request.user.auth_token.delete()
    except Exception:
        pass
    return Response({'detail': 'Déconnecté.'})


# ── ME ────────────────────────────────────────────────────────
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    return Response(UserSerializer(request.user).data)

# ── LISTE / CRÉATION utilisateurs ────────────────────────────
class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserCreateSerializer if self.request.method == 'POST' else UserSerializer

    def get_queryset(self):
        qs = User.objects.all().order_by('-date_joined')
        role = self.request.query_params.get('role')  # ✅ AJOUTER
        if role:
            qs = qs.filter(role=role)                 # ✅ AJOUTER
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