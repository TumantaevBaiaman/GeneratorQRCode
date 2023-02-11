from django.db import models
from apps.category import models as models_category


class ModelProducts(models.Model):
    category_product = models.ForeignKey(models_category.ModelCategory, verbose_name="category_product", on_delete=models.SET_NULL, null=True, blank=True)
    name_product = models.CharField(max_length=100, null=False, blank=False, verbose_name="name_product")
    description_product = models.TextField(verbose_name="description_product")
    image = models.ImageField(blank=True, null=True, upload_to='product_image')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name_product

