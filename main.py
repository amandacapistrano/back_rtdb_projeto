from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict
import random
from datetime import datetime
import requests
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API de recomendação de músicas funcionando! 🎶"}


# Modelo de entrada para criação de usuário
class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    genero: str

# Modelo para musica recomendada
class MusicaRecomendada(BaseModel):
    titulo: str
    artista: str
    link: str
    preview: str

# Modelo para usuário completo com recomendação
class Usuario(BaseModel):
    id: str
    nome: str
    email: str
    genero: str
    criado_em: Optional[str]
    musica_recomendada: Optional[MusicaRecomendada]

# Mapeamento dos gêneros
generos_deezer = {
    "Todos": 0,
    "Pop": 132,
    "Sertanejo": 80,
    "MPB": 78,
    "Rap/Funk Brasileiro": 472,
    "Rap/Hip Hop": 116,
    "Reggaeton": 122,
    "Rock": 152,
    "Dance": 113,
    "R&B": 165,
    "Alternativo": 85,
    "Samba/Pagode": 79,
    "Electro": 106,
    "Música Religiosa": 186,
    "Axé/Forró": 76,
}

FIREBASE_URL = "https://aula-b7426-default-rtdb.firebaseio.com/users.json"


class FirebaseRTDB:
    def __init__(self, url):
        self.url = url

    def criar_usuario(self, data: dict):
        try:
            response = requests.post(self.url, json=data)
            response.raise_for_status()
            return response.json()  # Retorna {'name': 'firebase_id'}
        except Exception as e:
            print(f"Erro ao criar usuário no Firebase: {e}")
            return None

    def listar_usuarios(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            dados = response.json()
            if dados:
                usuarios = [{"id": k, **v} for k, v in dados.items()]
                return usuarios
            return []
        except Exception as e:
            print(f"Erro ao listar usuários no Firebase: {e}")
            return []


class DeezerAPI:
    BASE_URL = "https://api.deezer.com"

    def buscar_artistas_por_genero(self, genero_id):
        try:
            url = f"{self.BASE_URL}/genre/{genero_id}/artists"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("data", [])
        except Exception as e:
            print(f"Erro Deezer artistas: {e}")
            return []

    def buscar_top_musica_por_artista(self, artist_id):
        try:
            url = f"{self.BASE_URL}/artist/{artist_id}/top?limit=1"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get("data"):
                return data["data"][0]
            return None
        except Exception as e:
            print(f"Erro Deezer música top: {e}")
            return None


firebase = FirebaseRTDB(FIREBASE_URL)
deezer = DeezerAPI()


@app.post("/criar_usuario", response_model=Dict[str, str])
def criar_usuario(usuario: UsuarioCreate):
    genero_id = generos_deezer.get(usuario.genero)
    if not genero_id:
        raise HTTPException(status_code=400, detail="Gênero inválido")

    artistas = deezer.buscar_artistas_por_genero(genero_id)
    if not artistas:
        raise HTTPException(status_code=404, detail="Nenhum artista encontrado para esse gênero")

    artista_escolhido = random.choice(artistas)
    musica = deezer.buscar_top_musica_por_artista(artista_escolhido["id"])

    musica_recomendada = None
    if musica:
        musica_recomendada = {
            "titulo": musica["title"],
            "artista": artista_escolhido["name"],
            "link": musica["link"],
            "preview": musica["preview"],
        }

    data = {
        "nome": usuario.nome,
        "email": usuario.email,
        "genero": usuario.genero,
        "musica_recomendada": musica_recomendada,
        "criado_em": datetime.now().isoformat(),
    }

    resultado = firebase.criar_usuario(data)
    if not resultado:
        raise HTTPException(status_code=500, detail="Erro ao criar usuário no Firebase")

    return resultado  


@app.get("/listar_usuarios", response_model=List[Usuario])
def listar_usuarios():
    usuarios = firebase.listar_usuarios()
    return usuarios
