from django.shortcuts import render
from shop.models import Product
from django.db.models import Q, query
import logging

logger = logging.getLogger('search_app')
logger.setLevel(logging.DEBUG)


# Create your views here.
def searchResult(request) :
    
    logger.debug('logger = {}'.format(logger))
    logger.debug('__name__ = {}'.format(__name__))
    products = None
    query = None
    if 'q' in request.GET :
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    
    logger.debug('GET access id = {} product_detail'.format(products))
    
    return render(request, 'search_app/search.html', {'query':query, 'products':products})