from django.shortcuts import render

# Create your views here.
def innogrhomepage(request):
    return render(request, 'homepage/home.html')