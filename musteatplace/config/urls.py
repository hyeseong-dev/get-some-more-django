from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('shareRes.urls')),
	path('sendEmail/', include('sendEmail.urls')),
]
