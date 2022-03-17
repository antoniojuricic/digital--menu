from django.db import models
from django.template.defaultfilters import slugify

class MealCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(MealCategory, self).save(*args, **kwargs)
    
class Meal(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(MealCategory, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Meal, self).save(*args, **kwargs)

   