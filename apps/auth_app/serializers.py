from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name   = serializers.ReadOnlyField()
    est_admin   = serializers.ReadOnlyField()
    peut_ecrire = serializers.ReadOnlyField()

    class Meta:
        model  = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'role', 'telephone', 'full_name', 'est_admin', 'peut_ecrire',
            'is_staff', 'date_joined',
            'locataire_profile', 'proprietaire_profile',
        ]
        read_only_fields = ['date_joined']


class UserCreateSerializer(serializers.ModelSerializer):
    # Pas required en update (laisser vide = inchangé)
    password = serializers.CharField(write_only=True, min_length=6, required=False, allow_blank=True)

    # Optionnel : lier à un profil existant
    locataire_profile_id   = serializers.IntegerField(required=False, allow_null=True, write_only=True)
    proprietaire_profile_id = serializers.IntegerField(required=False, allow_null=True, write_only=True)

    class Meta:
        model  = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'role', 'telephone', 'password',
            'locataire_profile_id', 'proprietaire_profile_id',
        ]

    def validate(self, data):
        # Création : mot de passe obligatoire
        if not self.instance and not data.get('password'):
            raise serializers.ValidationError({'password': 'Le mot de passe est obligatoire pour un nouvel utilisateur.'})
        return data

    def create(self, validated):
        pwd       = validated.pop('password', None)
        loc_id    = validated.pop('locataire_profile_id', None)
        prop_id   = validated.pop('proprietaire_profile_id', None)

        user = User(**validated)
        if pwd:
            user.set_password(pwd)
        else:
            user.set_unusable_password()

        # Lier profil selon le rôle
        if loc_id:
            user.locataire_profile_id = loc_id
        if prop_id:
            user.proprietaire_profile_id = prop_id

        user.save()
        return user

    def update(self, instance, validated):
        pwd     = validated.pop('password', None)
        loc_id  = validated.pop('locataire_profile_id', None)
        prop_id = validated.pop('proprietaire_profile_id', None)

        for attr, val in validated.items():
            setattr(instance, attr, val)

        if pwd:                          # Changer le mot de passe seulement si fourni
            instance.set_password(pwd)
        if loc_id is not None:
            instance.locataire_profile_id = loc_id
        if prop_id is not None:
            instance.proprietaire_profile_id = prop_id

        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        u = authenticate(username=data['username'], password=data['password'])
        if not u:
            raise serializers.ValidationError('Identifiants incorrects.')
        if not u.is_active:
            raise serializers.ValidationError('Compte désactivé.')
        data['user'] = u
        return data
