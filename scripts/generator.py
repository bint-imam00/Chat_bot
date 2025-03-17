
import google.generativeai as genai

# Configurer l'API Gemini directement avec votre clé
genai.configure(api_key="AIzaSyBY6qGnpjt9fpixiZgh_m7ht_QsRUvPKg4")

def generate_response(query, context_docs):
    """Génère une réponse à partir du contexte et de la requête"""
    
    prompt = f"""
Tu es un assistant virtuel pour le Centre de Formation Professionnelle et Technique Sénégal-Japon (CFPTSJ).
Réponds à la question en utilisant uniquement les informations fournies dans le contexte ci-dessous.
Si les informations ne sont pas suffisantes pour répondre à la question, indique clairement 
que tu n'as pas assez d'informations spécifiques sur ce sujet dans ta base de connaissances.

Contexte:
{' '.join([doc.split('] ', 1)[1] if '] ' in doc else doc for doc in context_docs])}

Question: {query}

Réponse:
"""
    
    try:
        # Utiliser spécifiquement un modèle Gemini 1.5
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erreur lors de la génération de la réponse: {str(e)}"

# Exemple d'utilisation
if __name__ == "__main__":
    from retriever import retrieve_docs
    
    query = "Quelles sont les frais de depot de dossier au CFPT Sénégal-Japon ?"
    context = retrieve_docs(query, top_k=5)
    print(f"Contexte récupéré: {context}")
    response = generate_response(query, context)
    print(f"Réponse: {response}")