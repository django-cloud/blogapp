from django import forms
from . import models

#form for creating new blog
class CreateBlog(forms.ModelForm):
    #to remove the currently and clear
    image = forms.ImageField(label=('Blog Image'), required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = models.Blog
        fields = ('title','body','image')

#form for creating new blog review(comment)
class Blog_review_form(forms.ModelForm):
    class Meta:
        model = models.Blog_reviews
        fields = ('comment',)

#form for editing blog
class Edit_Blog(forms.ModelForm):
    #to remove the currently and clear
    image = forms.ImageField(label=('Blog Image'), required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = models.Blog
        fields = ('title','body','image')
