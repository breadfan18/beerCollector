from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beers/', views.beers_index, name='index'),
    path('beers/<int:beer_id>/', views.beers_detail, name='detail'),
    path('beers/create', views.BeerCreate.as_view(), name='beers_create'),
    path('beers/<int:pk>/update/', views.BeerUpdate.as_view(), name='beers_update'),
    path('beers/<int:pk>/delete/', views.BeerDelete.as_view(), name='beers_delete'),
    path('beers/<int:beer_id>/add_drinking', views.add_drinking, name='add_drinking'),

    path('awards/', views.AwardList.as_view(), name='awards_index'),
    path('awards/<int:pk>/', views.AwardDetail.as_view(), name='awards_detail'),
    path('awards/create/', views.AwardCreate.as_view(), name='awards_create'),
]