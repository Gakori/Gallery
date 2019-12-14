from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image


def welcome(request):
    images = Image.all_images()
    return render(request,'index.html',{'images':images})

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_category = Category.search_by_title(search_term)
        message = f'{search_term}'
        
        return render(request,'search.html',{'message':message,'categories': searched_categories})
    else:
        message = 'You havent searched for any term'
        return render(request,'search.html',{'message':message})
    
def image(request,image_id):
    try:
        image=Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'index.html',{'image':image})

def category(request,category_id):
    try:
        category=Category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'search.html',{'category':category})
    

    