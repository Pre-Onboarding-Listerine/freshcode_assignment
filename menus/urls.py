from django.urls import path

from menus import views


urlpatterns = [
    path('', views.menu_not_detail),
    path('/<int:id>', views.menu_detail),
]
