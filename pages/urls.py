from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls'))
    