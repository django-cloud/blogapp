#for displaying webpages
from django.shortcuts import render, redirect
#importing models
from .models import Blog, Blog_reviews
#for checking if the user is logged in
from django.contrib.auth.decorators import login_required
#for importing forms
from . import forms
#for deleting image files
import os
#for messages
from django.contrib import messages

#displaying list of all blogs
def list(request):
   #getting all blogs
   blogs = Blog.objects.all().order_by('-created_date')
   return render(request , 'blog/index.html', {'blogs': blogs})

#detail of a particular blog
def blog_detail(request, blog_id):
   #getting blog data
   blog = Blog.objects.get(id = blog_id)
   #getting blog comments
   reviews = Blog_reviews.objects.filter(blog = blog).order_by('-created_date')
   #To get the name of the current user(whether to show delete-btn and edit-btn or not)
   authorised = False
   if request.user.is_authenticated:
      user = request.user.username
      if str(blog.author) == user:
         authorised = True
   #dictionary to store data to be passed in the render function
   context = {'blog': blog,'authorised': authorised, 'reviews': reviews}
   return render(request, 'blog/blog_detail.html', context)

@login_required
def create_blog(request):
   #to create blog(post data and create blog)
   if request.method == 'POST':
      form = forms.CreateBlog(request.POST, request.FILES)
      if form.is_valid():
         data = form.save(commit=False)
         data.author = request.user
         data.save()
         msg = 'Your blog has been created!'
         messages.success(request, msg)
      return redirect('blog:list')
   #to create blog(create form and get data)
   else:
      form = forms.CreateBlog()
   return render(request, 'blog/blog_create.html', {'form': form})


@login_required
def delete_blog(request, blog_id):
   #getting data of the blog
   blog = Blog.objects.get(pk = blog_id)
   author = blog.author
   img = blog.img_file_name()

   #checking if the author of the blog and the currently logged in user are the same
   if request.user == author:
      blog.delete()
      #delete the image from images folder
      if not 'default.png' in img:
         os.remove(img)
      #showing success msg
      msg = 'Blog has been deleted!'
      messages.success(request, msg)
   return redirect('blog:list')


@login_required
def delete_blog_review(request, blog_review_id):
   review = Blog_reviews.objects.get(pk = blog_review_id)
   author = review.author

   #checking if the author of the blog and the currently logged in user are the same
   if request.user == author:
      review.delete()
      #showing success msg
      msg = 'Comment has been deleted!'
      messages.success(request, msg)
   return redirect('blog:blog_detail', blog_id = review.blog.pk)


@login_required
def comment_blog(request, blog_id):
   #getting data of the blog
   blog = Blog.objects.get(pk=blog_id)
   #to comment blog(post data and comment blog)
   if request.method == 'POST':
      form = forms.Blog_review_form(request.POST)
      if form.is_valid():
         review = form.save(commit=False)
         review.blog = blog
         review.author = request.user
         # review.author = request.user
         review.save()
         return redirect('blog:blog_detail', blog_id = review.blog.pk)
   #to comment blog(create form and get data)
   else:
      form = forms.Blog_review_form()
   #dictionary to store data to be passed in the render function
   context = {'form': form, 'blog_id': blog_id}
   return render(request, 'blog/comment_blog.html', context)

@login_required
def edit_blog(request, blog_id):
   #getting data of the blog
   blog = Blog.objects.get(pk=blog_id)
   #if the current user and the author of the blog are same
   if blog.author == request.user:
      #to edit blog(post data and edit blog)
      if request.method == 'POST':
         form = forms.Edit_Blog(request.POST, request.FILES, instance=blog)
         if form.is_valid():
            form.save()
            return redirect('/'+str(blog_id))
      #to edit blog(create form and get data)
      else:
         form = forms.Edit_Blog(instance=blog)
      #dictionary to store data to be passed in the render function
      context = {'form': form,'blog':blog,'blog_id': blog_id}
      return render(request, 'blog/edit_blog.html', context)
   else:
      error_msg = 'Sorry! you are not authorised'
      return render(request, 'errors.html', {'error_msg':error_msg})

#confirmation for deletion of the blog
@login_required
def delete_blog_confirmation(request, blog_id):
   return render(request, 'blog/delete-confirmation.html', {'blog_id': blog_id})

#displaying the about page
def about(request):
    return render(request, 'about.html')

def announcements(request):
   msg = 'No announcements yet!'
   return render(request, 'informations.html', {'msg':msg})

def calenders(request):
   msg = 'No calenders yet!'
   return render(request, 'informations.html', {'msg':msg})

def portfolio(request):
   return render(request, 'portfolio.html')