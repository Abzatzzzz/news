from django import forms
from .models import News


class AddNewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "category", "is_published"]
        labels = {'title': 'Название'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}), 
            'category': forms.Select(attrs={'class': 'form-control'}), 
        } # in official doc this part doesn't work correctly https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/   forms. absents
