from django.contrib import admin
from .models import Meal, MealCategory

class MealAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'category', 'price', 'available')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25

class MealCategoryAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25

admin.site.register(Meal, MealAdmin)
admin.site.register(MealCategory, MealCategoryAdmin)