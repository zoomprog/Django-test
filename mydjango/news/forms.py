from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','content',"is_published",'category']
        widgets ={
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'content':forms.Textarea(attrs={"class":"form-control"}),
            'category':forms.Select(attrs={"class": "form-control"}),

        }

