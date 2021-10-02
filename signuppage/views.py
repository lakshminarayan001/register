from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.serializers import SerializerMetaclass
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import signuppage
from . serializers import signuppageSerializer
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from signuppage import serializers


# Create your views here.


class signupapi(APIView):

    def get_object(self, pk):
        try:
            return signuppage.objects.filter(pk=pk)
        except signuppage.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = signuppage.objects.all()

        serializer = signuppageSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = signuppageSerializer(data=data)

        serializer.is_valid(raise_exception=True)

# True
        # serializer.validated_data

        serializer.save()

        response = Response()

        response.data = {
            'message': 'signuppage Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        User_to_update = signuppage.objects.get(pk=pk)
        serializer = signuppageSerializer(
            instance=User_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'signuppage Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        User_to_delete = signuppage.objects.get(pk=pk)

        User_to_delete.delete()

        return Response({
            'message': 'signuppage Deleted Successfully'
        })

    # def get_object(self,  pk):
    #     try:
    #         return signuppage.objects.filter(pk=pk)
    #     except signuppage.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk=None, format=None):
    #     if pk:
    #         data = self.get_object(pk)
    #     else:
    #         data = signuppage.objects.all()

    #     serializer = signuppageSerializer(data, many=True)

    #     return Response(serializer.data)

    # def post(self, request):
    #     data = signuppage.objects.all()
    #     serializers = signuppageSerializer(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk=None, format=None):
    #     signuppage1 = self.get_object(pk=pk)
    #     signuppage1.delete()
    #     return Response(status=status.HTTP_202_ACCEPTED)
