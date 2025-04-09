from django.contrib import admin
from .models import Project, Skill, Education, Experience, Contact, SiteConfiguration, UserProfile

# Singleton Admins
class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(SingletonAdmin):
    pass

# Custom Admins
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    search_fields = ('degree', 'institution')

# Default Admins
admin.site.register(Project)
admin.site.register(Contact)
