from django.contrib import admin
from . import models

ebook_models = [models.EBook, models.Review]

admin.site.register(ebook_models)
