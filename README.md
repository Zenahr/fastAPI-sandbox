# Readme

run the api

```bash
uvicorn main:api --reload
```
translated this means: uivcorn take the api object (which is just an instance of fastAPI) from a file named main.py

see the raw api schema
(while the server is running)
```http://127.0.0.1:8000/openapi.json```