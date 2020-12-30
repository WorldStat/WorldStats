from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Article
from .forms import ArticleForm
from comments.models import Comment
from time import strftime



def index(request):
    data = dict()
    all_articles = Article.objects.all()
    data['all_articles'] = all_articles
    paginator = Paginator(all_articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'stats/index.html', context=data)

def create(request):
    data = dict()
    if request.method == 'GET':
        # Create empty example of form for filling out
        article_form = ArticleForm()
        data['form'] = article_form
        return render(request, 'stats/create.html', context=data)
    elif request.method == 'POST':
        # Recieve example of already filled form
        article_form = ArticleForm(request.POST, request.FILES)
        article_form.save()
        return redirect('stats/index')

def delete(request):
    return render(request, 'stats/delete.html')

def details(request, article_id: int):
    data = dict()
    data['article'] = Article.objects.get(id=article_id)
    data['comments'] = Comment.objects.all()
    return render(request, 'stats/details.html', context=data)

def details2(request, article_id: int):
    data = dict()
    if request.method == 'GET':
        data['article'] = Article.objects.get(id=article_id)
        data['comments'] = Comment.objects.all()
        return render(request, 'stats/details2.html', context=data)
    elif request.method == 'POST':
        _content = request.POST.get('content')
        _publish = strftime('%Y-%m-%d %H:%M:%S')
        _comment = Comment.objects.create(
            content=_content, publish=_publish, article_id=article_id,
            user_id=request.user.id
        )
        return redirect(f'/stats/details/{article_id}')

def edit(request):
    return render(request, 'stats/edit.html')