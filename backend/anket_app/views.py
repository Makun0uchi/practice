from rest_framework import viewsets
from django.core.exceptions import ValidationError
import datetime

from .models import StudentAnket, MentorAnket
from .serializers import StudentAnketSerializer, MentorAnketSerializer


class StudentAnketViewSet(viewsets.ModelViewSet):
    queryset = StudentAnket.objects.all()
    serializer_class = StudentAnketSerializer

    def perform_create(self, serializer):
        self.validate_study_years(serializer.validated_data)
        serializer.save()

    def perform_update(self, serializer):
        self.validate_study_years(serializer.validated_data)
        serializer.save()

    def validate_study_years(self, validated_data):
        start_year = validated_data.get('start_study_year')
        end_year = validated_data.get('end_study_year')

        if end_year < start_year:
            raise ValidationError('Старт обучения не может быть после его конца')
        if start_year and end_year and (end_year - start_year) < 4:
            raise ValidationError('Срок обучения должен составлять не менее 4-х лет')

        curr_date = datetime.date.today()
        if start_year > curr_date.year or (start_year == curr_date.year and curr_date.month < 9):
            raise ValidationError('Старт обучения не может быть в будущем')

        if curr_date.month < 9:
            course = curr_date.year - start_year
        else:
            course = curr_date.year - start_year + 1

        validated_data['course'] = course


class MentorAnketViewSet(viewsets.ModelViewSet):
    queryset = MentorAnket.objects.all()
    serializer_class = MentorAnketSerializer