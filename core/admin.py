from django.contrib import admin
from .models import Event, Booking, Payment, CheckinLog


from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
       list_display = ['name', 'date', 'organizer', 'location', 'capacity']
      
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status', 'ticket_id')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'booking', 'amount', 'status', 'payment_time')

@admin.register(CheckinLog)
class CheckinLogAdmin(admin.ModelAdmin):
    list_display = ('booking', 'scanned_by', 'checkin_time')
