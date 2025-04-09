from django.conf import settings
from .models import SiteConfiguration, UserProfile

def portfolio_context(request):
    return {
        'site_config': SiteConfiguration.objects.first(),
        'user_profile': UserProfile.objects.first()
    }