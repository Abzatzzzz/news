from django import forms
from .models import News


class AddNewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'is_published']



