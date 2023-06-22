
from django.urls import path
from SEARCH import views
app_name="SEARCH"
urlpatterns = [
    path('searchresult/',views.searchresult,name="searchresult"),

]
