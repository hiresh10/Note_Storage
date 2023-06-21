from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views


# Create a router and register your viewsets
router = DefaultRouter()
router.register('notes', views.NoteViewSet, basename='note')

# Include the generated URLs in your project's urlpatterns
urlpatterns = [
    path('note_api/', include(router.urls)),
    path('index/',views.Index,name='index'),
    path('signuppage/',views.SignupPage,name='signppage'),
    path('register/',views.Register,name='register'),
    path('loginpage/',views.LoginPage,name='loginpage'),
    path('accounts/login/', views.Loginuser, name='login'),
    path('home/',views.Home,name='home'),
    path('profile/',views.Profile,name="profile"),
    path('postpage/',views.Post_notepage, name="postpage"),
    path('post/',views.Post_note,name="add_note"),
    path('notes/',views.Notes,name="notes"),
    path('get_users/', views.get_users, name='get_users'),
    path('logout/', views.logout_view, name='logout'),

#######################################################   ADMIN   #############################################

    path('adminloginpage/',views.AdminLoginPage,name="adminloginpage"),
    path('adminlogin/',views.Aminlogin,name="adminlogin"),
    path('userlist/',views.Userlist,name='userlist'),
    path('userlist/delete/<int:pk>/', views.UserDelete, name='user_delete'),
    path('notelist/',views.NoteList,name='notelist'),
    path('notedelete/delete/<int:pk>',views.NoteDelete,name="notedelete"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
]
