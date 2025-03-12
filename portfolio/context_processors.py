from django.conf import settings

def portfolio_context(request):
    """Global context for all templates."""
    return {
        'site_name': 'My Portfolio',
        'site_author': 'Your Name',
        'site_description': 'Web Developer & Designer',
    }