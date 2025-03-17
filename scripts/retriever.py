import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Charger le modèle multilingue
model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")

# Charger les documents avec filtrage intelligent
with open("data/cfptsj_data.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

# Filtrage basé sur le nombre de mots (évite de supprimer les contacts)
documents = [doc for doc in documents if len(doc.split()) >= 3]
print(f"Documents indexés : {len(documents)}")

# Conversion en embeddings
embeddings = np.array([model.encode(doc) for doc in documents])

# Création de l'index FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def retrieve_docs(query, top_k=5):
    """Récupère les documents avec un score de similarité normalisé."""
    if not query.strip():
        raise ValueError("Erreur : Requête vide.")
    
    query_embedding = model.encode(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    
    # Convertir les distances en similarités (0 à 1)
    similarity_scores = 1 / (1 + distances)
    
    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(documents):
            doc = documents[idx]
            similarity = similarity_scores[0][i]
            results.append(f"[Similarité: {similarity:.2f}] {doc}")
    
    return results

# Tests complets
if __name__ == "__main__":
    test_queries = [
        ("Adresse du CFPTSJ ?", 3),
        ("Directeur du centre", 2),
        ("Formations disponibles en 2024", 5)
    ]
    
    for query, k in test_queries:
        print(f"\nRequête: '{query}'")
        try:
            results = retrieve_docs(query, top_k=k)
            for res in results:
                print(f"- {res}")
        except Exception as e:
            print(f"Erreur : {str(e)}")