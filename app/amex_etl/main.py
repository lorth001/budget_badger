import api_request as amex


transactions = amex.get_transactions()

for transaction in transactions:
    name = transaction['first_name']
    amount = transaction['amount']
    date = transaction['charge_date']

    # handles statement payments and fees, which don't contain merchant details
    if transaction['sub_type'] != 'PURCHASE':
        merchant_name = 'AMEX'
        merchant_id = 'AMEX'
        category_name = 'Payment'
    else:
        merchant_name = transaction['extended_details']['merchant']['name']
        merchant_id = transaction['extended_details']['merchant']['identifier']
        category_name = transaction['extended_details']['category']['category_name']

    data = (
        name,
        amount, 
        date,
        category_name,
        merchant_name, 
        merchant_id
    )

    print(data)
