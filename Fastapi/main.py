from turtle import title
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Mi primera fastAPI",
          description="FastApi con un crud",
          version="1.2.3")

informacion = []

class personas(BaseModel):
    nombre: str
    apellido: str
    celular: int
    correo: str

@app.get('/informacion todos')
async def get_informaicondetodos():
    return informacion

@app.get('/consultar/{nombre}')
async def get_informaicon(nombre: str):
    for infor in informacion:
        if infor ["nombre"] == nombre:
          return infor
    return "No existe esta persona"

@app.post("/añadir")
async def guardar_datos(datos: personas):
    informacion.append(datos.dict())
    return "Persona registrada"

@app.put("/actualizar/{nombre}")
async def actualizar_persona(actualizado: personas, nombre:str):
     for infor in informacion:
        if infor ["nombre"] == nombre:
           infor ["nombre"] = actualizado.nombre
           infor ["apellido"] = actualizado.apellido
           infor ["celular"] = actualizado.celular
           infor ["correo"] = actualizado.correo
           return "datos actualizados"
     return "No existe esta persona"

@app.delete("/eliminar/{nombre}")
async def eliminar_persona(nombre: str):
    for infor in informacion:
        if infor ["nombre"] == nombre:
          informacion.remove(infor)
          return "Persona eliminada"
    return "No existe esta persona"