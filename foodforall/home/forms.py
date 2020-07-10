from django import forms
from home.models import Post, Subcriber

class HomeForm(forms.ModelForm):
    # post = forms.CharField(widget=forms.TextInput(
       
    # ))

    class Meta:
        model = Post
        fields ={
            'postfood',
            'foodimg',
            'fooddes',
            'user'

        }

class SubcriberForm(forms.ModelForm):
    class Meta:
        model = Subcriber
        fields ={
        'subcriber'
         }