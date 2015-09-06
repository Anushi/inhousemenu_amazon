from django.contrib import admin

# Register your models here.

from .models import Category
from .models import Cuisine
from .models import Difficulty
from .models import Image
from .models import Ingredient
from .models import Taste
from .models import Recipe
from .models import QtyType
from .models import RecipieIngredients

class RecipieIngredientsInline(admin.TabularInline):
    model = RecipieIngredients

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipieIngredientsInline]

admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Difficulty)
admin.site.register(Image)
admin.site.register(Ingredient)
admin.site.register(Taste)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(QtyType)
admin.site.register(RecipieIngredients)