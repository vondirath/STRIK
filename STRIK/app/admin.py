from django.contrib import admin
from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    fields = ['title', 'post_date', 'image_name', 'sale', 'featured', 'price', 'temporary_price']


# Model Registration
admin.site.register(Posts, PostsAdmin)