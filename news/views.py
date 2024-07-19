from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsArticle, Comment, Tag
from .forms import CommentForm

def news(request):
    articles = NewsArticle.objects.all().order_by('published_date')
    context = {
        'articles': articles
    }
    return render(request, 'news/news.html', context)



def news_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    comments = Comment.objects.filter(article=article, is_active=True)
    recent_posts = NewsArticle.objects.exclude(pk=pk).order_by('-published_date')[:5]


    # Handle comment form submission
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            # Optionally, you might redirect or reload the page here after saving the comment
    else:
        comment_form = CommentForm()

    context = {
        'article': article,
        'comments': comments,
        'recent_posts': recent_posts,
        'comment_form': comment_form,  # Pass the comment form to the template
    }
    return render(request, 'news/news_detail.html', context)

def submit_comment(request, article):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect('news_detail.html', pk=article.pk)  # Redirect back to the article detail page after comment submission
    else:
        comment_form = CommentForm()
    return comment_form
