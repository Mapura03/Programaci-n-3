from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data model
class Pet(BaseModel):
    id: int
    name: str
    age: int
    breed: str
    owner: str

# List to store pets
pets: List[Pet] = []

# Create a pet
@app.post("/pets/", response_model=Pet)
def create_pet(pet: Pet):
    pets.append(pet)
    return pet

# List all pets
@app.get("/pets/", response_model=List[Pet])
def list_pets():
    return pets

# Get a pet by ID
@app.get("/pets/{pet_id}", response_model=Pet)
def get_pet(pet_id: int):
    for pet in pets:
        if pet.id == pet_id:
            return pet
    raise HTTPException(status_code=404, detail="Pet not found")

# Update a pet
@app.put("/pets/{pet_id}", response_model=Pet)
def update_pet(pet_id: int, updated_pet: Pet):
    for i, pet in enumerate(pets):
        if pet.id == pet_id:
            pets[i] = updated_pet
            return updated_pet
    raise HTTPException(status_code=404, detail="Pet not found")

# Delete a pet
@app.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
    for i, pet in enumerate(pets):
        if pet.id == pet_id:
            del pets[i]
            return {"message": "Pet successfully deleted"}
    raise HTTPException(status_code=404, detail="Pet not found")

# To run the server, use the following command in the terminal:
# uvicorn main:app --reload