

def word_finder(responses, word):
    target_customers = list()
    for response in responses:
        if word in response["response"].split():
            target_customers.append(response["customer-id"])
    if len(target_customers) > 0:
        return (
            False, target_customers
        )
    return True, target_customers