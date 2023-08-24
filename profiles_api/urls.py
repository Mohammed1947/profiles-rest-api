from django.urls import path

from profiles_api import views


urlpatterns = [
    path('apiview/', views.ApiView.as_view()),
]
