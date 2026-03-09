from fastapi import FastAPI

app = FastAPI(title="FruitsAPI")

FRUITS = {
    1: {"name": "Apple", "price": 1.20, "in_season": True},
    2: {"name": "Banana", "price": 0.80, "in_season": True},
    3: {"name": "Orange", "price": 1.00, "in_season": False},
}

_next_id = 4

@app.get("/health")
def root():
    return {"status": "ok"}

@app.get("/fruits")
def list_fruits():
    return [
        {"id": id_, **data}
        for id_, data in FRUITS.items()
    ]

@app.get("/fruits/{fruit_id:int}")
def get_fruit(fruit_id: int):
    return {"id": fruit_id, **FRUITS[fruit_id]}