from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Comment
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.utils import timezone
from django.forms.models import model_to_dict
import logging

logger = logging.getLogger('shop')
logger.setLevel(logging.DEBUG)

# Create your views here.
def allProdCat(request, c_slug = None) :
    c_page = None;
    products_list = None;
    logger.debug('GET access id = {} product_detail'.format(c_slug))
    logger.debug('logger = {}'.format(logger))
    logger.debug('__name__ = {}'.format(__name__))
    
    if c_slug != None :
        c_page = get_object_or_404(Category, slug = c_slug)
        products_list = Product.objects.filter(category = c_page)
    else :
        products_list = Product.objects.all()
    
    paginator = Paginator(products_list, 6)
    try :
        page = int(request.GET.get('page', 1))
    except :
        page = 1

    try :
        products = paginator.page(page)
    except(EmptyPage, InvalidPage) :
        produxts = paginator.page(paginator.num_pages)
    
    return render(request, 'shop/category.html', {'category' : c_page, 'products' : products})

def ProdCatDetail(request, c_slug, product_slug) :
    logger.debug('GET access id = {} product_detail'.format(product_slug))
    logger.debug('logger = {}'.format(logger))
    logger.debug('__name__ = {}'.format(__name__))
    # print('logger = ', logger)
    # print('__name__ = ', __name__)
    try :
        product = Product.objects.get(category__slug = c_slug, slug = product_slug)
        product_key = model_to_dict(product)['id']
        comments = Comment.objects.filter(post = product_key)
        if request.method == "POST":
            comment = Comment()
            comment.post = product
            comment.body = request.POST['body']
            comment.date = timezone.now()
            comment.save()
            print( "출력!", comment.post, comment.body, comment.date )
    except Exception as e :
        raise e
    
    return render(request, 'shop/product.html', {'product' : product, 'comments':comments})

# def detail(request,post_id):
    # post_detail = get_object_or_404(Product,pk=post_id)
    # comments = Comment.objects.filter(post = post_id)
    # if request.method == "POST":
        # comment = Comment()
        # comment.post = post_detail
        # comment.body = request.POST['body']
        # comment.date = timezone.now()
        # comment.save()
        # print( "출력!", comment.post, comment.body, comment.date )
    # return render(request,'shop/product.html',{'post':post_detail, 'comments':comments})