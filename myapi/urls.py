from django.urls import path, include
from myapi.views import CompanyViewSets, EmployeeViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSets)
router.register(r'employees', EmployeeViewSets)

urlpatterns = [
    path('', include(router.urls))
]
