import logging
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Product

logger = logging.getLogger('django')

menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "About", 'url_name': 'about'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Sneakers", 'url_name': 'sneakers'},
        {'title': "Sneakers Preview", 'url_name': 'sneakers_preview'}
        ]


def all_items(request):
    items_list = Product.objects.all()
    paginator = Paginator(items_list, 10) # Show 10 items per page
    page = request.GET.get('page')
    items = paginator.get_page(page)
    logger.info(f'All items were opened')
    return render(request, 'all_items.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    logger.info(f'Item {item} was opened')
    return render(request, 'item_detail.html', {'item': item})

def index(request):
    pass


def about(request):
    pass


def contact(request):
    pass
