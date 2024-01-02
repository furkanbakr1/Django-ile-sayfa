from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def articles(request):
    articles =Article.objects.all()

    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})

    return render(request,"articles.html",{"articles":articles})

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    article = Article.objects.filter(author = request.user)
    context = {
        "articles": article
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        
        messages.success(request,"Makale Başarıyla Oluşturuldu.")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})


def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article, "comments":comments})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi.")
        return redirect("article:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    article.delete()
    messages.success(request,"Makale başarıyla silindi.")
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))



def iletisim(request):
    return render(request,"iletisim.html")

def kisiler(request):
    return render(request,"kisiler.html")


def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        my_model = MyModel(image=image)
        my_model.save()
        return render(request, 'Kisiler.html')
    
    return render(request, 'Kisiler.html')