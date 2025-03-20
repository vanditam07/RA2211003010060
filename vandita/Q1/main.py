from fastapi import FastAPI, HTTPException
from typing import List, Dict
import requests
import asyncio

app = FastAPI()

WINDOW_SIZE = 10
API_TIMEOUT = 0.5
API_URL = "http://20.244.56.144/test/{type}"

number_data: Dict[str, List[int]] = {}

NUMBER_TYPE_MAP = {"p": "primes", "f": "fibonacci", "e": "even", "r": "random"}

async def fetch_numbers(number_id: str) -> List[int]:
    if number_id not in NUMBER_TYPE_MAP:
        raise HTTPException(status_code=400, detail="Invalid number ID")
    url = API_URL.format(type=NUMBER_TYPE_MAP[number_id])
    try:
        response = await asyncio.to_thread(requests.get, url, timeout=API_TIMEOUT)
        response.raise_for_status()
        return response.json().get("numbers", [])
    except requests.exceptions.RequestException:
        return []

@app.get("/numbers/{number_id}")
async def calculate_average(number_id: str):
    if number_id not in NUMBER_TYPE_MAP:
        raise HTTPException(status_code=400, detail="Invalid number ID")
    prev_state = number_data.get(number_id, [])[:]
    new_numbers = await fetch_numbers(number_id)
    unique_numbers = [num for num in new_numbers if num not in prev_state]
    current_state = (prev_state + unique_numbers)[-WINDOW_SIZE:]
    number_data[number_id] = current_state
    avg = round(sum(current_state) / len(current_state), 2) if current_state else 0.0
    return {"windowPrevState": prev_state, "windowCurrState": current_state, "numbers": unique_numbers, "avg": avg}
