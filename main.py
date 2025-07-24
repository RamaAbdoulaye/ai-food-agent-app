from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import traceback


# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Récupérer la clé OpenAI depuis la variable d'environnement
OPENAI_API_KEY = os.environ.get("OpenAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "La clé OpenAI_API_KEY n'a pas été trouvée dans les variables d'environnement")

client = OpenAI(api_key=OPENAI_API_KEY)


def load_food_data():
    with open("data/food_data.json", encoding="utf-8") as f:
        return json.load(f)


prompts_suggeres = [
    "Quels plats contiennent du poulet ?",
    "Avez-vous des options végétariennes ?",
    "Quels sont les plats les plus populaires ?",
    "Y a-t-il des plats sans gluten ?"
]


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prompts": prompts_suggeres})


@app.post("/ask")
async def ask_agent(prompt: str = Form(...)):
    food_data = load_food_data()

    system_prompt = f"""
Tu es un assistant IA spécialisé en restauration. Voici les plats disponibles dans la base de données :
{json.dumps(food_data, ensure_ascii=False, indent=2)}

Réponds aux questions des utilisateurs en te basant uniquement sur ces données.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        answer = response.choices[0].message.content.strip()
        return JSONResponse({"answer": answer})

    except Exception as e:
        traceback.print_exc()  # This will print the full error in the console
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/foods")
async def get_foods():
    return load_food_data()
