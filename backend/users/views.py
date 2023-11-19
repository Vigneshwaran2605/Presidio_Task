from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm,FlightForm
from .models import Flight,Booking
from django.core.mail import send_mail

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def search_flights(request):
    if request.method == 'POST':
        date = request.POST['date']
        from_location = request.POST['from_location']
        to_location = request.POST['to_location']
        flights = Flight.objects.filter(date=date, from_location=from_location, to_location=to_location)
        return render(request, 'users/flight_search.html', {'flights': flights})
    return render(request, 'users/flight_search.html')

@login_required
def book_flight(request):
    error_message = None  # Initialize error message variable

    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        num_bookings = int(request.POST.get('num_bookings'))

        flight = Flight.objects.get(id=flight_id)

        if num_bookings <= flight.available_seats:
            for _ in range(num_bookings):
                Booking.objects.create(user=request.user, flight=flight)
                flight.available_seats -= 1
            flight.save()
            messages.success(request, 'Flights booked successfully!')
            return redirect('my_bookings')
        else:
            error_message = 'Number of bookings exceeds available seats.'
    
    # Render the same page with error message
    return render(request, 'users/book_flight.html', {'error_message': error_message})

@login_required
def cancel_flight(request):
    error_message = None
    bookings = Booking.objects.all()
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')

        try:
            booking = Booking.objects.get(id=booking_id)
            flight = booking.flight

            # Update the available seats and delete the booking
            flight.available_seats += 1
            flight.save()
            booking.delete()

            messages.success(request, 'Flight booking canceled successfully!')
        except Booking.DoesNotExist:
            messages.error(request, 'Booking not found.')
            error_message = 'Booking not found.'
            return render(request, 'users/cancel_flight.html',{'error_message': error_message})

    return render(request, 'users/cancel_flight.html',{'Bookings': bookings})



@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'users/my_bookings.html', {'bookings': bookings})

@login_required
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flight added successfully!')
            return redirect('show_flights')
    else:
        form = FlightForm()
    context = {'form': form}
    return render(request, 'users/add_flight.html', context)


@login_required
def remove_flight(request):
    flights = Flight.objects.all()
    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        try:
            flight = Flight.objects.get(id=flight_id)
            flight.delete()
            messages.success(request, 'Flight removed successfully!')
            return redirect('show_flights')
        except Flight.DoesNotExist:
            messages.error(request, 'Flight not found.')
            return redirect('remove_flight')        
    return render(request, 'users/remove_flight.html',{'flights': flights})


@login_required
def view_bookings(request):
    flights = Flight.objects.all()
    flight_id = request.GET.get('flight_id')

    if flight_id:
        bookings = Booking.objects.filter(flight_id=flight_id)
    else:
        bookings = []

    return render(request, 'users/view_bookings.html', {'bookings': bookings,'flights': flights})
@login_required
def show_flights(request):
    flights = Flight.objects.all()
    return render(request, 'users/show_flights.html', {'flights': flights})

@login_required
def show_flights_user(request):
    flights = Flight.objects.all()
    return render(request, 'users/show_flights_user.html', {'flights': flights})

