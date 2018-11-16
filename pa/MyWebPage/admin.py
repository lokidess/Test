from django.contrib import admin
from MyWebPage.models import Products, BrandType


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'brand_type')
    search_fields = ('name', 'brand_type__name')

#    def get_total(self, obj):
#        return obj.price * obj.count
#    get_total.short_description = 'Total'


#admin.site.register(Mark)
admin.site.register(Products, ProductAdmin)
admin.site.register(BrandType)
