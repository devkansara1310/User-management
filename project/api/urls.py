from django.urls import path
# from api.views import UserRegistrstion, login_user
from api.views import UserRegistrstion, UserProfiles, UpdateUserProfile, LoginUser, Logout
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', UserRegistrstion.as_view(), name='auth_register'),
    path('login/', LoginUser.as_view(), name='login'),  
    path('logout/', Logout.as_view(), name='logout'),  
    path('users/', UserProfiles.as_view(), name='users_listing'),
    path('users/<int:pk>/', UpdateUserProfile.as_view(), name='update_profile'),
]