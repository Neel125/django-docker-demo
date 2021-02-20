from django.urls import path
from . import views

app_name = "token_auth"
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name="create_user"),
    path('token/', views.CreateTokenView.as_view(), name="token"),
    path('user/', views.RetrieveUpdateUserView.as_view(), name="user"),
]
