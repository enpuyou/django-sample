from django.contrib import admin
from .models import Post

""" Use to display models in django admin panel also
you can customise admin panel using this file """
admin.site.register(Post)
