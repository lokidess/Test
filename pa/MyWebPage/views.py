from django.views.generic import TemplateView, ListView
from MyWebPage.models import Products, BrandType
from django.shortcuts import get_object_or_404



class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        products = Products.objects.all()[:100]
        context['products'] = products
        return context


class BrandView(ListView):
    template_name = 'brand_type.html'
    model = Products

    def get_queryset(self):
        brand_type = get_object_or_404(BrandType, id=self.kwargs['brand_type_id'])
        queryset = self.model.objects.filter(brand_type=brand_type)
        return queryset
