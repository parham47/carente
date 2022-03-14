from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('' , views.carsIndex.as_view() , name = 'cars'),
    #path('user/<int:user_id>' , views.UsercarsIndex.as_view() , name = 'user.cars'),
    path('cars/send/' , views.SendcarsView.as_view() , name = 'cars.send'),
    # path('cars/send/store' , views.store , name = 'cars.send.store'),
    # /cars/<int:cars_id>
    path('<int:pk>/' , views.SinglecarsView.as_view() , name = 'car'),
    path('<int:pk>/edit' , views.EditcarsView.as_view() , name= 'cars.edit'),
    
    path('home/', views.home),
    path('formjadid/', views.formjadid),

]
