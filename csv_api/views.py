from csv_api.models import CustomerMaster
from rest_framework.response import Response
from rest_framework import status
from csv_api.serializers import CustomerMasterSerializer
from rest_framework.views import APIView
import csv, io

class CustomerMasterList(APIView):

    def get(self, request, format = None):
        '''Return a list of API View feature'''

        id=request.GET.get('id')
        if id is not None:
            cm_data = CustomerMaster.objects.get(id=id)
            cm_serializer = CustomerMasterSerializer(cm_data)
            return Response (cm_serializer.data)

        name=request.GET.get('name')
        if name is not None:
            cm_data = CustomerMaster.objects.filter(name__icontains=name)
            cm_serializer = CustomerMasterSerializer(cm_data, many=True)
            return Response (cm_serializer.data)

        email=request.GET.get('email')
        if email is not None:
            cm_data = CustomerMaster.objects.filter(email__icontains=email)
            cm_serializer = CustomerMasterSerializer(cm_data, many=True)
            return Response (cm_serializer.data)

        address=request.GET.get('address')
        if address is not None:
            cm_data = CustomerMaster.objects.filter(address__icontains=address)
            cm_serializer = CustomerMasterSerializer(cm_data, many=True)
            return Response (cm_serializer.data)

        phone=request.GET.get('phone')
        if phone is not None:
            cm_data = CustomerMaster.objects.filter(phone__icontains=phone)
            cm_serializer = CustomerMasterSerializer(cm_data, many=True)
            return Response (cm_serializer.data)

        cm_data = CustomerMaster.objects.all()
        cm_serializer = CustomerMasterSerializer(cm_data, many=True)
        return Response(cm_serializer.data)

    def post(self, request):
        file =  request.FILES['file']
        data_set = file.read().decode()
        io_string = io.StringIO(data_set)
        next(io_string)
        for customer in csv.reader(io_string, delimiter=',', quotechar="|"):
            CustomerMaster(name=customer[0],email=customer[1], 
            address=customer[2], phone=customer[3]).save()

        return Response({'received data': request.data})


    
class CustomerMasterDetail(APIView):

    def get(self, request, pk):
        '''Return a list of API View feature'''
        cm_data = CustomerMaster.objects.get(id=pk)
        cm_serializer = CustomerMasterSerializer(cm_data)
        return Response(cm_serializer.data)

    def delete(self, request, pk=None):
        """Delete an object"""
        cm_data = CustomerMaster.objects.get(id=pk)
        cm_data.delete()
        return Response({'id deleted': pk})

    def put(self, request, pk, format=None):
        cm_data = CustomerMaster.objects.get(id=pk)
        cm_serializer = CustomerMasterSerializer(cm_data, data=request.data)
        if cm_serializer.is_valid():
            cm_serializer.save()
            return Response(cm_serializer.data)
        return Response(cm_serializer.errors, status=status.HTTP_400_BAD_REQUEST)