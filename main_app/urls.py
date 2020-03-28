from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>/', views.bird_detail, name='detail'),
    path('birds/create/', views.BirdCreate.as_view(), name='bird_create'),
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird_update'),
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='bird_delete'),
]