from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from . import utils
from .trigger import trigger 
import json
from .models import (
    user_model,
    customer_model,
    form_model,
    query_model,
    response_model
)
from . import MongoClient

# Create your views here.

# Create your views here.
def home(request):
    try:
        if request.method != "GET":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")
        
        return JsonResponse({"success":"true", "status":"online"})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

# User Views
@csrf_exempt 
def create_user(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["provider_name"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")
            
        if MongoClient.find_one({"type": "user", "provider-name": req_data['provider_name']}):
            return JsonResponse({"success":"false", "message": "User already exists."})

        user = user_model(provider_name=req_data['provider_name'])
        MongoClient.insert_one(user)
        
        return JsonResponse({"success":"true", "user": str(user)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt 
def create_customer(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["customer_name", "email", "ph_no", "location"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        if MongoClient.find_one({"type": "customer", "customer-name": req_data['customer_name'], "location": req_data['location'], "email": req_data['email'], "ph_no": req_data['ph_no']}):
            return JsonResponse({"success":"true", "message": "User already exists."})

        print(req_data)
        customer = customer_model(customer_name=req_data['customer_name'], location=req_data['location'], email=req_data['email'], ph_no=req_data['ph_no'])
        print(customer)
        MongoClient.insert_one(customer)
        
        return JsonResponse({"success":"true", "customer": str(customer)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})


@csrf_exempt
def create_form(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["user_id", "form_title"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        if MongoClient.find_one({"type": "form", "form-title": req_data['form_title'], "user-id": req_data['user_id']}):
            return JsonResponse({"success":"true", "message": "Form already exists."})

        form = form_model(user_id = req_data['user_id'], form_title = req_data['form_title'])
        MongoClient.insert_one(form)
        
        return JsonResponse({"success":"true", "form": str(form)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def get_forms(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["user_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        forms = list(MongoClient.find({"type": "form", "user-id": req_data['user_id']}))
        return JsonResponse({"success":"true", "forms": str(forms)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def get_form(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["form_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        form = MongoClient.find_one({"type": "form", "id": req_data['form_id']})
        
        return JsonResponse({"success":"true", "form": str(form)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def delete_forms(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["user_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        forms = MongoClient.delete_many({"type": "form", "user-id": req_data['user_id']})
        
        return JsonResponse({"success":"true", "forms": str(forms)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def delete_form(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["form_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        form = MongoClient.delete_one({"type": "form", "id": req_data['form_id']})
        queries = MongoClient.delete_many({"type": "query", "form-id": req_data['form_id']})
        
        return JsonResponse({"success":"true", "form": str(form)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def add_query(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["form_id", "query", "mandatory"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        if MongoClient.find_one({"type": "query", "form-id": req_data['form_id'], "query": req_data['query'], "mandatory": req_data['mandatory']}):
            return JsonResponse({"success":"true", "message": "Query already exists."})

        query = query_model(form_id = req_data['form_id'], query = req_data['query'], mandatory = req_data['mandatory'])
        MongoClient.insert_one(query)
        
        return JsonResponse({"success":"true", "query": str(query)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def delete_query(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        query = MongoClient.delete_one({"type": "query", "id": req_data['query_id']})
        responses = MongoClient.delete_many({"type": "response", "query-id": req_data['query_id']})

        return JsonResponse({"success":"true", "query": query})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def get_queries(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["form_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        queries = list(MongoClient.find({"type": "query", "form-id": req_data['form_id']}))
        
        return JsonResponse({"success":"true", "forms": str(queries)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def get_query(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        query = MongoClient.find_one({"type": "query", "id": req_data['query_id']})
        
        return JsonResponse({"success":"true", "form": str(query)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})

@csrf_exempt
def add_response(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query_id", "response", "customer_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        if MongoClient.find_one({"type": "response", "query-id": req_data['query_id'], "response": req_data['response'], "customer-id": req_data['customer_id']}):
            return JsonResponse({"success":"false", "message": "Response already exists."})

        response = response_model(query_id = req_data['query_id'], response = req_data['response'], customer_id = req_data['customer_id'])
        MongoClient.insert_one(response)

        try:
            if trigger(response["type"], response) == False:
                return JsonResponse({"success": "false", "message": "Interrupt External Pluggins"})
        except Exception as e:
            print("Warning: Triggering Failed")
        
        return JsonResponse({"success":"true", "response": str(response)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})
    
@csrf_exempt
def get_responses(request):
    try:
        if request.method != "POST":
            raise utils.CustomError(f"Method - {request.method} is not Allowed")

        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["query_id"]:
            if key not in req_data.keys():
                raise utils.CustomError(f"The parameter {key} is missing")

        responses = list(MongoClient.find({"type": "response", "query-id": req_data['query_id']}))
        
        return JsonResponse({"success":"true", "forms": str(responses)})
    
    except Exception as e:
        return JsonResponse({"success":"false", "message":f"{e}"})


