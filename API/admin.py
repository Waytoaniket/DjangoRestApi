from django.contrib import admin
from API.models import Advisor, Users, CallBooked

# Register your models here.

admin.site.register(Advisor)
admin.site.register(Users)
admin.site.register(CallBooked)

