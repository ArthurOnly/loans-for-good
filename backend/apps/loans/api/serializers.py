from apps.loans.business import create_loan_request
from apps.loans.models import LoanRequest, Question, QuestionOption
from rest_framework import serializers


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ("id", "label", "key")


class QuestionSerializer(serializers.ModelSerializer):
    questionoption_set = QuestionOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "label", "key", "required", "type", "active", "ordering", "questionoption_set")

class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ("id", "status_external", "status_internal", "response", "created_at")

class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ("id", "status_external", "status_internal", "response", "created_at")

class LoanRequestCreateSerializer(serializers.Serializer):
    class LoanRequestResponseSerializer(serializers.Serializer):
        label = serializers.CharField()
        value = serializers.CharField(required=False)
        file = serializers.FileField(required=False)

    response = LoanRequestResponseSerializer(many=True)

    def to_internal_value(self, data):
        """
        Need to convert multipart to NestedSerializer
        """
        formated = {}
        for key, value in data.items():
            index = key.split(".")[1]
            label = key.split(".")[2]
            value = value
            if index not in formated.keys():
                formated[index] = {}
            formated[index][label] = value

        fields = []
        for key, value in formated.items():
            fields.append(value)
        
        return super().to_internal_value({"response": fields})
    
    def to_representation(self, instance):
        return LoanRequestSerializer(instance).data

    def update(self, instance, validated_data):
        raise NotImplementedError()
    
    def create(self, validated_data):
        return create_loan_request(validated_data)