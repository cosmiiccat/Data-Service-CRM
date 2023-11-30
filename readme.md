# Data Collection Platform Backend README

## Overview
Welcome to the backend of our data collection platform, a robust system used by customers in 50+ countries, powering data collection for over 11 million responses. This platform facilitates critical activities, ranging from governments delivering vaccines to small business owners managing daily inventory.

## Tech Stack
- Python
- MongoDB
- Django
- Google Sheets API
- Twilio
- Docker 
- Kubernetes

## Problem Statement
The lifecycle of data collection doesn't end with the submission of a response. Post-submission business logic is often required, such as searching for slangs in local languages, validating responses against business rules, integrating with Google Sheets, sending SMS notifications, and more. The goal is to create a flexible system that supports various post-submission actions in a plug-n-play fashion.

## Routes
- **/**: Check if the server is online.
- **/create_user/**: Create a new user.
- **/create_customer/**: Create a new customer.
- **/create_form/**: Create a new form.
- **/get_form/**: Get details of a specific form.
- **/get_forms/**: Get all forms for a user.
- **/delete_form/**: Delete a specific form.
- **/delete_forms/**: Delete all forms for a user.
- **/add_query/**: Add a query to a form.
- **/add_response/**: Add a response to a query.
- **/get_query/**: Get details of a specific query.
- **/get_queries/**: Get all queries for a form.

## Models
### User Model
- **Endpoint:** /create_user/
- **Parameters:** provider_name
- **Example Usage:**
```
{
  "provider_name": "example_provider"
} 
```


## Customer Model
- **Endpoint:** /create_customer/
- **Parameters:** customer_name, email, ph_no, location
- **Example Usage:**
```
{
  "customer_name": "John Doe",
  "email": "john@example.com",
  "ph_no": "1234567890",
  "location": "City"
}
```

## Form Model
- **Endpoint:** /create_form/
- **Parameters:** user_id, form_title
- **Example Usage:**
```
{
  "user_id": "user123",
  "form_title": "Example Form"
}
```


## Query Model
- **Endpoint:** /add_query/
- **Parameters:** form_id, query, mandatory
- **Example Usage:**
```
{
  "form_id": "form123",
  "query": "Example Query",
  "mandatory": true
}
```


## Response Model
- **Endpoint:** /add_response/
- **Parameters:** query_id, response, customer_id
- **Example Usage:**
```
{
  "query_id": "query123",
  "response": "Example Response",
  "customer_id": "customer123"
}
```

## Views
- **home:** Check server status.
- **create_user:** Create a new user.
- **create_customer:** Create a new customer.
- **create_form:** Create a new form.
- **get_forms:** Get all forms for a user.
- **get_form:** Get details of a specific form.
- **delete_forms:** Delete all forms for a user.
- **delete_form:** Delete a specific form.
- **add_query:** Add a query to a form.
- **get_queries:** Get all queries for a form.
- **get_query:** Get details of a specific query.
- **add_response:** Add a response to a query.
- **get_responses:** Get all responses for a query.

## Models
Models define the data structure for user, customer, form, query, and response.

- **User Model:** `user_model(provider_name)`
- **Customer Model:** `customer_model(customer_name, location, email, ph_no)`
- **Form Model:** `form_model(form_title, user_id)`
- **Query Model:** `query_model(query, form_id, mandatory)`
- **Response Model:** `response_model(response, query_id, customer_id)`

## Google Sheets Integration
We have integrated with Google Sheets to export data. The functionalities include:

- **interact_sheet(form_id):** Update a Google Sheet with form responses.

## Business Rules Validation
We perform rule matching for specific queries, such as validating that income should not be less than savings. The function `rule_match` identifies invalid data entries.

## SMS Notifications
SMS notifications are sent using the Twilio API. The function `sms_message` sends a custom message to a specified customer number, and `sms_confirmation` sends a confirmation message for a received response.

## Offensive Word Detection
The function `word_finder` detects offensive words in responses based on specified criteria.

# Main Features 

## Plug in and No OverHaul on the Backend
Each utility functionalities are separately moduled and stored in a different Django App. 
If they are **post database store functionalities**, they can directly talk to the database.
If they are **pre database store functionalities**, they can be triggered using a trigger function without bothering the main backend architecture. Here, they can act as a interrupt to the core backend, however exception handling done for any errors.

## Free Flow and Exception Handling 
Exception handling is being done for all the external methods being called, so that no other external service interupts the main backend server.

## No Version mismatch and installation headache 
Entire application is containarized and docker image is being built to run the server without taking the headache of version mismatch.

## Async Operations creates no overhaul on Backend 
RabbitMQ used to handle async operations to negate the overhaul and latency on backend. (in progress/ to be done)

## Scalability, No Downtime, Multiple Server image management, Low overhead etc 
Handled by Kubernetes (in progress/ to be done)

## Checking System Health 
There are cloud provider tools like Azure monitor for Benchmarking.

# Further Improvement 

## Cloud Deployment 
Can be Deployed in Microsoft Azure and scale as much as we want alocating suitable resources to all the worker nodes. 

## Shift from Mongodb to Cosmosdb 
This would ensure that a partitioning scheme is used such as User level partitioning, which ensures faster Crud operations.
