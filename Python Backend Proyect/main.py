from fastapi import FastAPI
from credit_card import CreditCardRequest,CreditCardResponse
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime
"""

Prerequisites:
1. Install Python
2. Virtual Enviroments
3. Create Virtual env
4. Install dependencies fastAPI, pydantic 
5. Run uvicorn main:app --reload

Connect localhost too view docs :) : http://127.0.0.1:8000/docs

Algorithm

1. Create Custom clases for putRequest and Response using pydantic efficient for validation
2. Create API with FastAPI = (app = FastAPI)
3. Define Endpoint 'validate_credit_card'
4. Validate Credit Card: Return tuple (wasSucessful, Success/Error Message)
    4.1 Validate cvv
    4.2 Validate Date
    4.3 Validate with Luhm Algorithm
5. return response
"""

#NEW API
app = FastAPI()

"""
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
]
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

#Define Endpoint /validate_credit_card
@app.post('/validate_credit_card', response_model=CreditCardResponse)
def validateCreditCardRequest(credit_card: CreditCardRequest):


    # Validate credit_card here
    isValid, message = validate_credit_card(credit_card)
    
    #message = "SUCESS: Credit card is valid." if is_valid else "FAILURE: Credit card is invalid."

    return CreditCardResponse(valid=isValid, message=message)


def validate_credit_card(credit_card):

    # Validate CVV length
    # American Express are cards whose PAN (card numbers) starts with either “34” or “37”  
    if credit_card.card_number.startswith(('34', '37')):    
        if len(credit_card.cvv) != 4:
            return False, "FAILURE: CV Lenght"
    #The CVV (security code) of the credit card must be exactly 3 digits long
    elif len(credit_card.cvv) != 3:
        return False, "FAILURE: CV Lenght"
    

    # Validate expiry date
    now = datetime.now()
    current_year, current_month = now.year-2000, now.month
    expiry_month, expiry_year = map(int, credit_card.expiration_date.split('/'))
    if expiry_year < current_year or (expiry_year == current_year and expiry_month < current_month) or expiry_month > 12 or expiry_year > 99:
        return False, "FAILURE: Invalid Expirity Date"

  
    # Validate PAN using Luhn's algorithm
    if not luhnValidate(credit_card.card_number):
        return False, "FAILURE: Lun Algorithm"

   
    return True, "SUCESS: Credit card is valid."




def luhnValidate(card_number) :
    digits = list(map(int, card_number))
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]

    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(divmod(digit * 2, 10))

    return total % 10 == 0
"""
def lunValidate2(card_number):

    digits = []

    for digit in card_number:

    int nDigits = cardNo.length();
 
    int nSum = 0, isSecond = false;
    for (int i = nDigits - 1; i >= 0; i--) {
 
        int d = cardNo[i] - '0';
 
        if (isSecond == true)
            d = d * 2;
 
        // We add two digits to handle
        // cases that make two digits after
        // doubling
        nSum += d / 10;
        nSum += d % 10;
 
        isSecond = !isSecond;
        """
