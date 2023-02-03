from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from myapi.models import Company, Employee
from myapi.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #companies/{companyID}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(emp, many=True, context={'request':request})       
            return Response(emp_serializer.data)
        except Exception as e:
            return Response({'message':'Company might not be exists'})


class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer