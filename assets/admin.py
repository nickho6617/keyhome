from django.contrib import admin

from .models import OwnedProperty, AddressModel, Structure, Locks


class StructureInline(admin.TabularInline):
    model = Structure


class LocksInline(admin.TabularInline):
    model = Locks


class StructureAdmin(admin.ModelAdmin):
    inlines = [LocksInline]


class OwnedPropertyAdmin(admin.ModelAdmin):
    inlines = [StructureInline]


admin.site.register(OwnedProperty, OwnedPropertyAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(Locks)
admin.site.register(AddressModel)
