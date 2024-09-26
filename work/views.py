from django.shortcuts import render,redirect
from work.models import Work,Category
from teacher.models import Teacher
from django.core.paginator import Paginator
from contact.models import Contact
from contact.forms import ContactForm
from article.models import Article

def home_page(request):
    teacher = Teacher.objects.all()[:6]
    paginator = Paginator(Work.objects.all(), per_page=4)
    articles = Article.objects.all()

    page = request.GET.get("page")
    page = int(page)

    if not page or not isinstance(page, int):
        page = 1

    all_pages = paginator.num_pages
    if page > all_pages or page < 0 :
        return redirect("not_found")
    

    works = paginator.get_page(page)

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "works": works,
        "page": page,
        "teacher": teacher,
        "articles": articles,
        "form" : form ,
    }

    return render(request, template_name='index.html',context=context)


def not_found(request):
    return render(request, template_name='404_not_found')