#from MyWebPage.models import Mark
from MyWebPage.models import BrandType


#def trade_marks(request):
#    return {'trade_marks': Mark.objects.all()}



def brand_types(request):
    return {'brand_types': BrandType.objects.all()}