from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
import openai
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load food data from JSON


def load_food_data():
    with open("data/food_data.json") as f:
        return json.load(f)

# Endpoint: Serve the main HTML page


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    common_prompts = [
        "Quels plats contiennent du poulet ?",
        "Avez-vous des options végétariennes ?",
        "Quels sont les plats les plus populaires ?",
        "Y a-t-il des plats sans gluten ?"
    ]

    return templates.TemplateResponse("index.html", {"request": request, "prompts": common_prompts})

# Endpoint: Handle user query and return AI response


@app.post("/ask")
async def ask_agent(prompt: str = Form(...)):
    food_data = load_food_data()

    # This would be a call to GPT-4.1 with food_data context
    # Example placeholder logic
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a helpful food assistant. Use only the food data provided."},
            {"role": "user",
                "content": f"Here is the menu data: {json.dumps(food_data)}.\nUser: {prompt}"}
        ]
    )

    answer = response.choices[0].message.content
    return JSONResponse({"answer": answer})

# Endpoint: Fetch food data (optional)


@app.get("/foods")
async def get_foods():
    data = load_food_data()
    return JSONResponse(content=data)
