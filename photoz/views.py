from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Category,Location

def welcome(request):
    images = Image.all_images()
    return render(request,'index.html',{'images':images})

def search_results(request):
    if 'photos' in request.GET and request.GET['photos']:
        category = request.GET.get('photos')
        searched_category = Image.search_by_category(category)
        message = f'{category}'
        
        return render(request,'search.html',{'message':message,'categories': searched_category})
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
        category= Category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404() 
    return render(request,'category.html', {'category:category'})


    

    