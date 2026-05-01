from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import UserName

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        
        if name:
            user_name = UserName.objects.create(name=name)
            all_names = UserName.objects.all()
            
            return render(request, 'test_app/home.html', {
                'name': name,
                'show_greeting': True,
                'all_names': all_names,
                'saved': True
            })
    
    all_names = UserName.objects.all()
    return render(request, 'test_app/home.html', {
        'show_greeting': False,
        'all_names': all_names
    })