# from django.shortcuts import render

# # Create your views here.
# def login(request):
  
#     return render(request, 'registration/login.html')

# def register(request):
  
#     return render(request, 'registration/register.html')

# from django.shortcuts import redirect, render
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate , login , logout
# from django.http import HttpResponseRedirect,HttpResponse
# # Create your views here.
# from .models import Profile
# from django.contrib.auth.decorators import login_required


# def login_page(request):
    
    
    
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_obj = User.objects.filter(username = email)

#         if not user_obj.exists():
#             messages.warning(request, 'Account not found.')
#             return HttpResponseRedirect(request.path_info)


#         if not user_obj[0].profile.is_email_verified:
#             messages.warning(request, 'Your account is not verified.')
#             return HttpResponseRedirect(request.path_info)

#         user_obj = authenticate(username = email , password= password)
#         if user_obj:
#             login(request , user_obj)
#             return redirect('home')

        

#         messages.warning(request, 'Invalid credentials')
#         return HttpResponseRedirect(request.path_info)
    
    
    


#     return render(request ,'registration/login.html')


# def register_page(request):

#     if request.method == 'POST':
#         first_name = request.POST.get('firstName')
#         last_name = request.POST.get('lastName')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_obj = User.objects.filter(username = email)

#         if user_obj.exists():
#             messages.warning(request, 'Email is already taken.')
#             return HttpResponseRedirect(request.path_info)

#         print(email)

#         user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
#         user_obj.set_password(password)
#         user_obj.save()

#         messages.success(request, 'An email has been sent on your mail.')
#         return HttpResponseRedirect(request.path_info)


#     return render(request ,'registration/register.html')




# def activate_email(request , email_token):
#     try:
#         user = Profile.objects.get(email_token= email_token)
#         user.is_email_verified = True
#         user.save()
#         return redirect('home')
#     except Exception as e:
#         return HttpResponse('Invalid Email token')
    
# @login_required
# def UserLogout(request):
#     logout(request)
#     return redirect('home')
# from django.shortcuts import render

# # Create your views here.
# def login(request):
  
#     return render(request, 'registration/login.html')

# def register(request):
  
#     return render(request, 'registration/register.html')

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile


def login_page(request):
    
    
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('home')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)
    
    
    


    return render(request ,'registration/login.html')


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'registration/register.html')




def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('home')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    


@login_required
def UserLogout(request):
    logout(request)
    return redirect('home')