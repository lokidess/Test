from MyWebPage.models import Mark


def trade_marks(request):
    return {'trade_marks': Mark.objects.all()}
