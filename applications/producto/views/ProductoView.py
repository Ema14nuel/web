from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from ..models import Pro042Producto, Pro045Marca, Pro041Tipo, Pro044Imagen

# Create your views here.
class Inicio(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'base/index.html'

# Create your views here.
class Nosotros(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'base/nosotros.html'

class ProductoListaView(ListView):
    model = Pro042Producto
    template_name = 'producto/index.html'
    context_object_name = 'productos'
    paginate_by = 10  # Número de productos por página

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar por búsqueda (nombre o descripción)
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nombre__icontains=search_query) |
                Q(descripcion__icontains=search_query)
            )

        # Filtrar por marca
        marca_id = self.request.GET.get('marca')
        if marca_id:
            queryset = queryset.filter(marca_045_id=marca_id)

        # Filtrar por tipo
        tipo_id = self.request.GET.get('tipo')
        if tipo_id:
            queryset = queryset.filter(tipo_041_id=tipo_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Pro045Marca.objects.all()
        context['tipos'] = Pro041Tipo.objects.all()
        return context