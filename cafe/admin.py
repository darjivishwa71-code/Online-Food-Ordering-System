from django.contrib import admin
from cafe.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(menu_item)
admin.site.register(rating)
admin.site.register(order)
admin.site.register(bill)
# admin.site.register(Payment)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "get_order_id", "amount", "status")

    def get_order_id(self, obj):
        return obj.order.order_id