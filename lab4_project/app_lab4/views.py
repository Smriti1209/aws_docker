from django.shortcuts import render
import pymongo

from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import json

# Create your views here.
def index(request):
    return render(request,'home.html') #,{"out1":out1})


def list_student(request):
    client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
    db = client.AWS
    coll = db.Student
    print(coll.find())
    # coll.find_one({"name":"room2"})
    #form=FilterCriteria()
    return render(request, 'list_student.html' , {'students': coll.find()})#,'form':form})
    # return render(request,'home.html')


def action_student(request):
    student_id=""
    print("hi")
    if "delete_button" in request.POST:
        student_id=request.POST.get("delete_button")
        print("id=",student_id)
        client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
        db = client.AWS
        coll = db.Student
        # Delete Document with univ_id
        result = coll.delete_one({"univ_id":student_id})
        delete_output="Student details with university ID={} has been deleted.".format(student_id)
        return render(request, 'list_student.html',{
            'delete_output': delete_output, 'students': coll.find(),
        })
    elif "edit_button" in request.POST:
        student_id=request.POST.get("edit_button")
        print("id=",student_id)
        client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
        db = client.AWS
        coll = db.Student
        print(coll.find())
        coll.find_one({"univ_id":student_id})
        return render(request, 'edit_student.html',{
            'student_id': student_id, 'student': coll.find_one({"univ_id":student_id}),
        })
        # instance_id=request.POST.get("start_button")


def edit_action(request):
    student_id=""
    if "edit_submit" in request.POST:
        student_id=request.POST.get("univ_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        age=request.POST.get("age")
        course=request.POST.get("course")
        client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
        db = client.AWS
        coll = db.Student
        myquery = { "univ_id": student_id }
        newvalues = { "$set": { "age": age, "course": course} }

        coll.update_one(myquery, newvalues)
        edit_output="Details of the student with university id ={} has been updated successfully!".format(student_id)



        return render(request, 'list_student.html',{
            'edit_output': edit_output,'students': coll.find(),
        })

def add_student(request):
    return render(request,'add_student.html')

def add_action(request):
    student_id=""
    if "add_submit" in request.POST:
        student_id=request.POST.get("univ_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        age=int(request.POST.get("age"))
        course=request.POST.get("course")
        client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
        db = client.AWS
        coll = db.Student
        newvalues = { "univ_id":student_id,"first_name":first_name,"last_name":last_name,"age":age,"course":course}

        coll.insert_one( newvalues)
        add_output="Details of the student with university id ={} has been added successfully!".format(student_id)



        return render(request, 'list_student.html',{
            'add_output': add_output,'students': coll.find(),
        })


def search_student(request):
    return render(request,'search_student.html')

def search_validate(request):
    student_id=""
    if "search_submit" in request.POST:
        student_id=request.POST.get("univ_id")
        client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
        db = client.AWS
        coll = db.Student
        return render(request, 'search_student.html',{
            'student': coll.find_one({"univ_id":student_id}),
        })

# GET list of all students and POST students details
@api_view(['GET', 'POST'])
def student_list(request):
     
    if request.method == 'GET':
        print(Student.objects)
        client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
        db = client.AWS
        coll = db.Student
        student=coll.find()
        print(student)
        student_serializer = StudentSerializer(student, many=True)
        print("after serial get",student_serializer.data)
        return JsonResponse(student_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        print(student_data)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            # student_serializer.save()
            client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
            db = client.AWS
            coll = db.Student
            coll.insert_one( student_data)
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
''' 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        tutorial = Room.objects.get(pk=pk) 
    except Room.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    # GET all published tutorials
'''
# Get student with ID, edit student details with ID and delete student details with ID
@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    print(pk)
    pk=str(pk)
    if request.method == 'GET':
        try:
            client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
            db = client.AWS
            coll = db.Student
            student=coll.find_one({"univ_id":pk})
            print(student)
            student_serializer = StudentSerializer(student, many=False)
            print("after serial",student_serializer.data)
            return JsonResponse(student_serializer.data, safe=False)
        except Exception: 
            return JsonResponse({'message': 'Error occurred in finding room.'}, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        print(student_data)
        student_serializer = StudentSerializer(data=student_data)
        client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
        db = client.AWS
        coll = db.Student
        if student_serializer.is_valid():
            myquery = { "univ_id": pk }
            newvalues = { "$set": student_serializer.data }
            coll.update_one(myquery, newvalues)
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
            db = client.AWS
            coll = db.Student
            # Delete Document with univ_id
            result = coll.delete_one({"univ_id":pk})
            return JsonResponse("Data deleted successfully!", safe=False)
        except Exception:
            return JsonResponse("Error occurred!", status=status.HTTP_400_BAD_REQUEST)
