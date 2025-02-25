from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de datos
class Mascota(BaseModel):
    id: int
    nombre: str
    edad: int
    raza: str
    dueno: str

# Lista para almacenar mascotas
mascotas: List[Mascota] = []

# Crear una mascota
@app.post("/mascotas/", response_model=Mascota)
def crear_mascota(mascota: Mascota):
    mascotas.append(mascota)
    return mascota

# Listar todas las mascotas
@app.get("/mascotas/", response_model=List[Mascota])
def listar_mascotas():
    return mascotas

# Obtener una mascota por ID
@app.get("/mascotas/{mascota_id}", response_model=Mascota)
def obtener_mascota(mascota_id: int):
    for mascota in mascotas:
        if mascota.id == mascota_id:
            return mascota
    raise HTTPException(status_code=404, detail="Mascota no encontrada")

# Modificar una mascota
@app.put("/mascotas/{mascota_id}", response_model=Mascota)
def modificar_mascota(mascota_id: int, mascota_actualizada: Mascota):
    for i, mascota in enumerate(mascotas):
        if mascota.id == mascota_id:
            mascotas[i] = mascota_actualizada
            return mascota_actualizada
    raise HTTPException(status_code=404, detail="Mascota no encontrada")

# Eliminar una mascota
@app.delete("/mascotas/{mascota_id}")
def eliminar_mascota(mascota_id: int):
    for i, mascota in enumerate(mascotas):
        if mascota.id == mascota_id:
            del mascotas[i]
            return {"message": "Mascota eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Mascota no encontrada")

# Para ejecutar el servidor, usa el siguiente comando en la terminal:
# uvicorn main:app --reload
