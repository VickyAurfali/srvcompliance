from fastapi import FastAPI, Request
import json
import datetime

app = FastAPI()

@app.post("/collect_data")
async def collect_data(request: Request):
    data = await request.json()
    ip_address = request.client.host
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"{ip_address}_{date_str}.json"
    
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=4)
    
    return {"message": "Data received and stored"}

@app.get("/get_data")
def get_data():
    import glob
    data_files = glob.glob("*.json")
    data = []
    for file in data_files:
        with open(file, 'r') as f:
            data.append(json.load(f))
    return data

@app.get("/")
def read_root():
    return {"message": "Welcome to the System Info API! Use /collect_data to send system info and /get_data to retrieve collected data."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)