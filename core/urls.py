from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('user/', views.UserCreation.as_view(), name='user-creation'),
    path('user/login/', views.Login.as_view(), name='user-login'),
    path('user/logout/', views.Logout.as_view(), name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
