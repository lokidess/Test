from django.views.generic import TemplateView
from MyWebPage.models import Products



class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        products = Products.objects.all()[:100]
        context['products'] = products
        return context


#class MarkView(ListView):
#    template_name = 'trade_mark.html'
#    model = Products
#
#    def get_queryset(self):
#        # trade_mark = TradeMark.objects.get(id=self.kwargs['trade_mark_id'])
#        trade_mark = get_object_or_404(Mark, id=self.kwargs['trade_mark_id'])
#        queryset = self.model.objects.filter(trade_mark=trade_mark)
        # queryset = self.model.objects.filter(
        #     trade_mark__id=self.kwargs['trade_mark_id'],
        #     count__gt=0
        # )
#        return queryset