from django.urls import path
from .import views

app_name = "notes"

urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add_note_sql_injection,name="add"),
    path('delete/<int:note_id>/',views.delete_note,name="delete"),
    path('cookie/',views.set_cookie_data,name="set_cookie"),

]
    