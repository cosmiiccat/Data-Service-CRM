import uuid
from django.db import models
from . import MongoClient
from datetime import datetime

# Create your models here.

def user_model(provider_name):
    user = {
            'id': str(uuid.uuid4()),
            'type': 'user',
            'provider-name': provider_name,
            'createdAt': datetime.utcnow().isoformat(),  
            'updatedAt': datetime.utcnow().isoformat(),  
        }
    return (
        user
    )

def customer_model(customer_name, location, email, ph_no):
    customer = {
            'id': str(uuid.uuid4()),
            'type': 'customer',
            'customer-name': customer_name,
            'location': location,
            'email': email,
            'ph-no': ph_no,
            'createdAt': datetime.utcnow().isoformat(),  
            'updatedAt': datetime.utcnow().isoformat(),  
        }
    
    print(customer)
    return (
        customer
    )

def form_model(form_title, user_id):
    form = {
            'id': str(uuid.uuid4()),
            'type': 'form',
            'form-title': form_title,
            'user-id': user_id,
            'createdAt': datetime.utcnow().isoformat(),  
            'updatedAt': datetime.utcnow().isoformat(),  
        }
    return (
        form
    )

def query_model(query, form_id, mandatory):
    query = {
            'id': str(uuid.uuid4()),
            'type': 'query',
            'form-id': form_id,
            'query': query,
            'mandatory': mandatory,
            'createdAt': datetime.utcnow().isoformat(),  
            'updatedAt': datetime.utcnow().isoformat(),  
        }
    return (
        query
    )

def response_model(response, query_id, customer_id):
    response = {
            'id': str(uuid.uuid4()),
            'type': 'query',
            'query-id': query_id,
            'customer-id': customer_id,
            'response': response,
            'createdAt': datetime.utcnow().isoformat(),  
            'updatedAt': datetime.utcnow().isoformat(),  
        }
    return (
        response
    )