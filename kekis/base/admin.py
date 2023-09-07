from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
admin.site.register(Contacts)
admin.site.register(Image)
admin.site.register(Project)
admin.site.register(Account)
admin.site.register(Shop)
admin.site.register(Buy)
admin.site.register(Timetable)
admin.site.register(Group)
admin.site.register(Competitions)