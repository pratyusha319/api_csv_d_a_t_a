from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *
import csv

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app.serializers import *


def bank_upload(file_path):
    a = 'C:\\Users\\Pratyusha\\OneDrive\\Desktop\\74de6\\workplace\\Scripts\\api\\bank.csv'
    
    with open(a, 'r') as file:
        csv_data = csv.reader(file)
          # Skip the header row if it exists
        next(csv_data)
        i=1
        for row in csv_data:
            print(i)
            i+=1
            bn=row[0].strip()
            instance = Bank(bank_name=bn,)
           
            instance.save()

       

        return HttpResponse('successful')

def branch_upload(file_path):
    b = 'C:\\Users\\Pratyusha\\OneDrive\\Desktop\\74de6\\workplace\\Scripts\\api\\branch1.csv'
    
    with open(b, 'r') as file:
        csv_data = csv.reader(file)
          # Skip the header row if it exists
        next(csv_data)
        i=1
        for row in csv_data:
              i+=1
              bank_name = row[0]
              print(row[0])
              bo = Bank.objects.filter(bank_name=bank_name)[0]
              instance = Branch(
                      bank_name=bo,            
                      
                      ifsc = row[1],
                      branch = row[2],
                      address =row[3],
                      contact=row[4],
                      city = row[5],
                      district = row[6],
                      state = row[7],)
                                  
              instance.save()


       

        return HttpResponse('successful')







# def display(request):
#     BO=Branch.objects.all()
#     d = {'BO': BO}
#     return render(request, 'display.html',d)




class branchjd(ViewSet):
    def list(self,request,):
        ATO=Branch.objects.all()
        STD=Branchserializers(ATO,many=True)
        return Response(STD.data)
    

    def create(self,request):
        bmsd=Branchserializers(data=request.data)
        if bmsd.is_valid():
            bmsd.save()
            return Response({'message':'branch is created'})
       
        return Response({'message':'branch creation is failed'})
    def retrieve(self,request,pk):
        po=Branch.objects.get(pk=pk)
        pmsd=Branchserializers(po)
    
        return Response(pmsd.data)
    

    def update(self,request,pk):
      
        bo=Branch.objects.get(pk=pk)
        ubo=Branchserializers(bo,data=request.data)
      
        if ubo.is_valid():
            ubo.save()
            return Response({'message':'brancht is updated'})
       
        return Response({'message':'branch updation is failed'})

    def partial_update(self, request, pk):
       
        bo=Branch.objects.get(pk=pk)
        ubo=Branchserializers(bo,data=request.data,partial=True)
        if ubo.is_valid():
            ubo.save()
            return Response({'message': 'branch is partially updated'})
        return Response({'message':'branch updation is failed'})

        

    def destroy(self,request,pk ):
        
        Branch.objects.get(pk=pk).delete()
        
        return Response({'success': 'branch is deleted'})

class bankjd(ViewSet):
    def list(self,request,):
        ATO=Bank.objects.all()
        STD=Bankserializers(ATO,many=True)
        return Response(STD.data)
    

    def create(self,request):
        bmsd=Bankserializers(data=request.data)
        if bmsd.is_valid():
            bmsd.save()
            return Response({'message':'Bank is created'})
       
        return Response({'message':'Bank creation is failed'})
    def retrieve(self,request,pk):
        po=Bank.objects.get(pk=pk)
        pmsd=Bankserializers(po)
    
        return Response(pmsd.data)
    

    def update(self,request,pk):
      
        bo=Bank.objects.get(pk=pk)
        ubo=Bankserializers(bo,data=request.data)
      
        if ubo.is_valid():
            ubo.save()
            return Response({'message':'Bank is updated'})
       
        return Response({'message':'Bank updation is failed'})

    def partial_update(self, request, pk):
       
        bo=Bank.objects.get(pk=pk)
        ubo=Bankserializers(bo,data=request.data,partial=True)
        if ubo.is_valid():
            ubo.save()
            return Response({'message': 'Bank is partially updated'})
        return Response({'message':'bank updation is failed'})

        

    def destroy(self,request,pk ):
        
        Bank.objects.get(pk=pk).delete()
        
        return Response({'success': 'Bank is deleted'})