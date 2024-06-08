from django.urls import path
from . import views

urlpatterns = [
    path('tipos/', views.TiposListView.as_view(), name='tipos_list'),
    path('tipos/<int:pk>/detail/', views.TiposDetailView.as_view(), name='tipos_detail')
]
