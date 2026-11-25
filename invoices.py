import logging

from fastapi import FastAPI

app = FastAPI()
logger = logging.getLogger(__name__)


@app.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: str) -> dict:
    logger.info("loading invoice %s", invoice_id)
    return {"data": {"id": invoice_id}}
