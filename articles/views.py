from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'articles/index.html',context)


def detail(request,id):
    article = Article.objects.get(id=id)
    context = {'article':article}
    return render(request,'articles/detail.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.id)
    else:
        form = ArticleForm()  # 빈 폼을 만들어서
    context = {'form':form}
    return render(request,'articles/create.html',context)

def update(request,id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.id)
    else:
        form = ArticleForm(instance=article)  # 빈 폼을 만들어서
    context = {'form':form,'article':article,}
    return render(request,'articles/update.html',context)


def delete(request,id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')