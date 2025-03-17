# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer

# # Charger le modèle d'embeddings
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # Charger les documents
# with open("data/cfptsj_data.txt", "r", encoding="utf-8") as f:
#     documents = f.readlines()

# # Convertir en embeddings
# embeddings = np.array([model.encode(doc.strip()) for doc in documents if doc.strip()])

# # Création de l'index FAISS
# dimension = embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(embeddings)

# # Sauvegarde de l'index
# faiss.write_index(index, "models/cfptsj_index.faiss")
# print(" Index FAISS créé !")

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Charger le modèle d'embeddings multilingue amélioré
model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")

# Charger les documents scrapés
with open("data/cfptsj_data.txt", "r", encoding="utf-8") as f:
    raw_documents = [doc.strip() for doc in f.readlines() if doc.strip()]

# Découpage des documents en chunks avec recouvrement
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=256,
    chunk_overlap=20,
    separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]
)

# Appliquer la segmentation
documents = []
for doc in raw_documents:
    chunks = text_splitter.split_text(doc)
    documents.extend(chunks)

print(f"Nombre de chunks après segmentation: {len(documents)}")

# Filtrer les chunks trop courts
documents = [doc for doc in documents if len(doc) > 10]
print(f"Nombre de chunks après filtrage: {len(documents)}")

# Convertir en embeddings
embeddings = np.array([model.encode(doc) for doc in documents])

# Création de l'index FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Sauvegarde de l'index
faiss.write_index(index, "models/cfptsj_index.faiss")

print("Index FAISS optimisé créé avec succès!")
print(f"Caractéristiques:")
print(f"- Modèle d'embedding: paraphrase-multilingual-mpnet-base-v2")
print(f"- Nombre de chunks indexés: {len(documents)}")
print(f"- Taille des embeddings: {dimension} dimensions")