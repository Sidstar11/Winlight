from django import forms
from .models import RecentWork, UpcomingProject, CrewMember, Article


class RecentWorkForm(forms.ModelForm):
    class Meta:
        model = RecentWork
        # UPDATED: Added is_featured field
        fields = ['title', 'image', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control modern-input', 'placeholder': 'Project Title'}),
            'image': forms.FileInput(attrs={'class': 'form-control modern-file-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input modern-checkbox'}),
        }

# (Keep your UpcomingProjectForm, CrewMemberForm, and ArticleForm exactly as they are)
class UpcomingProjectForm(forms.ModelForm):
    class Meta:
        model = UpcomingProject
        fields = ['title', 'description', 'cover_image', 'release_expected', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control modern-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control modern-input', 'rows': 3}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control modern-file-input'}),
            'release_expected': forms.TextInput(attrs={'class': 'form-control modern-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input modern-checkbox'}),
        }

class CrewMemberForm(forms.ModelForm):
    class Meta:
        model = CrewMember
        fields = ['name', 'role', 'photo', 'display_order', 'is_featured']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control modern-input'}),
            'role': forms.TextInput(attrs={'class': 'form-control modern-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-control modern-file-input'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control modern-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input modern-checkbox'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'thumbnail', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control modern-input'}),
            'summary': forms.Textarea(attrs={'class': 'form-control modern-input', 'rows': 2}),
            'content': forms.Textarea(attrs={'class': 'form-control modern-input', 'rows': 5}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control modern-file-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input modern-checkbox'}),
        }