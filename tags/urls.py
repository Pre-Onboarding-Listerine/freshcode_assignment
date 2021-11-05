from django.urls import path

from tags import views

urlpatterns = [
    path('', views.tag_not_detail),
    path('/<int:pk>', views.tag_detail),
]
