
from rest_framework import serializers

from api.models import Company,Empolyee
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

       

class EmpolyeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id=serializers.ReadOnlyField()
    class Meta:
        model=Empolyee
        fields="__all__"

