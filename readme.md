
# Simple Fastapi planning app

# via Docker
```
docker build . --tag fastapi
docker run -p 80:80 fastapi
```

# To see docs

http://localhost:80/docs

# via CLI
Run: 
```
py -m venv venv
.\venv\scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```