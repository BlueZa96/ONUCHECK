from django.urls import path
from .views import index, get_onu_data_and_stat

urlpatterns = [
    path('', index, name="index"),
    path('getOnuFullData', get_onu_data_and_stat, name="get_onu_data_and_stat"),
]