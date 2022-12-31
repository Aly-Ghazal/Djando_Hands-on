from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('',views.renderhtml),
    path('cars/',views.viewcars,name="cars"),
    path('Createcar/',views.CreateCar,name="Createcar"),
    path('showcar/<ID>',views.ShowCarWithID,name="showwithid"),
    path('deletecar/<ID>',views.DeleteCarWithID,name="deletewithid"),
    path('updatecar/<ID>',views.UpdateCarWithID,name="updatewithid"),

]
