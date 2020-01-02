from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'user']   # 어떤 부분을 보여줄 것이냐
    list_display_links = ['nickname', 'user']
    search_fields = ['nickname']
