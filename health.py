import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    logger.info("health check")
    return {"status": "ok"}
