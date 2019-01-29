from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import faculty
from .serializers import facultySerializer


# Create your views here.


class facultylist(APIView):

    def get(self, request):
        faculty1 = faculty.objects.all()
        serializer = facultySerializer(faculty1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
