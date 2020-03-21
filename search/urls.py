from django.urls import path, include
from search.views import search, thumbs_up

urlpatterns = [
    path('',search),
    path('upvote/', thumbs_up)
]
