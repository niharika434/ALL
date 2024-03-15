from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import*

class ProductCrud(APIView):
    def get(self,request,id):
        PDO=Product.objects.all()
        PJO=ProductModelSerializer(PDO,many=True)

        #PDO=Product.objects.get(id=id)
        #PJO=ProductModelSerializer(PDO)
        return Response(PJO.data)
    
    def post(self,request,id):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'data is inserted succesfully'})
        else:
            return Response({'error':'Data is not inserted'})



    def put(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=ProductModelSerializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})

    def patch(self,request,id):
        PO=Product.objects.get(id=id)
        UPO=ProductModelSerializer(PO,data=request.data,partial=True)
        if UPO.is_valid():
            UPO.save()
            return Response({'update':'updated successfully'})
        else:
            return Response({'error':'Update is not done'})


    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'deletion':'Data is Deleted'})
