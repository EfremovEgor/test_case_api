from pydantic import BaseModel


class CurrencyResponse(BaseModel):
    result: float
