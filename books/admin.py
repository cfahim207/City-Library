from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.BookModel)
admin.site.register(models.Comment)