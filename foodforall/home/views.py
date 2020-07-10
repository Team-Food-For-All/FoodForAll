from django.shortcuts import render
from django.http import HttpResponse
# # Create your views here.
# def home(request):
#     return HttpResponse('It works')

from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse,redirect


class HomeView(TemplateView):
    template_name = "home.html"

    

    def get(self, request):
        form = SubcriberForm()
        carosels = Carosel.objects.all()
        partners = Partner.objects.all()
        donaters = Donater.objects.all()
        args = {'carosels': carosels,
                'partners': partners, 
                'donaters': donaters,
                'form':form
                                     }
        # args1= {'partners': partners}
        
        return render(request, self.template_name,args)
    
    # def get(self, request):
        
    #     partners = Partner.objects.all()
        
    #     args1 = {'partners': partners} 
    #     return render(request, self.template_name, args1)

    def post(self, request):
        form = SubcriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/home')

        args = {'form':form }
        return render(request,self.template_name, args)




from home.models import Post, Carosel, Partner, Donater
from home.forms import HomeForm, SubcriberForm
from django.views.generic import ListView, CreateView 

class postfood(TemplateView):
    template_name = "postfood.html"

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all()
        args = {'form':form , 'posts':posts}
        return render(request,self.template_name, args )

    def post(self, request):
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.foodimg = request.foodimg
            post.user = request.user
            form.save()

            # text = form.cleaned_data['postfood']
            # form = HomeForm()
            return redirect ('/postfood')
        

        args = {'form':form , 'text': text}
        return render(request,self.template_name, args)






