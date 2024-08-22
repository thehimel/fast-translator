# fast-translator

An AI powered translator built with FastAPI.

## Setup

* Clone the repository.
* Install the packages with `pip install -r requirements.txt`.

## Run the Server

* `fastapi dev src/main.py`
* `uvicorn src.main:app --host 127.0.0.1 --port 8080`

### Note

* The required models will be downloaded on the first execution.
  * Models to be downloaded: `pytorch_model.bin`. Location: `~/.cache/huggingface/hub/` 
* Therefore, the first API response will take some time.

## Resources

* API: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
