from django.contrib import admin

from .models import NewsBlog
from django_summernote.admin import SummernoteModelAdmin


class NewsBlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'created_at', 'updated_at')
    list_filter = ('title', 'created_at', 'updated_at')

admin.site.register(NewsBlog, NewsBlogAdmin)
