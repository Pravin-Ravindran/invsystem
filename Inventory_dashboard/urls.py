from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('products/', views.products, name='products'),
path('staff/', views.staff, name='staff'),
path('editorder/<int:order_id>',views.editorder, name='editorder'),
path('deleteorder/<int:order_id>',views.deleteorder, name='deleteorder')
]
#static files are served correctly from the STATICFILES_DIRS directory
urlpatterns+=staticfiles_urlpatterns()
#This pattern maps URLs starting with the STATIC_URL prefix to the files located in the STATIC_ROOT directory.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)