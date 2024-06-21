from django.shortcuts import render

# Create your views here.
def blog(request):
    context={}
    return render(request, 'blog/blog.html', context)

def pricing(request):
    context={}
    return render(request, 'blog/pricing.html', context)

def terms(request):
    context={}
    return render(request, 'blog/terms.html', context)


