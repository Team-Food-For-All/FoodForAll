from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render (request, 'home.html')

# def login(request):
#     return render (request, 'login.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request,'reg_form.html', args)