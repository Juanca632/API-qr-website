from typing import List
from fastapi import FastAPI, status
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import json
import math

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get(
    path="/fr",
    # response_model=List[Chart],
    status_code=status.HTTP_200_OK,
    summary="Questionnaire",
    tags=["Questionnaire"]
)
def home():
    with open('links-fr.json') as f:
        data = json.load(f)
    return data
@app.get(
    path="/en",
    # response_model=List[Chart],
    status_code=status.HTTP_200_OK,
    summary="Questionnaire",
    tags=["Questionnaire"]
)
def home():
    with open('links-en.json') as f:
        data = json.load(f)
    return data


def find_key_recursive(data, path):
    """
    Busca una ruta específica en un diccionario anidado de forma recursiva.

    :param data: El diccionario en el que buscar.
    :param path: La ruta que se desea buscar, separada por '-'.
    :return: El valor asociado a la ruta, o None si la ruta no se encuentra.
    """
    keys = path.strip("|").split("|")  # Obtener las claves de la ruta

    current = data
    for key in keys:
        if key in current:
            current = current[key]
        else:
            return None
    
    return current

@app.get(
    path="/en/{id}",
    status_code=status.HTTP_200_OK,
    summary="Get by ID",
    tags=["ID"]
)
def get_by_id(id: str):
    with open('links-en.json') as f:
        data = json.load(f)
        obj = find_key_recursive(data, id)
    return obj

@app.get(
    path="/fr/{id}",
    status_code=status.HTTP_200_OK,
    summary="Get by ID",
    tags=["ID"]
)
def get_by_id(id: str):
    with open('links-fr.json') as f:
        data = json.load(f)
        obj = find_key_recursive(data, id)
    return obj