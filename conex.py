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

# <----------------------------------Ordenes de alejamiento---------------------------------->
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

# <----------------------------------Vocalario---------------------------------->
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

# <----------------------------------Stars---------------------------------->
def AddStar():
    """FUNCION INSERTAR"""

# <----------------------------------Atencion---------------------------------->
def AddAtencion():
    """FUNCION INSERTAR"""

# <----------------------------------Contadores---------------------------------->
def ContPico():
    """Funcion para actualizar el contador de la Tabla c1_conteos del registro 'pito' """
    response = (
        supabase.table("c1_conteos")
        .select("conteo")
        .match({"Palabra": "Pito"})
        .execute())
    cont = response.data[0].get('conteo')
    cont += 1
    response = (
        supabase.table("c1_conteos")
        .update({"conteo": cont})
        .eq("id", 2)
        .execute())

def ContWeon():
    """Funcion para actualizar el contador de la Tabla c1_conteos del registro 'weon'"""
    response = (
        supabase.table("c1_conteos")
        .select("conteo")
        .match({"Palabra": "Weon"})
        .execute())
    cont = response.data[0].get('conteo')
    cont += 1
    response = (
        supabase.table("c1_conteos")
        .update({"conteo": cont})
        .eq("id", 3)
        .execute())

def ContWey():
    """Funcion para actualizar el contador de la Tabla c1_conteos del registro 'wey'"""
    response = (
        supabase.table("c1_conteos")
        .select("conteo")
        .match({"Palabra": "Wey"})
        .execute())
    cont = response.data[0].get('conteo')
    cont += 1
    response = (
        supabase.table("c1_conteos")
        .update({"conteo": cont})
        .eq("id", 4)
        .execute())

def ContKbezuko():
    """Funcion para actualizar el contador de la Tabla c1_conteos del registro 'Kbezuko'"""
    response = (
        supabase.table("c1_conteos")
        .select("conteo")
        .match({"Palabra": "Kbezuko"})
        .execute())
    cont = response.data[0].get('conteo')
    cont += 1
    response = (
        supabase.table("c1_conteos")
        .update({"conteo": cont})
        .eq("id", 1)
        .execute())

# <----------------------------------Data General---------------------------------->
def SelectUser(id):
    """Despliega y retorna la data del usuario en la base de datos"""
    response = (
        supabase.table("c1_usuario")
        .select("order, vocalario, stars, atention")
        .match({"id": id})
        .execute())
    return response

def SelectCont():
    """Despliega los contadores generales"""
    responseCont = (
        supabase.table("c1_conteos")
        .select("*")
        .execute())
    responseVoca = (
        supabase
        .rpc('sum_vocalario')
        .execute())
    response = [["Vocalario",responseVoca.data]]
    for datos in responseCont.data:
        response.append([datos.get('Palabra'),datos.get('conteo')])
    return response
