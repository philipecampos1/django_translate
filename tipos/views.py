from django.views.generic import ListView, DetailView
from .models import Tipos


class TiposListView(ListView):
    model = Tipos
    template_name = 'tipos.html'
    context_object_name = 'tipos'

    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.request.GET.get('tipo')

        if tipo:
            queryset = queryset.filter(name__icontains=tipo)

        return queryset


class TiposDetailView(DetailView):
    model = Tipos
    template_name = 'tipos_detail.html'
