from . import views
from django.urls import path

app_name = "food"
urlpatterns = [
    # food/
    path("", views.show_list, name="show_list"),
    # food/item_id
    path("<int:item_id>/", views.detail, name="detail"),
    path("item/", views.show_item, name="items"),
    # add items
    path("add", views.create_item, name="create_item"),
    # edit item
    path("update/<int:id>/", views.update_item, name="update_item"),
    #delete item
    path("delete/<int:id>/", views.delete_item, name="delete_item"),
]
