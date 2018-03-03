from django.contrib import admin
from .models import Post

# Register your models here ---- register will make the models visible on the admin page
admin.site.register(Post)