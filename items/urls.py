from django.urls import path

from items import views


urlpatterns = [
    path('', views.item_not_detail),
    path('/<int:pk>', views.item_detail),
]
