from django.urls import path,include
from .views import (
    Index,
<<<<<<< Updated upstream
    Show,
    Register,
    Login,
    Logout,
    )
=======
    AnuntView,
    AnuntCreateView,
    AnuntDeleteView,
    AnuntEditView
)
>>>>>>> Stashed changes

urlpatterns = [ 
    path('',Index.as_view(), name='home'),
    path(r'^anunt/<int:pk>/detail', AnuntView.as_view(), name='anunt'),
    path(r'^anunt/<int:pk>/delete', AnuntDeleteView.as_view(), name='anunt_delete'),
    path(r'^anunt/<int:pk>/edit', AnuntEditView.as_view(), name='anunt_edit'),
   # path(r'^anunt/<int:pk>/aplica', AplicaAnunt.as_view(), name='aplica_anunt'),
<<<<<<< Updated upstream
    path(r'^anunt/create', AnuntCreateView.as_view(), name='anunt_create'),
    path('anunt/<int:id>', Show.as_view(), name='anunt_detail'),
    path('register', Register.as_view(), name='register_path'),
    path('login', Login.as_view(), name='login_path'),
    path('logout', Logout.as_view(), name='logout_path')
=======
    path(r'^anunt/create', AnuntCreateView.as_view(), name='anunt_create')
>>>>>>> Stashed changes
]