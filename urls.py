# mydjangoapp/urls.py

from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('.urls')),  # Add this line to include your app's URLs
]
