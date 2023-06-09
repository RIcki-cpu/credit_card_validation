
from pydantic import BaseModel,Field

class CreditCardRequest(BaseModel):

    # 3. The PAN (card number) is between 16 and 19 digits long
    card_number: str = Field(..., min_length=16, max_length=19)
    expiration_date: str = Field(..., regex=r"\d{2}/\d{2}")
    cvv: str = Field(..., min_length=3, max_length=4)

from pydantic import BaseModel

class CreditCardResponse(BaseModel):
    valid: bool
    message: str
