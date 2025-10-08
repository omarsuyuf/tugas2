from django.urls import path
from main.views import show_main, create_product, show_product
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
from .views import add_product_entry_ajax
from .views import update_product_entry_ajax
from .views import delete_product_entry_ajax

from . import views

app_name = 'main'

urlpatterns = [
    path("", views.show_main, name="show_main"),
    path("add/", views.create_product, name="create_product"),
    path("detail/<uuid:id>/", views.show_product, name="show_product"),
    path("xml/<uuid:id>/", views.show_xml_by_id, name="show_xml_by_id"),
    path("json/<uuid:id>/", views.show_json_by_id, name="show_json_by_id"),
    path("xml/", views.show_xml, name="show_xml"),
    path("json/", views.show_json, name="show_json"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path("create-product-ajax", add_product_entry_ajax, name="add_product_entry_ajax"),
    path("update-product-ajax/<uuid:id>/", update_product_entry_ajax, name="update_product_entry_ajax"),
    path("delete-product-ajax/<uuid:id>/", delete_product_entry_ajax, name="delete_product_entry_ajax"),
]
