from django import forms
from home.models import Post, Subcriber, Contactinfo

class HomeForm(forms.ModelForm):
    # post = forms.CharField(widget=forms.TextInput(
       
    # ))

    class Meta:
        model = Post
        fields ={
            'postfood',
            'foodimg',
            'fooddes',
            

        }

class SubcriberForm(forms.ModelForm):
    class Meta:
        model = Subcriber
        fields ={
        'subcriber'
         }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactinfo
        fields = {
            'name',
            'email',
            'subject',
            'message'
        }