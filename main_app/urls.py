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

    # path for adding photo
    path('beers/<int: beer_id>/add_photo', views.add_photo, name='add_photo'),

    path('awards/', views.AwardList.as_view(), name='awards_index'),
    path('awards/<int:pk>/', views.AwardDetail.as_view(), name='awards_detail'),
    path('awards/create/', views.AwardCreate.as_view(), name='awards_create'),
    path('awards/<int:pk>/update', views.AwardUpdate.as_view(), name='awards_update'),
    path('awards/<int:pk>/delete', views.AwardDelete.as_view(), name='awards_delete'),

    # Associate the award with the beer 
    path('beers/<int:beer_id>/assoc_award/<int:award_id>/', views.assoc_award, name='assoc_award'),
    path('beers/<int:beer_id>/unassoc_award/<int:award_id>/', views.unassoc_award, name='unassoc_award')
]