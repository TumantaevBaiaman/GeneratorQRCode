from django.db import models
from apps.product import models as models_product


class ModelInstruction(models.Model):
    product_instruction = models.ForeignKey(models_product.ModelProducts, verbose_name="product_instruction", on_delete=models.SET_NULL, null=True, blank=True)
    name_instruction = models.CharField(max_length=255, verbose_name="name_instruction")
    text_instruction = models.TextField(verbose_name="text_instruction")
    image_instruction = models.ImageField(null=True, blank=True, upload_to='instruction_image')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name_instruction
