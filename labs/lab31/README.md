# Lab 31: API Gateway / Reverse Proxy with Nginx

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab31
cd ~/python/labs/lab31
```

---

## Step 2: Setup FastAPI App

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Create **requirements.txt**:

```bash
cat >> requirements.txt << EOF
fastapi
uvicorn
EOF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 3: Create FastAPI App `main.py`

```bash
cat >> main.py << EOF
from fastapi import FastAPI

app = FastAPI(title="FastAPI with Nginx Gateway")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@app.get("/service")
def service():
    return {"message": "This is the service endpoint"}
EOF
```

Run two instances on **different ports**:

```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload &
uvicorn main:app --host 0.0.0.0 --port 8002 --reload &
```

---

## Step 4: Install Nginx

```bash
sudo apt update
sudo apt install -y nginx
```

---

## Step 5: Configure Nginx as Reverse Proxy

```bash
sudo tee /etc/nginx/sites-available/fastapi_gateway << EOF
upstream fastapi_app {
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
}

server {
    listen 80;

    location / {
        proxy_pass http://fastapi_app;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF
```

Enable the config:

```bash
sudo ln -s /etc/nginx/sites-available/fastapi_gateway /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## Step 6: Test API Gateway

### Send request via Nginx (port 80):

```bash
curl http://127.0.0.1/
```

**Expected Response:**

```json
{"message":"Hello from FastAPI"}
```

### Test load balancing

Make multiple requests:

```bash
for i in {1..5}; do curl -s http://127.0.0.1/service; echo; done
```

Responses will be served alternately by the **two FastAPI instances** (round-robin).

---

## Step 7: Key Learning Points

* **Nginx upstream block** = backend pool for load balancing.
* Requests are **proxied to FastAPI** via `proxy_pass`.
* Can add **SSL, caching, rate limiting, authentication** in Nginx.
* This setup mimics a **basic API Gateway** architecture.
