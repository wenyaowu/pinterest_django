from django.contrib import admin

from models import Pin, Category, Board


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class BoardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Pin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Board, BoardAdmin)