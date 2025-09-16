from django.urls import path
from main.views import show_main, create_product, show_product
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
]
