from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecipeForm
from .models import Recipe




def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
		
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'recipes':recipes})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
            
    
    return render(request, 'register.html', {'form':form})


def recipe(request, pk):
	if request.user.is_authenticated:
		recipe = Recipe.objects.get(id=pk)
		return render(request, 'recipe.html', {'recipe':recipe})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def add_recipe(request):
    recipes = Recipe.objects.all()
    
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            image = request.FILES.get('image') 
            
            new_recipe = Recipe.objects.create(
                name = data['name'],
                description = data [ 'description'],
                image=image, 
                )
            messages.success(request, "You have successfully published a new recipe. Congratulations!")
            return redirect('home')
        
    return render(request, 'add_recipe.html',)
    