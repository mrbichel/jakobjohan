from django.contrib import admin
from images.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display  = ('title', 'file', 'upload_date', 'mod_date')
    list_filter   = ('upload_date', 'mod_date')
    search_fields = ('title', 'file', 'description')

admin.site.register(Image, ImageAdmin)