from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.models import SystemUser

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=SystemUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    image = serializers.ImageField() 
    class Meta:
        model = SystemUser
        fields = ('username', 'password', 'email', 'name','image','is_blocked')   
        extra_kwargs = {'name': {'required': True},'is_blocked': {'required': False}}

    def create(self, validated_data):
        user = SystemUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            image=validated_data['image'],
            is_blocked=validated_data['is_blocked']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(label="Password",style={'input_type': 'password'},trim_whitespace=False,write_only=True)
    class Meta:
        model = SystemUser
        fields = ('username', 'password', 'email')

    def validate(self, data):
        username = data.get('username') 
        password = data.get('password')
        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                user = authenticate(request=self.context.get('request'), email=username, password=password)
                if not user:
                    raise serializers.ValidationError('Unable to log in with provided credentials.', code='authentication')
        else:
            raise serializers.ValidationError('Must include "username" and "password".', code='authentication')
        data['user'] = user
        return data