from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/',views.welcome_user),
    path('sum/<int:first>/<int:second>/', views.calculate_sum),
    path('diff/<int:first>/<int:second>/', views.calculate_diff)
]