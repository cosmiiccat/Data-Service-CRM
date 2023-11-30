from . import MongoClient

def word_finder(form_id, target_word, filter, filter_val):

    queries = list(MongoClient.find({"type": "query", "form-id": form_id}))
    customer_ids = list()
    for query in queries:
        responses = MongoClient.find({"type": "response", "query-id": query["id"]})
        for response in responses:
            if response["customer-id"] not in customer_ids:
                customer_ids.append(response["customer-id"])
    for customer_id in customer_ids:
        for query in queries:
            customer = MongoClient.find_one({"type": "customer", "id": customer_id})
            if customer[filter] == filter_val:
                responses = list(MongoClient.find({"type": "response", "customer-id": customer_id, "query-id": query["id"]}))
                if len(responses) > 0:
                    words = responses[0]["response"].split()
                    if target_word in words:
                        print(f"Offensive Data Entries: Customer Id {customer_id}")

# word_finder("3abe191c-aedd-4b79-9378-e4fca037492b", "Faltu", "location", "Kolkata")