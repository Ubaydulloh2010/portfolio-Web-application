from django.shortcuts import render, get_object_or_404
from article.models import Article
from .forms import CommentForm

def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm()
    
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = article
            obj.save()

    context = {
        "article": article,
        "form": form,
    }

    return render(request, "blog-single.html", context)