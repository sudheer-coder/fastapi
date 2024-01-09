from datetime import date
from typing import Optional, List

from pydantic import BaseModel, EmailStr


class insurance_create(BaseModel):
    policy_holder_id: int
    policy_holder_name: Optional[str]=None
    city: Optional[str]=None
    country: Optional[str]=None
    start_date: Optional[date]=None
    coverage_amount: Optional[int]=None
    user_id: int

class UserCreate(BaseModel):
    first_name : Optional[str]=None
    last_name : Optional[str]=None
    phone_number : Optional[str]=None
    email: Optional[EmailStr] = None
class userGet(UserCreate):
    insurances: List[insurance_create] = []
