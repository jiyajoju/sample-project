from django.contrib import admin
from .models import Department,Doctor,booking

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(booking)

