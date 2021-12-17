from django.urls import path
from .import views

urlpatterns=[
    path('add/',views.laptop,name='add_lap'),
    path('show/',views.show,name='show_lap'),
    path('del/<int:i>',views.delete,name='delete_lap'),
    path('upd/<int:i>',views.update,name='update_lap')

]