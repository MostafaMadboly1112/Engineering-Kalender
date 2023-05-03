from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Booking, Books
from .forms import AvailForm
from ENGKalenderApp.Booking_fun.avilability import check_Avil

# Create your views here.

class Booking_list(ListView):
    model = Booking

class Booking_list(ListView):
    model = Books

class BookingView(FormView):
    form_class = AvailForm
    template_name = 'avilability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        booking_list = Booking.objects.filter(category=data['category'])
        available_slots = []
        for booking in booking_list:
            if check_Avil(booking, data['slot_from'], data['slot_to']):
                available_slots.append(booking)
        
        if len(available_slots) > 0:
            slot = available_slots[0]
            booking = Books.objects.create(
                user = self.request.user,
                booking = slot,
                slot_from = data['slot_from'],
                slot_to = data['slot_to']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This Slot is taken')