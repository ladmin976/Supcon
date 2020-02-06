from django.contrib import admin
from.models import kit_interfaceInLine
from .forms import GoodForm
# Register your models here.
from catalog.models import good, unit, contact, comp_type, country, company, interface, category, subcategory1, subcategory2, subcategory3, control_interface, family, subfamily, cables
class catalogAdmin (admin.ModelAdmin):
    #form = GoodForm
    list_display = ('no', 'name', 'description', 'part_no')
    list_display_links =('name', 'description')
    search_fields = ('name', 'part_no')
    inlines = (kit_interfaceInLine,)
admin.site.register(good, catalogAdmin)
class categoryAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(category, categoryAdmin)
class subcategory1Admin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(subcategory1, subcategory1Admin)
class subcategory2Admin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(subcategory2, subcategory2Admin)
class subcategory3Admin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(subcategory3, subcategory3Admin)
class unitAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(unit, unitAdmin)
class contactAdmin (admin.ModelAdmin):
    list_display = ('no', 'family_name', 'first_name', 'description')
    list_display_links =('family_name', 'first_name')
    search_fields = ('family_name', 'description')
admin.site.register(contact, contactAdmin)
class countryAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(country, countryAdmin)
class companyAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(company, companyAdmin)
class comp_typeAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(comp_type, comp_typeAdmin)
class familyAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(family, familyAdmin)
class subfamilyAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(subfamily, subfamilyAdmin)
class cablesAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(cables, cablesAdmin)
class interfaceAdmin (admin.ModelAdmin):
    inlines = (kit_interfaceInLine,)
    list_display = ('no', 'name', 'description')
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(interface, interfaceAdmin)
class control_interfaceAdmin (admin.ModelAdmin):
    list_display = ('no', 'name', 'description', )
    list_display_links =('name', 'description')
    search_fields = ('name', 'description')
admin.site.register(control_interface, control_interfaceAdmin)
