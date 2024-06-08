from django.views.generic import ListView, DetailView
from traducoes.models import Traducoes
from tipos.models import Tipos


class TraducoesListView(ListView):
    model = Traducoes
    template_name = 'translate_list.html'
    context_object_name = 'translates'

    def get_queryset(self):
        tipo_id = self.kwargs.get('tipo_id')
        return Traducoes.objects.filter(tipo_id=tipo_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = Tipos.objects.get(pk=self.kwargs['tipo_id'])
        return context


class tranducoesDetailView(DetailView):
    model = Traducoes
    template_name = 'translate_detail.html'
    context_object_name = 'translate'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo_str = self.kwargs.get('tipo')
        context['tipo'] = Tipos.objects.get(tipo=tipo_str)
        return context
