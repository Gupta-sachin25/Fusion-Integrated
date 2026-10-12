from rest_framework import serializers
from modules.elm.models import LeaveRequest, LeaveCategory

class LeaveRequestSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=LeaveCategory.choices)

    class Meta:
        model = LeaveRequest
        fields = '__all__'
