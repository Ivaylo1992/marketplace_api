from django.contrib import admin
from marketplace_api.api.models import Order, OrderItem, User

class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderItemInline,
    )


admin.site.register(Order, OrderAdmin)

admin.site.register(User)