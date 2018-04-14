from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article


def article_list(request):
    # articles = Article.objects.all()
    articles = Article.objects.filter(is_deleted=False)
    return render_to_response('articles.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('article_detail.html', {'article': article})

def article_detail2(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        # return render(request, 'article_detail.html', {'article': article})
        return render_to_response('article_detail.html', {'article': article})
    except Article.DoesNotExist:
        raise Http404('此页面不存在或已丢失.')
    # return HttpResponse('Title: {0}'.format(article.title))
