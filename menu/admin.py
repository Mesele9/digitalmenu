""" 
from django.contrib import admin
from .models import Category, MenuItem

admin.site.register(Category)
admin.site.register(MenuItem)
 """

from django.contrib import admin
from .models import MainCategory, Category, MenuItem, Rating

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']
    filter_horizontal = ['categories']  # Allow selecting multiple categories

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'stars', 'guest_name', 'created_at']

admin.site.register(Category)