from django.contrib import admin
from .models import Post,NewsArticle,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(NewsArticle)
admin.site.register(Comment)

