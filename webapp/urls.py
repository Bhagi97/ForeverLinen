from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^about.html$', views.about, name='about'),
    url(r'^product.html$', views.product_view, name='products'),
    url(r'^product_detail/(?P<id_value>[0-9]+)/$', views.product_detail_view, name='product_detail_view'),
    url(r'^quick_view/(?P<id_value>[0-9]+)/$', views.quick_view, name='quick_view'),
    url(r'^add/(?P<item_name>.*)$', views.add_cart, name='add_to_cart'),

    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
