from django.urls import path
from . import views

urlpatterns = [
    path('translate/<int:tipo_id>', views.TraducoesListView.as_view(), name='translate_types_list'),
    path('translate/<str:tipo>/<int:pk>', views.tranducoesDetailView.as_view(), name='translate_detail')
]
