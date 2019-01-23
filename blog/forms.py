from django import forms

from .models import Article

class ItemForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'contents',
            'active',
        
        ]