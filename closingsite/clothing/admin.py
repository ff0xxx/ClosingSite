from django.contrib import admin
from .models import ClothingModel, Rubric


class ClothingAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'price', 'rubric')
    list_display_links = ('title', 'desc', 'price', 'rubric')
    search_fields = ('title', 'rubric')


class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(ClothingModel, ClothingAdmin)
admin.site.register(Rubric, RubricAdmin)
