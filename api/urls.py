from django.urls import include, path
from rest_framework import routers
from . import views
from .views import apiViewSet

# router = routers.DefaultRouter()
# router.register(r'books', views.apiViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/',apiViewSet.as_view()),
    path('books/', apiViewSet.as_view()),
    path('books/<int:id>', apiViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]