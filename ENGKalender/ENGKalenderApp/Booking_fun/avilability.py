import datetime
from ENGKalenderApp.models import Booking, Books

def check_Avil (booking, slot_from, slot_to):

    avail_list = []
    booking_list = Books.objects.filter(booking=booking)
    for booking in booking_list:
        if booking.slot_from > slot_to or booking.slot_to < slot_from:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

