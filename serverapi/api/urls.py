from django.urls import path
# from .views import DetailServerapi, ListServerapi
from . import views

urlpatterns = [
    # path('<int:pk>/', DetailServerapi.as_view()),
    # path('', ListServerapi.as_view(),)
    path('', views.home, name='home')
]