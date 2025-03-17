from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from scripts.retriever import retrieve_docs
from scripts.generator import generate_response

# Initialisation de FastAPI
app = FastAPI(title="Chatbot CFPTSJ", description="Chatbot basé sur Gemini 1.5 et FAISS")

# Configuration des templates (affichage HTML)
templates = Jinja2Templates(directory="templates")

class QueryRequest(BaseModel):
    query: str

# Route pour afficher la page HTML
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route API pour la requête AJAX
@app.post("/chat")
async def chat(request: QueryRequest):
    """Récupère la question de l'utilisateur et génère une réponse"""
    context = retrieve_docs(request.query, top_k=5)
    response = generate_response(request.query, context)
    return JSONResponse(content={"question": request.query, "response": response})

# Route pour soumettre via formulaire HTML
@app.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, query: str = Form(...)):
    context = retrieve_docs(query, top_k=5)
    response = generate_response(query, context)
    return templates.TemplateResponse("index.html", {"request": request, "query": query, "response": response})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
