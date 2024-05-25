from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost
from .forms import NewBlogForm,commentForm,searchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def all_blogs(request):
    recent_blogs = BlogPost.objects.all()
    #searchbar
    form=searchForm()
    if request.method == 'POST' and form.is_valid:
        form = searchForm(request.POST)
        form.save(commit=False)
        query = form.cleaned_data['query']
        matching_blogs = BlogPost.objects.filter(title__icontains = query)
        return render(request,'blogs/all_blogs.html',{'matching_blogs':matching_blogs})
    return render(request,'blogs/all_blogs.html',{'recent_blogs':recent_blogs})

def create_blog(request):
    if not request.user.is_authenticated:
        return render(request,'main/login.html',{'message':"Log in to post blogs"})
    form = NewBlogForm()
    if request.method == 'POST':
        form = NewBlogForm(request.POST,request.FILES)
        if form.is_valid:
            blog = form.save(commit=False)
            blog.posted_by = request.user
            if 'image_small' in request.FILES:
                image = request.FILES['image_small']
                blog.image_small = image

            blog.save()
            return redirect('blogs:BlogsPage')
        return render(request,'blogs/CreateBlogPage.html')
    return render(request,'blogs/CreateBlogPage.html',{'form':form})

def blog_post(request,title):
    blog = get_object_or_404(BlogPost,title=title)
    comment = commentForm()
    comment.comment_on = title
    #posting comments
    if request.method == 'POST':
        comment = commentForm(request.POST,request.FILES)

        if comment.is_valid:
            comment = comment.save(commit=False)
            comment.comment_by = request.user
            comment.comment_on = BlogPost.objects.get(title=title)
            
            if 'image' in request.FILES:
                image = request.FILES['image']
                comment.image = image
                print('*************************')
                if comment.image:
                    print("IMAGE SAVED!!!!")
            comment.save()
            all_comments = blog.blog_comments.all()
            return render(request, 'blogs/BlogPage.html',{'blog':blog,'all_comments':all_comments})

        else:
            all_comments = blog.blog_comments.all()
            error = "The only kind of file you are allowed to upload are images."
            return render(request, 'blogs/BlogPage.html',{'blog':blog,'error':error,'all_comments':all_comments})


    else:
        all_comments = blog.blog_comments.all()
        return render(request, 'blogs/BlogPage.html',{'blog':blog,'all_comments':all_comments})

def user_blogs(request,user_id):
    if not request.user.is_authenticated:
        return render(request,'main/login.html',{'message':"Log in to proceed."})
    user = get_object_or_404(User,id=user_id)
    user_blogs = user.related_blogs.all()
    return render(request,"blogs/user's_blogs.html",{'user_blogs':user_blogs,'Blogger':user.username})

#delete blog
@login_required
def delete_blog(request,title):
    blog = get_object_or_404(BlogPost,title=title)
    blog.delete()

    return render(request,"blogs/user's_blogs.html",{'message':"Blog deleted successfully!"})