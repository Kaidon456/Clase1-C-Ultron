# Librerias Discord API
import discord
from discord.ext import commands
from discord import Colour
from discord import Embed
from discord import Intents
from discord import app_commands

# LIbrerias Auxilires
import json
from random import randint
import time
import conex as con
import comando as com
import Frases
from prettytable import PrettyTable
from prettytable import TableStyle
BOT_ID = 1365395968979107850

# Importacion de Token
with open("./Tokens.json") as file:
    data = json.load(file)

# Creacion del Prefijo
client = commands.Bot(command_prefix = 'U!', intents=discord.Intents.all(), help_command=None)


# Eventos Discord
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Larga vida clase 1-C'))
    print('Developed by Kaidon456')
    print('Powered by Discord API '+discord.__version__)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member: discord.Member):
    response = con.InsertUser(member.id,member.name)
    print(response)
    embed = Embed(title=f"***Bienvenido a la clase {member.mention}***", description="Recuerda las siguientes acciones para una mejor expericiencia dentro de la clase", color=Colour.random())
    embed.add_field(name="**Leer las reglas**", value="https://discord.com/channels/1364742230748696636/1364743522430750730", inline=False)
    embed.add_field(name="**Presentate al salon**", value="https://discord.com/channels/1364742230748696636/1364804432004382840", inline=False)
    embed.add_field(name="**Cumpleaños en el siguiente canal**", value="https://discord.com/channels/1364742230748696636/1365036789521453201", inline=False)
    embed.add_field(name="**Asignate tus roles**", value="https://discord.com/channels/1364742230748696636/1389295517401350234", inline=False)
    embed.set_footer(text="Larga vida Clase 1-C.")
    time.sleep(5)
    await client.get_channel(1365038654845751346).send(embed=embed)


    # await channel.send(f'Welcome {member.mention}.')

# <---------------------------------------COMANDOS--------------------------------------->
@client.command()
@commands.has_permissions(administrator=True)
async def anunciar(ctx, *args):
    """Permite a los docentes con permisos de administrador hacer un anuncio."""
    response = com.cadenas(args)
    message = f""" @everyone"""
    embed = Embed(title=" 📢 ***Anuncio Importante*** 📢", description=f"{response}", color=Colour.random())
    embed.set_footer(text="Larga vida Clase 1-C.")
    await client.get_channel(1365036980953419908).send(message, embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def recordatorio(ctx):
    """Funcion para mandar un recordatorios generales como asignarse autorol, leer las reglas y dar su cumpleaños"""
    embed = Embed(title="***Recordatorio***", description="Recuerda hacer las siguientes acciones si te falta alguna.", color=Colour.random())
    embed.set_image(url="https://pbs.twimg.com/profile_images/1916185280719020032/fQzoXWcS_400x400.jpg")
    embed.add_field(name="**Presentate al salon**", value="https://discord.com/channels/1364742230748696636/1364804432004382840", inline=False)
    embed.add_field(name="**Cumpleaños en el siguiente canal**", value="https://discord.com/channels/1364742230748696636/1365036789521453201", inline=False)
    embed.add_field(name="**Asignarte tus roles**", value="https://discord.com/channels/1364742230748696636/1389295517401350234", inline=False)
    embed.set_footer(text="Larga vida Clase 1-C.")
    # await ctx.send(embed=embed)
    await client.get_channel(1364742231206133782).send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def updatereglas(ctx, id_mensaje):
    DaRules = """
# 📜 Reglas Oficiales | Clase 1-C
Bienvenido(a) al servidor oficial de Clase 1-C. Estas normas buscan asegurar una experiencia sana, respetuosa y divertida para todos los miembros de la comunidad.

❌Contenido inapropiado
Está estrictamente prohibido compartir material gore o NSFW
(A NO SER QUE TODOS LOS DEMÁS INTEGRANTES ESTÉN DE ACUERDO Y DEBE BORRARSE DESPUÉS DE 10 MINUTOS).
La primera infracción recibirá una advertencia; reincidir conllevará expulsión inmediata.

🚫Discriminación
No se tolerarán expresiones o conductas de racismo, sexismo, homofobia ni ninguna otra forma de discriminación que no se digan en contexto de humor. Las bromas pueden ser aceptadas, siempre que no vulneren la dignidad de otros.

🎭Humor con límites
Las bromas pesadas están permitidas solo entre personas con confianza mutua y siempre dentro de un marco de respeto.
Roleos o simulaciones de peleas deben ser claramente marcadas como tales. El objetivo es el humor sano, no la humillación.

🔒Privacidad y seguridad
Está terminantemente prohibido cualquier intento de doxxeo:
No compartas ni solicites información personal.

🌐Conductas fuera del servidor
Acciones graves como acoso, doxxeo o conductas ilegales, incluso fuera del servidor, pueden ser motivo de sanción.

🤝Resolución de conflictos
Cualquier conflicto entre miembros deberá resolverse de forma privada, con apoyo del staff de 1-C como mediadores si es necesario.

📢Spam y estafas
Está prohibido el spam masivo.

✝️Estan estrictamente prohibidos hacer comentarios o ataques de Índice Político, Religioso u que ofendan a la cultura de otros.

📹Si vas a prender/Estás en Stream y vas a meterte a un Canal de voz , pon en el estado del canal: STREAM

🗣️Siguiendo la Anterior regla
Personas que van a unirse a un Canal de Voz, verificar si está el estado de "STREAM" en el Canal y en caso de meterse, mantener una actitud respetuosa tanto para el streamer como para su audiencia.
El bullying a Kreirus YA NO ES LEGAL.
"""
    # embed = Embed(title="***📜 __***Reglas Oficiales | Clase 1-C***__***", description="Bienvenido(a) al servidor oficial de Clase 1-C. Estas normas buscan asegurar una experiencia sana, respetuosa y divertida para todos los miembros de la comunidad.", color=Colour.purple)
    # embed.set_image(url="https://pbs.twimg.com/profile_images/1916185280719020032/fQzoXWcS_400x400.jpg")
    # embed.add_field(name="**❌Contenido inapropiado**", value="Está estrictamente prohibido compartir material gore o NSFW(A NO SER QUE TODOS LOS DEMÁS INTEGRANTES ESTÉN DE ACUERDO Y DEBE BORRARSE DESPUÉS DE 10 MINUTOS). La primera infracción recibirá una advertencia; reincidir conllevará expulsión inmediata.", inline=False)
    # embed.set_footer(text="Larga vida Clase 1-C.")
    try:
        # 1. Obtenemos el objeto Message desde la API usando el ID.
        # Documentación: https://discordpy.readthedocs.io/en/stable/api.html#discord.TextChannel.fetch_message
        mensaje = await ctx.channel.fetch_message(id_mensaje)

        # 2. Verificamos si el bot es el autor del mensaje (solo puedes editar tus propios mensajes)
        

        # 3. Aplicamos el cambio de texto.
        nuevo_texto = "esto es una prueba del cambio texto"
        await mensaje.edit(content=DaRules)
        await ctx.send(f"✅ Mensaje `{id_mensaje}` actualizado correctamente.", delete_after=5)

    except discord.NotFound:
        await ctx.send("No se encontró ningún mensaje con ese ID en este canal.")
    except discord.Forbidden:
        await ctx.send("No tengo permisos suficientes para realizar esta acción.")
    except Exception as e:
        await ctx.send(f"Ocurrió un error inesperado: {e}")
    await ctx.send(f"📢 **{ctx.author.mention}:** Las reglas fueron actualizadas correctamente", delete_after=10)


@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command()
async def denunciar(ctx, user: discord.Member = None):
    """Permite a los miembros levantar una orden de alejamiento"""
    if user is None:
        await ctx.send(f"Pendejo la denuncia no es para ti mismo o si?")
    elif user.id is ctx.author.id:
        await ctx.send(f"Pendejo la denuncia no es para ti mismo o si?")
    else:    
        response = con.AddOrden(user.id) # Llamado a la funcion de Update valor de denuncia +1
        await ctx.send(response)

@client.command()
@commands.guild_only()
async def denuncias(ctx, *args):
    """Permite ver la lista de personas con mas ordenes de alejamiento del server"""
    try:
        u = args[0]
    except:
        # Despliega la cantidad de ordenes de alejamiento del miembro que mando el mensaje
        response = con.SelectOrden(ctx.author.id)
        embed = Embed(title="*Ordenes de alejamiento*", description=f"{ctx.author.mention} cuenta con {response.data[0].get('order')} ordenes", color=Colour.magenta())
        await ctx.send(embed=embed)
    else:
        if u == "*": # Despliega una lista de los top 10 miembros con mas ordenes de alejamiento
            response = con.SelectOrden(None)
            table = PrettyTable()
            table.field_names = ["TOP", "<----Usuario----->", "Conteo"]
            table.set_style(TableStyle.PLAIN_COLUMNS)
            i = 1
            for user in response.data: # Lee y agrega a la tabla 
                table.add_row([f"{i}°",f" <@{user.get('id')}> -",user.get('order')])
                i += 1
            embed = Embed(title="***Tops con ordenes de alejamiento***", description=table, color=Colour.purple())
            await ctx.send(embed=embed)
        else: # Despliega las ordenes de un miembro pingeado
            exist = False
            user = int(u[2:-1])
            for member in ctx.guild.members: # Aquí es donde se realiza la verificación:
                if member.id == user: # Si Member y usuario son iguales
                    exist = True
                    break
            if exist == True: # Verifica si encontro el usuario 
                response = con.SelectOrden(user)
                embed = Embed(title="*Ordenes de alejamiento*", description=f"<@{user}> cuenta con {response.data[0].get('order')} ordenes", color=Colour.magenta())
                await ctx.send(embed=embed)
            else: # Se ingresa una cadena que no corresponde
                await ctx.send("# Es necesario pingear un usuario o un *")  

@client.command()
@commands.guild_only()
async def vocalario(ctx):
    """Funcion que despliega el top 10 de vocalarios en la base de datos"""
    opc = None
    response = con.SelectVocalario(opc)
    table = PrettyTable()
    table.field_names = ["TOP", "<----Usuario----->", "Conteo"]
    table.set_style(TableStyle.PLAIN_COLUMNS)
    i = 1
    for user in response.data: # Lee y agrega a la tabla 
        table.add_row([f"{i}°",f" <@{user.get('id')}> -",user.get('vocalario')])
        i += 1
    embed = Embed(title="***Tops Vocalarios***", description=table, color=Colour.purple())
    await ctx.send(embed=embed)


@client.command()
@commands.guild_only()
async def stats(ctx):
    """Despliega un Embed message para dar la lista de palabras en un formato de lista"""
    response = con.SelectCont()
    embed = Embed(title="__***Contadores generales***__", description="Aqui el contador de palabras y vocalario", color=Colour.random())
    for data in response:
        embed.add_field(name= data[0], value=data[1], inline=True)
    await ctx.send(embed=embed) 


@client.command()
@commands.guild_only()
async def profile(ctx, user: discord.Member = None):
    """Despliega tus estadisticas con las que se cuentas en la base de datos"""
    if user is None:
        response = con.SelectUser(ctx.author.id) # Llama para devolver los valores de los Denuncias, Vocalario, Atention, Stars
        embed = Embed(title=f"Perfil de __***{ctx.author.global_name}***__ ", description="Aqui tienes tus estadisticas de __***CLASE 1-C***__", color=Colour.random())
        embed.add_field(name="Denuncias", value=f"{response.data[0].get('order')}", inline=True)
        embed.add_field(name="Vocalario", value=f"{response.data[0].get('vocalario')}", inline=True)
        embed.add_field(name="Estrellas", value=f"{response.data[0].get('stars')}", inline=True)
        embed.add_field(name="Llamadas de atencion", value=f"{response.data[0].get('atention')}", inline=True)
        await ctx.send(embed=embed)   
    else:    
        response = con.SelectUser(user.id) # Llama para devolver los valores de los Denuncias, Vocalario, Atention, Stars
        embed = Embed(title=f"Perfil de __***{user.nick}***__ ", description="Aqui tienes tus estadisticas de __***CLASE 1-C***__", color=Colour.random())
        embed.add_field(name="Denuncias", value=f"{response.data[0].get('order')}", inline=True)
        embed.add_field(name="Vocalario", value=f"{response.data[0].get('vocalario')}", inline=True)
        embed.add_field(name="Estrellas", value=f"{response.data[0].get('stars')}", inline=True)
        embed.add_field(name="Llamadas de atencion", value=f"{response.data[0].get('atention')}", inline=True)
        await ctx.send(embed=embed)

@client.command()
async def creditos(ctx):
    """Despliega un Embed Message un menu de donde se detallen los creditos de varios detalles"""
    embed = Embed(title="***Creditos***", description="Un agradecimiento los que han aportado a la clase 1-C", color=Colour.random())
    embed.set_image(url="https://pbs.twimg.com/profile_images/1916185280719020032/fQzoXWcS_400x400.jpg")
    embed.add_field(name="**Redes**", value="<@617693849308889094><@257365930902814720> <@805898227446054953>", inline=False)
    embed.add_field(name="Arte", value="<@617693849308889094> <@318598735628206083>", inline=False)
    embed.add_field(name="Memes", value="<@257365930902814720> <@444604836219191297> <@400855538205982721>", inline=False)
    embed.add_field(name="Gifs", value="<@257365930902814720> <@314605600723959809> <@>400855538205982721", inline=False)
    embed.add_field(name="Desarrollador", value="<@356618682073481228>", inline=False)
    embed.set_footer(text="Larga vida Clase 1-C.")
    await ctx.send(embed=embed)

@client.command()
async def help(ctx, opc=""):
    """Despliega un Embed Message un menu de ayuda para el uso de comandos del mismo bot"""
    if opc == "admins":
        await ctx.send(f"📢 **{ctx.author.mention}:** Paciencia, este comando esta en desarrollo . agradezco su paciencia atte: señor K")
    else:
        embed = Embed(title="__***AYUDA***__", description="Aqui una breve descripcion del uso de cada comando disponible", color=Colour.magenta())
        embed.set_image(url="https://pbs.twimg.com/profile_images/1916185280719020032/fQzoXWcS_400x400.jpg")
        embed.add_field(name="U!denunciar <@usuario/id> ", value="Para es comando se arroba al usuario o su ID", inline=False)
        embed.add_field(name="U!denuncias <@usuario/vacio/*>", value="Arrobar a un usuario para ver sus denuncias,Vacio para ver tus propias denuncias, usar el * para ver el top 10 de denuncias de la clase", inline=False)
        embed.add_field(name="U!vocalario <vacio>", value="Ver el top 10 del vocalarios", inline=False)
        embed.add_field(name="U!stats <vacio>", value="Para ver los contadores generales del server", inline=False)
        embed.add_field(name="U!profile <@usuario/vacio>", value="arroba a alguien para ver su perfil, vacio para tu perfil", inline=False)
        embed.add_field(name="U!ping", value="Prueba si el bot funciona correctamente", inline=False)
        embed.add_field(name="U!creditos", value="Da la lista de quienes han apoyado al servidor en forma de arte, redes, memes, gifs, dessarrollo", inline=False)
        embed.add_field(name="U!help", value="Da una lista de los comando disponibles", inline=False)
        await ctx.send(embed=embed)

@client.command()
async def log(ctx):
    await ctx.send(f"📢 **{ctx.author.mention}:** Paciencia, este comando esta en desarrollo . agradezco su paciencia atte: señor K")
# <---------------------------------------SLASH COMMANDS--------------------------------------->


# <---------------------------------------EXTRAS--------------------------------------->
@client.command()
@commands.guild_only() # Asegura que el comando solo se pueda usar en un servidor
async def listar_miembros(ctx):
    """
    Lista la ID y el nombre de cada miembro en el servidor actual.
    Requiere que el bot tenga el Intent `discord.Intents.members` habilitado
    y permisos para ver los miembros del servidor.
    """
    if ctx.author.id != 356618682073481228:
        await ctx.send("Pa q quieres agregar a mas, dile al Señor K")
        return

    if not ctx.guild:
        await ctx.send("Este comando solo puede usarse en un servidor.")
        return
    for member in ctx.guild.members:
        # Accedemos a los atributos 'id' y 'name' del objeto Member
        # Documentación de discord.Member.id: https://discordpy.readthedocs.io/en/stable/api.html#discord.Member.id
        # Documentación de discord.Member.name: https://discordpy.readthedocs.io/en/stable/api.html#discord.Member.name
        print(f"Ingresa usuarioa  la base de datos a{member.id}:{member.name} ")
        #con.InsertUser(member.id,member.name)
    await ctx.send("Agregados y actualizados a la Base datos")

@client.listen()
async def on_message(message):
    if message.author.id == BOT_ID:
        return
    if "https://tenor.com/view/pass-banana-gif-23743798" in message.content and message.channel.id == 1365773983261261975:
        await message.channel.send("https://tenor.com/view/pass-banana-gif-23743798")
    if "hello there" in message.content.lower():
        if com.random100()<=5:
            await message.channel.send("https://tenor.com/view/general-kenobi-kenobi-general-hello-there-star-wars-gif-13723705")
        else:
            await message.channel.send("General Kenobi")
    if "larga vida clase 1-c" in message.content.lower():
        await message.reply("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGNjOW1pd3dlcWhoYmdkdjRjNnRya2Y0aDd2OGZ1YWZ2eWVrdzVhYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R7LG30RPpbAaqMIwaX/giphy.gif")
    if "1c 1c 1c" in message.content.lower():
        await message.reply("https://cdn.discordapp.com/attachments/1367363346021486613/1371972994624127036/1_3.gif?ex=682514eb&is=6823c36b&hm=8db52173a81f52f9f627d229787ea61e367184fc85bae570bbdfb8b5d8f816f8&")
    if "y pipo?" in message.content.lower():
        opc = "Flameo" if randint(1,100)>=50 else "Peruano"
        await message.reply(f"**Observa en {opc}*",file=discord.File('src/pipobosque.png'))
    # Parte dedicada al conteo de palabras 
    contenido = message.content.lower().replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').replace('_', ' ')
    # Separa las palabras para ser procesadas en forma de lista
    palabras = contenido.split()
    # Lectura de la lista y verificacion de para el contador
    for palabra in palabras:
        if palabra in Frases.weon:
            con.ContWeon()
            # Seleccion probabilidades para easter egg
            if randint(1, 100)<=5:
                await message.reply("Mucho chileno alv")
            break
        if palabra in Frases.wey:
            con.ContWey()
            if randint(1, 100)<=5:
                await message.reply("Mucho mexicano alv")
            break
        if palabra in Frases.pito:
            con.ContPico()
            if randint(1, 100)<=2:
                await message.reply("***Oh un pito!!***",file=discord.File('src/oh-un-pico.mp4'))
                time.sleep(2)
                await message.reply("Eh no cierto a mi no me gusta el pene")
            elif randint(1, 100)<= 20:
                await message.reply("Oh un pito!!")
            break
        if palabra in Frases.kbezuco:
            con.ContKbezuko()
            if randint(1,100)<=20:
                await message.reply("quiedes untate chodalate en el cuedpo?")
            break

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        print("Error: Faltan Argumentos ")
        await ctx.send("Faltan argumentos.")
    if isinstance(error, commands.CheckFailure):
        print("Error: Falta de permisos ")
        await ctx.send("**No tienes permisos**")
    if isinstance(error, commands.CommandNotFound):
        print("Error: Comando no existente ")
        if randint(1, 100)<=5:
            await ctx.send("https://tenor.com/te5hdcZaoTl.gif")

# Inicializacion del Bot
client.run(data.get('ID_BOT'))