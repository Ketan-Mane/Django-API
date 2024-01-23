from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
# Create your views here.


# Function Based API's
@api_view(['GET','POST',])
def home(request):
    if request.method=="POST":
        return Response(
            {
                'status':200,
                'Response':'Connection Successfull..',
                'Method':'POST'
            }
        )
    elif request.method=="GET":
        return Response(
            {
                'status':200,
                'Response':'Connection Successfull..',
                'Method':'GET'
            }
        )
    

@api_view(['GET'])
def getStudent(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(
        {
            'status':True,
            'message':'data fetched',
            'data':serializer.data
        }
    )


@api_view(['POST'])
def postStudent(request):
    data = request.data
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'status':True,
                'message':'data saved',
                'data':serializer.data
            }
        )
    return Response(
            {
                'status':False,
                'message':'something went wrong',
                'data':serializer.errors
            }
        )


@api_view(['PUT'])
def putStudent(request):
    if request.method=='PUT':
        data = request.data
        student = Student.objects.get(id=data.get('id'))
        serializer = StudentSerializer(student,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status':True,
                    'message':'data saved',
                    'data':serializer.data
                }   
            )
        return Response(
            {
                'status':False,
                'message':'something went wrong',
                'data':serializer.errors
            }
        )
