from django.urls import path
from . import views

urlpatterns = [
    # Gateway (Directs unauthenticated to login, authenticated to home)
    path('', views.root_gateway_view, name='root'),
    
    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Main Application
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),

    # Gamification Tracks & Levels
    path('course/<slug:slug>/', views.course_quest_map_view, name='course_quest_map'),
    path('course/<slug:slug>/level/<int:level_number>/', views.level_module_detail_view, name='level_detail'),

    # APIs
    path('api/complete-level/<slug:slug>/<int:level_number>/', views.complete_level_api, name='complete_level_api'),
    path('api/ai-tutor/', views.ai_tutor_api, name='ai_tutor_api'),
]
