from django.urls import path
from teldir.views import (CategoryView, ContactView)

app_name = "teldir"

urlpatterns = [
    path('category/<int:crud>/<int:pk>', CategoryView.as_view(), name='category_index'),
    path('book/<int:crud>/<int:pk>', ContactView.as_view(), name='contact_index'),
]
