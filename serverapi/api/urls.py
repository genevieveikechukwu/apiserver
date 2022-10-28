from django.urls import path
from .views import DetailServerapi, ListServerapi

urlpatterns = [
    path('<int:pk>/', DetailServerapi.as_view()),
    path('', ListServerapi.as_view(),)
]