from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import forms

# Create your views here.

def index(request):
    category = models.Category.objects.all()
    post = models.Post.objects.all()
    paginator = Paginator(post, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(2)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
            'categoris': category,
            'ojbect': post,
            'queryset': paginated_queryset,
            'page_request_var': page_request_var

    }

    return render(request,'index.html',context)


def blog(request,blogger):
    obj = get_object_or_404(models.Post,id=blogger)
    form = forms.CommentForms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = obj
            form.save()
        return redirect('blog',blogger=blogger)

    context = {
        'blogger':obj,
        'forms':form
    }
    return render(request,'blog.html',context)


def category (request,detail):
    category = models.Category.objects.all()
    obj = models.Post.objects.filter(categories__title__contains=detail)
    context ={
        'obj' : obj,
        'cats' : detail,
        'categoris': category,
    }
    return render(request,'categories.html',context)

