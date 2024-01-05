from django.contrib import admin
from django.urls import path, include
import static_pages.urls  # Import the urls from your static_pages app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(static_pages.urls))  # Correctly include the URLs from static_pages
]
