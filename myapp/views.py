from django.shortcuts import render,redirect
from . models import turfs,Booking
from .forms import BookingForm
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')


def turf(request):
    dict_tur={
        'tur':turfs.objects.all()
    }
    return render(request,'turf.html',dict_tur)

def check_availability(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if Booking.objects.filter(
                turf=booking.turf,
                start_time__lt=booking.end_time,
                end_time__gt=booking.start_time
            ).exists():
                return render(request, 'availability.html', {
                    'form': form,
                    'error': 'The selected time slot is not available.'
                })
            booking.save()
            return render(request, 'availability.html', {
                    'message':'Booking Successful.'
                })
            
    else:
        form = BookingForm()
    return render(request, 'availability.html', {'form': form})


def contactus(request):
    return render(request, 'contactus.html')
