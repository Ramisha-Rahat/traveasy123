from django.shortcuts import render,redirect
from .forms import UserCarSubmissionForm
from .models import UserCar

def car_submission_view(request):
    if request.method == 'POST':
        form = UserCarSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCarSubmissionForm()
    return render(request, 'user/user.html', {'form': form})