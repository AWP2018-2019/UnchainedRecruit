from django.urls import path,include
from .views import (
    Index,
    Show,
    Register,
    Login,
    Logout,
    )

urlpatterns = [ 
    path('',Index.as_view(), name='home'),
    path('anunt/<int:id>', Show.as_view(), name='anunt_detail'),
    path('register', Register.as_view(), name='register_path'),
    path('login', Login.as_view(), name='login_path'),
    path('logout', Logout.as_view(), name='logout_path')
]