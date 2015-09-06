from django.db import models

from fractions import Fraction
import math

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
    	return self.name

class Image(models.Model):
	image_key = models.CharField(max_length=1024)
	title = models.CharField(max_length=255)
	def __unicode__(self):
		return self.title

class Difficulty(models.Model):
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class Cuisine(models.Model):
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class Taste(models.Model):
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class QtyType(models.Model):
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    difficulty = models.ForeignKey(Difficulty)
    serves = models.IntegerField(default=1)
    preparation = models.IntegerField(default=0)
    cooking = models.IntegerField(default=0)
    cuisine = models.ForeignKey(Cuisine)
    category = models.ForeignKey(Category)
    ingredients = models.ManyToManyField(Ingredient, through='RecipieIngredients')
    #images = models.ManyToManyField(Image)
    featured_image = models.ForeignKey(Image,blank=False,null=True)
    method = models.TextField()
    source = models.CharField(max_length=255)
    taste = models.ForeignKey(Taste)
    def __unicode__(self):
    	return self.name
    def get_ingredients(self):
    	return self.ingredient_set.all()

class RecipieIngredients(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredient = models.ForeignKey(Ingredient)
	qty_type = models.ForeignKey(QtyType)
	volume = models.FloatField(default=0)
	def __unicode__(self):
		return str(self.volume) + " " + self.qty_type.name + " " + self.ingredient.name
	def get_volume(self):
		wholenum = math.trunc(self.volume)
		fracDec = self.volume - wholenum
		volStr = ""
		if (wholenum > 0):
			volStr += str(wholenum) + " "
		if (fracDec > 0):
			volStr += str(Fraction(fracDec))
		return volStr
	def get_qty(self):
		if (self.qty_type.name == "Each"):
			return self.get_volume()
		else:
			return self.get_volume() + " " + self.qty_type.name
		