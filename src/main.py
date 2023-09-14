from fastapi import FastAPI, Depends
from .schemas import CurrencyResponse
from fastapi import Query
from fastapi import HTTPException
from typing import Annotated
from .setting import API_KEY
import requests

app = FastAPI(docs_url="/api", redoc_url=None)


@app.get("/api/rates")
def create(
    from_: Annotated[str, Query(alias="from")], to: str, value: float
) -> CurrencyResponse:
    url = "https://api.freecurrencyapi.com/v1/latest"
    headers = {"apikey": API_KEY}
    params = {"base_currency": from_, "currencies": [to]}
    response = requests.get(url, headers=headers, params=params)
    if not response.ok:
        details = response.json()
        details.pop("info")
        raise HTTPException(status_code=response.status_code, detail=details)
    return {"result": response.json()["data"][to] * value}
