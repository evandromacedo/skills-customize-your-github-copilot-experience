from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List, Optional

app = FastAPI(title="Sistema de Biblioteca")

# TODO: Defina o modelo Pydantic para Book aqui

# TODO: Crie uma estrutura de dados para armazenar os livros

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API da Biblioteca!"}

# TODO: Implemente os endpoints necessários aqui
# GET /books
# GET /books/{book_id}
# POST /books
# PUT /books/{book_id}
# DELETE /books/{book_id}