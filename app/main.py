from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    companies = [
        {"name": "Nvidia", "valuation": "$4.86T"},  
        {"name": "Microsoft", "valuation": "$4.04T"},  
        {"name": "Apple", "valuation": "$3.99T"},  
        {"name": "Alphabet", "valuation": "$2.58T"},  
        {"name": "Amazon", "valuation": "$2.44T"}  
    ]
    return templates.TemplateResponse("index.html", {"request": request, "companies": companies})
