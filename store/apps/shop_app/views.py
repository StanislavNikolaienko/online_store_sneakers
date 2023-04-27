import logging

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Product

logger = logging.getLogger('django')


class Index(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'items'
    paginate_by = 20


def item_detail(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    logger.info(f'Item {item} was opened')
    return render(request, 'item_detail.html', {'item': item})
