from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from datetime import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from weasyprint import HTML  # type: ignore
from cars.models import Car

@login_required
def cart(request):
    car_name = request.GET.get('car_name')
    car_company = request.GET.get('car_company')
    car_image = request.GET.get('car_image')
    car_price = request.GET.get('car_price')
    
    
    car_image_url = request.build_absolute_uri(car_image)
    

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = Booking(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                driver_license=form.cleaned_data['driver_license'],
                cnic=form.cleaned_data['cnic'],
                start_date=form.cleaned_data['start_date'],
                return_date=form.cleaned_data['return_date'],
                car_name=form.cleaned_data['car_name'],
                car_company=form.cleaned_data['car_company'],
                car_image=form.cleaned_data['car_image'],
                car_price=form.cleaned_data['car_price'],
            )
            booking.save()

            rental_days = (booking.return_date - booking.start_date).days
            price_per_day = float(form.cleaned_data['car_price'])  
            total_price = rental_days * price_per_day

            # Pass booking ID and total price to success page
            request.session['booking_id'] = booking.id
            request.session['total_price'] = total_price

            return redirect('success')
    else:
        form = BookingForm(initial={
            'car_name': car_name,
            'car_company': car_company,
            'car_image': car_image_url,
            'car_price': car_price
        })

    context = {
        'form': form,
        'car_name': car_name,
        'car_company': car_company,
        'car_image': car_image_url,
        'car_price': car_price
    }
    return render(request, 'cart/cart.html', context)

def success(request):
    booking_id = request.session.get('booking_id')
    total_price = request.session.get('total_price')
    booking = Booking.objects.get(id=booking_id)

    context = {
        'booking': booking,
        'total_price': total_price
    }
    return render(request, 'cart/success.html', context)

def send_receipt_email(booking, total_price):
    context = {
        'booking': booking,
        'total_price': total_price
    }
    html_content = render_to_string('cart/receipt.html', context)
    pdf_content = HTML(string=html_content).write_pdf()

    email = EmailMessage(
        'Booking Receipt',
        'Thank you for your booking. Please find attached your receipt.',
        'from@example.com',
        [booking.email],
    )
    email.attach('receipt.pdf', pdf_content, 'application/pdf')
    email.send()

def send_rejection_email(booking):
    context = {
        'booking': booking
    }
    html_content = render_to_string('cart/reject.html', context)
    email = EmailMessage(
        'Booking Rejection',
        'We apologize for the inconvenience, but your application has been rejected due to incorrect information.',
        'from@example.com',
        [booking.email],
    )
    email.send()

@login_required
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    total_price = (booking.return_date - booking.start_date).days * float(booking.car_price)
    send_receipt_email(booking, total_price)
    return redirect('adminpanel')  

@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    send_rejection_email(booking)
    return redirect('adminpanel')  
