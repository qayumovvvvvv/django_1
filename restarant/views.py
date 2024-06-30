from django.shortcuts import render
from . import models

def main(request):
    featured_works = models.Featured_works.objects.all()
    latest_blogs = models.Lates_blog.objects.all().order_by('-id')[:3]
    menu_prices = models.Menu_price.objects.all()
    address = models.Contact_info.objects.last()
    context = {
        'featured_works' : featured_works,
        'latest_blog' : latest_blogs,
        'menu_prices' : menu_prices,
        'address' : address
    }
    return render(request, 'index.html', context)

