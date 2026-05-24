from django.contrib import admin
from . models import CrewMember , Article , UpcomingProject , RecentWork 
# Register your models here.

admin.site.register(CrewMember)
admin.site.register(Article)
admin.site.register(UpcomingProject)
admin.site.register(RecentWork)