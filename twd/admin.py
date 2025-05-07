from django.contrib import admin
from .models import Usersign_up, Vendorregister, Packagecreate, Bookingdetails

# Register Usersign_up, Vendorregister, Bookingdetails normally
admin.site.register(Usersign_up)
admin.site.register(Vendorregister)
admin.site.register(Bookingdetails)

# Register Packagecreate using decorator
@admin.register(Packagecreate)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor', 'date', 'price', 'aprovel')
    list_filter = ('aprovel',)
    search_fields = ('title', 'businessname')
