#for displaying webpages
from django.shortcuts import render, redirect
#for checking if the user is logged in
from django.contrib.auth.decorators import login_required
#for login and signup
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
#for importing forms
from . forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
#for showing profiles
from django.contrib.auth.models import User
#importing models
from blog.models import Blog
#for messages
from django.contrib import messages

def signup_user(request):
    #if user is already logged in
    if request.user.is_authenticated:
        msg = 'You are already logged in!'
        return render(request, 'errors.html', {'msg': msg})
    else:
        #for signing up the user(post data and show errors if any)
        if request.method == 'POST':
            #registering data entered by the user
            form = RegistrationForm(request.POST)
            if form.is_valid():
                #getting username the user
                user = form.save()
                username = form.cleaned_data.get('username')
                #for displaying success msg
                msg = 'Account created for ' + username +'. You have been logged in.'
                messages.success(request, msg)
                #for logging in the user
                login(request, user)
                return redirect('blog:list')
        #for signing up the user(create form and get data)
        else:
            form = RegistrationForm()
        return render(request, 'accounts/signup.html', {'form': form})

def login_user(request):
    #if user is already logged in
    if request.user.is_authenticated:
        msg = 'You are already logged in.'
        return render(request, 'errors.html', {'msg': msg})
    else:
        #for loging in the user(post data and show errors if any)
        if request.method == 'POST':
            #registering data entered by the user
            form = AuthenticationForm(data = request.POST)
            if form.is_valid():
                #getting username the user
                user = form.get_user()
                username = form.cleaned_data.get('username')
                #for displaying success msg
                msg = 'User ' + username + ' has been logged in!'
                messages.success(request, msg)
                login(request, user)
                #to redirect to createblog page(if user arrived this page through createblog page)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                #to redirect to blog list
                else:
                    return redirect('blog:list')
        #for loging in the user(create form and get data)
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'accounts/logged-out.html')
    else:
        msg = 'You are not logged in.'
        return render(request, 'errors.html', {'msg': msg})

#showing profle of the current user
@login_required
def user_profile(request):
    #all blogs by the user
    blogs = Blog.objects.filter(author = request.user).order_by('created_date')
    #to update user profile
    #for updating user profile(post data and show errors if any)
    if request.method == 'POST':
        #creatinf forms
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #showing success msg
            msg = 'Your profile has been updated!'
            messages.success(request, msg)
            return redirect('accounts:user_profile')
    #for updating user profile(create form and get data)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    #dictionary to store data to be passed in the render function
    context = {'u_form' : u_form , 'p_form' : p_form,'blogs': blogs}
    return render(request, 'accounts/profile.html', context)

#showing profile of other users
def show_user_profile(request, user_id):
    #information about the user
    user = User.objects.get(id = user_id)
    #all blogs by the user
    blogs = Blog.objects.filter(author=user).order_by('created_date')
    return render(request, 'accounts/show_profile.html', {'user': user,'blogs': blogs})