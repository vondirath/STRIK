from django.contrib import admin
from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    fields = ['title', 'product_id', 'post_date', 'image_name',
              'sale', 'featured', 'price', 'temporary_price',
              'inventory', 'description']
    list_display = ('title', 'price', 'sale', 'temporary_price',
                    'inventory', 'featured', 'product_id')


# Model Registration
admin.site.register(Posts, PostsAdmin)
