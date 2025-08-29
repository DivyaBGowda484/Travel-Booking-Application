from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Booking
from .forms import BookingForm
from travel.models import TravelOption
from django.contrib import messages

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def book_travel(request, travel_id):
    travel = get_object_or_404(TravelOption, travel_id=travel_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel

            if booking.number_of_seats > travel.available_seats:
                messages.error(request, "Not enough seats available.")
            else:
                travel.available_seats -= booking.number_of_seats
                travel.save()
                booking.total_price = booking.number_of_seats * travel.price
                booking.booking_date = timezone.now()
                booking.status = "confirmed"
                booking.save()
                messages.success(request, "Booking confirmed successfully!")
                return redirect('booking_list')
    else:
        form = BookingForm()

    return render(request, 'bookings/book_travel.html', {'form': form, 'travel': travel})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)

    if booking.status == "confirmed":
        booking.status = "cancelled"
        booking.save()
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()

    return redirect('booking_list')
