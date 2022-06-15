from django.contrib import admin
from .models import seminars, workshops, Employee


admin.site.register(seminars)
admin.site.register(workshops)
admin.site.register(Employee)