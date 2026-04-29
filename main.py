from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Contact(BaseModel):
    name: str
    phone_number: str

contacts = {}

@app.get("/")
def home():
    contact_options = "Add, View, Search, Update, Delete"
    return f"contact options: {contact_options}"

@app.post("/add_contact")
def add_contact(contact: Contact):
    new_contact = contact
    contacts[contact.name] = new_contact
    return "Contact added successfully"

@app.get("/view_contacts")
def view_contact():
    return contacts

@app.get("/search_contact")
def search_contact(contact_name: str):
    if contact_name in contacts:
        return contacts[contact_name]

@app.put("/update_contact")
def update_contact(contact_name: str, contact: Contact):
    if contact_name in contacts:
        del contacts[contact_name]
        new_data = contact
        contacts[contact.name] = new_data
        return "Contact updated successfully"
    
@app.delete("/delete_contact")
def delete_contact(contact_name: str):
    if contact_name in contacts:
        del contacts[contact_name]
        return "Contact deleted successfully"