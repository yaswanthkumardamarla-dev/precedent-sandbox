from fastapi import FastAPI

app = FastAPI()


@app.get("/invoices/{invoice_id}")
def get_invoice(invoice_id):
    print("loading invoice", invoice_id)
    return {"data": {"id": invoice_id}}
