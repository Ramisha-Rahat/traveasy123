from django.shortcuts import render

# Create your views here.
def aboutus(request):
    context={}
    return render(request, 'aboutus/aboutus.html', context)
