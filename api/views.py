from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Empolyee
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serialize import CompanySerializer,EmpolyeeSerializer
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all().order_by('name')
    serializer_class=CompanySerializer


    # api/companies/{companyId}/employees

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try: 
            company=Company.objects.get(pk=pk)
            emp=Empolyee.objects.filter(company_name=company)
            emp_serializer=EmpolyeeSerializer(emp,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                "Message":'Company does not exit'
            })


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Empolyee.objects.all()
    serializer_class=EmpolyeeSerializer
