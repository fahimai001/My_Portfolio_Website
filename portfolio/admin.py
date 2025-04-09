from django.contrib import admin
from .models import Project, Skill, Education, Experience, Contact, SiteConfiguration, UserProfile

class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(SingletonAdmin):
    pass

# Keep existing registrations
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact)