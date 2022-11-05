from django.urls import path
# from .views import DetailServerapi, ListServerapi
from .views import home, CalculateView

urlpatterns = [
    # path('<int:pk>/', DetailServerapi.as_view()),
    # path('', ListServerapi.as_view(),)
    path('', home, name='home'),
    path('calculate', CalculateView.as_view(), name='calculate'),
    # path('answer', RetrieveView.as_view(), name='answer'),
]