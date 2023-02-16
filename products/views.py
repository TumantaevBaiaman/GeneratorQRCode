from django.shortcuts import render
from django.views import View
from . import models


class Home(View):
    template_name = "products/index.html"

    def get(self, request, *args, **kwargs):
        category = models.Category.objects.all()
        print(category[0].logo)
        return render(request, self.template_name, context={"category": category})
