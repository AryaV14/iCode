from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
            
            'name': request.user
        }

    return render(request, 'profilec/index.html', context)
