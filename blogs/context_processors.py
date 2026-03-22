from .models import Category, Logo
from abouts.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_logo(request):
    latest_logo = Logo.objects.order_by('-uploaded_at').first()
    return dict(latest_logo = latest_logo)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links = social_links)