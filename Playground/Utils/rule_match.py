from . import MongoClient

def rule_match(income_query_id, savings_query_id):
    # income of a person cannot be less than savings 
    customer_ids = list()
    responses = list(MongoClient.find({"type":"response", "query-id": income_query_id}))
    for response in responses:
        if response["customer-id"] not in customer_ids:
            customer_ids.append(response["customer-id"])
    responses = list(MongoClient.find({"type":"response", "query-id": savings_query_id}))
    for response in responses:
        if response["customer-id"] not in customer_ids:
            customer_ids.append(response["customer-id"])

    for customer_id in customer_ids:
        responses = list(MongoClient.find({"type": "response", "query-id": income_query_id, "customer-id": customer_id}))
        if len(responses) > 0:
            income = responses[0]["response"]
            responses = list(MongoClient.find({"type": "response", "query-id": savings_query_id, "customer-id": customer_id}))
            if len(responses) > 0:
                savings = responses[0]["response"]

                if savings >= income:
                    print(f"Invalid Data Entries: Customer Id {customer_id}")

# rule_match("bfd8bd7a-cf74-4109-b90c-bb6a5da6fb33", "215c8d8a-c889-4c1a-82ef-6acf73ee57d7")
    
        



        

    
