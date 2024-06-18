from fastapi import FastAPI, HTTPException, Query
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

from src.utils import translator

app = FastAPI()


class TranslateRequest(BaseModel):
    text: str
    source: str = "deu_Latn"
    target: str = "ben_Beng"


class TranslateResponse(BaseModel):
    text: str


@app.get("/api/", response_model=TranslateResponse)
async def translate(text: str = Query(...), source: str = "deu_Latn", target: str = "ben_Beng"):
    if not text:
        raise HTTPException(status_code=400, detail="The text parameter is missing.")

    translation = await translator(text, source, target)
    return {"text": translation}


# Generate OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Translation API",
        version="1.0.0",
        description="Translate text using a transformer model.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi
