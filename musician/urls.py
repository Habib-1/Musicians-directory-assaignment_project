from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register_user/',views.register_user.as_view(),name='register'),
    path('login/',views.login_user.as_view(),name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_musician/',views.add_musician.as_view(),name='add_musician'),
    path('add_album/',views.add_album.as_view(),name='add_album'),
    path('edit/<int:pk>/',views.edit_album.as_view(),name='edit'),
    path('delete/<int:pk>/',views.delete_album.as_view(),name='delete_album'),
]