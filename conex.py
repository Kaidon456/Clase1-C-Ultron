import json
import os
from supabase import create_client, Client
from supabase.client import ClientOptions

# Importacion de Token
with open("./Tokens.json") as file:
    data = json.load(file)

url: str = data.get('API_LINK')
key: str = data.get('SUPA')
supabase: Client = create_client(
    url, 
    key,
    options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
    )
)

# <----------------------------------Usuarios---------------------------------->
def InsertUser(id: int, name: str):
    """FUNCION INSERT USER"""
    try:
        response = (
            supabase.table("c1_usuario")
            .insert([
                {"id": id, "name": name}
            ])
            .execute()
        )
        return f"Se agrego con exito a {name}!! "
    except Exception as exception:
        return f"Hubo un error con {name}!!"

def DeleteUser():
    """FUNCION DELETE USER"""

def UpdateUser():
    """FUNCION UPDATE USER"""

def SelectData():
    """FUNCION SELECT USER"""
    response = (
    supabase.table("c1_usuario")
    .select("*")
    .execute()
)
    print(response)

# <----------------------------------Demas data---------------------------------->
def AddOrden(id):
    """FUNCION AGREGAR ORDEN DE ALEJAMIENTO"""
    response = (
        supabase.table("c1_usuario")
        .select("order")
        .match({"id": id})
        .execute())
    order = response.data[0].get('order')
    order += 1
    response = (
        supabase.table("c1_usuario")
        .update({"order": order})
        .eq("id", id)
        .execute())
    return "Se levanto la orden de alejamiento con exito!"

def SelectOrden(id):
    """FUNCION SELECT ORDEN DE ALEJAMIENTO"""
    if id is None: # Imprime top 10
        response = (
            supabase.table("c1_usuario")
            .select("id, order")
            .limit(10)
            .order("order", desc=True)
            .execute())
        return response 
    else: # Imprime al miembro pingeado o al autor del mensaje
        response = (
            supabase.table("c1_usuario")
            .select("name, order")
            .match({"id": id})
            .execute())
        return response

def AddStar():
    """FUNCION INSERTAR"""

def AddAtencion():
    """FUNCION INSERTAR"""

def SelectUser(id):
    """Despliega y retorna la data del usuario en la base de datos"""
    response = (
        supabase.table("c1_usuario")
        .select("order, vocalario, stars, atention")
        .match({"id": id})
        .execute())
    return response

def SelectVocalario(opc):
    if opc is None:
        response = (
            supabase.table("c1_usuario")
            .select("id, vocalario")
            .limit(10)
            .order("vocalario", desc=True)
            .execute())
        return response
    if opc == "*":
        response = (supabase
            .rpc('sum_vocalario')
            .execute())
        return response