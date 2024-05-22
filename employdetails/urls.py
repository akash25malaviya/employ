from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employdetails.views import MyModelViewSet,DemoListView

router = DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = [
    path('demos/', DemoListView.as_view(), name='demo-list'),
    path('', include(router.urls)),
]
