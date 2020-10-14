from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import BlogPost


def index(request):
    return render(request, 'blog/index.html')

def aboutUs(request):
    return render(request, 'blog/about_us.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)


@login_required
def profile(request):
    return render(request, 'blog/profile.html')

@login_required
def dashboard(request):
    return render(request, 'blog/dashboard_block.html')


@login_required
def createBlog(request):

    # if the mentod is post
    if request.method == 'POST':
        blogTitle = request.POST['blog_title']
        blogContent = request.POST['blog_content']
        newBlog = BlogPost.objects.create(blog_title = blogTitle, blog_content=blogContent, user=request.user)
        return redirect(f'/blog/{newBlog.slug}')

    # if the method is get
    return render(request, 'blog/create_blog.html')


def blog(request, slug):
    try:
        blogpost = BlogPost.objects.get(slug=slug)
        user = blogpost.user
    except:
        return render(request, 'blog/404.html')
    context = {
        'blogpost':blogpost,
        'pub_user':user,
    }
    return render(request, 'blog/single_blog.html', context)


@login_required
def myBlogs(request):
    blogs = BlogPost.objects.filter(user=request.user)
    context = {
        'blogs':blogs,
    }
    return render(request, 'blog/my_blogs.html', context)