from fastapi import FastAPI

app = FastAPI()


@app.get("/orders/{order_id}")
def get_order(order_id):
    print("fetching order", order_id)
    return {"id": order_id, "status": "shipped"}
