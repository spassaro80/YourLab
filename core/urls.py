from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('update/<id>', views.update_match, name="update_match"),
    path('display/', views.display, name="display"),
    path('display/<id>/', views.display_match, name="display_match"),
    path('creatematch/', views.create_match, name="create_match"),
    path('newevent/<id>', views.new_event, name="new_event"),
    path('stats/<id>', views.stats, name="stats"),
]