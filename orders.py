import logging

from fastapi import FastAPI

app = FastAPI()
logger = logging.getLogger(__name__)


@app.get("/orders/{order_id}")
def get_order(order_id: str) -> dict:
    logger.info("fetching order %s", order_id)
    return {"data": {"id": order_id, "status": "shipped"}}
