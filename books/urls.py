from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'ratings', views.RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]