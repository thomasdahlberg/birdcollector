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
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('birds/<int:bird_id>/add_photo/', views.add_photo, name='add_photo'),
    path('birds/<int:bird_id>/assoc_gift/<int:gift_id>/', views.assoc_gift, name='assoc_gift'),
    path('birds/<int:bird_id>/rm_gift/<int:gift_id>/', views.rm_gift, name='rm_gift'),
    path('gifts/', views.GiftList.as_view(), name='gifts_index'),
    path('gifts/<int:pk>/', views.GiftDetail.as_view(), name='gifts_detail'),
    path('gifts/<int:pk>/update/', views.GiftUpdate.as_view(), name='gifts_update'),
    path('gifts/<int:pk>/delete/', views.GiftDelete.as_view(), name='gifts_delete'),
    path('gifts/create/', views.GiftCreate.as_view(), name='gifts_create'),
    path('accounts/signup/', views.signup, name='signup'),
]