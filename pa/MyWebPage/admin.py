from django.contrib import admin
from MyWebPage.models import Mark, Products


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'get_total')
    search_fields = ('name', 'trade_mark__name')

    def get_total(self, obj):
        return obj.price * obj.count
    get_total.short_description = 'Total'


admin.site.register(Mark)
admin.site.register(Products, ProductAdmin)