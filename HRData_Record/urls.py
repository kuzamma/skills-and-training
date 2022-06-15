
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('employees.urls')),
    path('authentication/', include('authentication.urls')),
    path('admin/', admin.site.urls),

]
