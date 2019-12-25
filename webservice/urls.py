from django.contrib import admin
from django.urls import path
from seqcollazt import views as seqcollazt_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seq/', seqcollazt_view.calc),
    path('', seqcollazt_view.home),

]
