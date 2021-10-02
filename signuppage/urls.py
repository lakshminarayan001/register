from django.contrib import admin
from django.urls import path, include
from signuppage.views import signupapi
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('', signupapi.as_view()),
    path('<int:pk>/', signupapi.as_view()),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
