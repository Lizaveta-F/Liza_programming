from django.contrib import admin
from . models import Order, Product

# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.index_title = "Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(caregory = "default")
    
    change_category_to_default.short_description = 'Defaul category'
    list_display = ('title', 'price', 'discount_price', 'caregory', 'description',)
    search_fields = ('title','caregory','description',)
    actions = ('change_category_to_default',)
    list_editable = ('price','caregory',)
    
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)