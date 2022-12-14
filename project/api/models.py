from django.db import models
from django.contrib.auth.models import  AbstractUser


class SystemUser(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    image = models.ImageField(upload_to ='media/profile', blank=True, null=True)
    is_blocked = models.BooleanField(default=False)
    # USERNAME_FIELD = 'email'


from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

user_model = get_user_model()

class AuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None,**kwargs):
        if username is None:
            username = kwargs.get('email')
        users = user_model._default_manager.filter(
            Q(username__iexact=username) | Q(email__iexact=username))
        for user in users:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        if not users:
            user_model().set_password(password)