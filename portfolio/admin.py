from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Project, Skill, Education, Experience, Contact

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact)