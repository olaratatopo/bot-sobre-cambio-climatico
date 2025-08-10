import discord
import random
import requests
from discord.ext import commands

# iniciar el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    channel = bot.get_channel(1400572850880122952)
    if channel:
        await channel.send("Para saber los comandos utiliza /ayuda")

# Devolver mensajes


@bot.command()
async def ayuda(ctx):
    await ctx.send("Los comandos son: /consecuencias, /causas, /evitarlo, /meme, /mas_info /video, /calculadora_co2, /clima (ubicacion) ")


@bot.command()
async def consecuencias(ctx):
    await ctx.send("hay muchas consecuencias pero las principales consecuencias ambientales son: aumento en la temperatura global, deshielo de los polos y glaciares, cambio de patrones climáticos, pérdida de biodiversidad.Las pricipales consecuencias sociales y económicas: migraciones climáticas, impacto en la agricultura, aumento de la pobreza y genera escazes de recursos ")


@bot.command()
async def causas(ctx):
    await ctx.send("El calentamiento global es el aumento progresivo de la temperatura media del planeta, y sus causas principales están relacionadas con la actividad humana. La más importante es la emisión de gases de efecto invernadero, que se liberan principalmente por la quema de combustibles fósiles (carbón, petróleo y gas natural) en la industria, el transporte y la generación de electricidad, otra causa relevante es la deforestación, ya que los árboles absorben CO₂, y al ser talados, se reduce la capacidad de la Tierra para eliminar este gas de la atmósfera, la agricultura intensiva y la ganadería también contribuyen significativamente, otras fuentes incluyen el uso excesivo de fertilizantes, ciertos procesos industriales y la acumulación de residuos que liberan gases al descomponerse.")


@bot.command()
async def evitarlo(ctx):
    await ctx.send("Una de las formas más importantes de combatir el cambio climático es reducir las emisiones de gases de efecto invernadero, como el dióxido de carbono (CO₂). Esto se logra utilizando energías limpias y renovables, como la solar, la eólica o la hidroeléctrica, en lugar de combustibles fósiles como el petróleo o el carbón. Además, es fundamental fomentar el transporte sostenible, como andar en bicicleta, caminar, usar el transporte público o vehículos eléctricos. También se debe reducir el consumo innecesario de energía, apagando luces y aparatos que no se usan, y mejorando la eficiencia energética en casas y edificios. Otra acción clave es proteger y plantar árboles, ya que absorben CO₂ y ayudan a regular el clima. La reducción del uso de plásticos, el reciclaje, y una alimentación más basada en productos vegetales también son medidas efectivas para reducir el impacto ambiental. Por último, es importante educar y generar conciencia sobre el problema, para que más personas se sumen a cuidar el planeta. Cada acción, por pequeña que parezca, contribuye a un futuro más sostenible.")


@bot.command()
async def mas_info(ctx):
    await ctx.send("Un artículo de la ONU sobre el calentamiento global:" \
    "https://www.un.org/es/un75/climate-crisis-race-we-can-win" \
    "Un artículo de la ONU sobre las causas y efectos del calentamiento global:" \
    "https://www.un.org/es/climatechange/science/causes-effects-climate-change")


@bot.command()
async def meme(ctx):
    fotos = random.randint(1, 8)
    if fotos == 1:
        await ctx.send("https://vamosahaceralgoporlatierra.com/wp-content/uploads/2019/11/520-ctxt-trump-cambio-climatico.jpg")
    elif fotos == 2:
        await ctx.send("https://vamosahaceralgoporlatierra.com/wp-content/uploads/2019/11/tot%C3%A9-2.jpg")
    elif fotos == 3:
        await ctx.send("https://vamosahaceralgoporlatierra.com/wp-content/uploads/2019/11/3c69fcccc336c602e1e6ce0dc4481d1e.jpg")
    elif fotos == 4:
        await ctx.send("https://vamosahaceralgoporlatierra.com/wp-content/uploads/2019/11/mafalda-1.jpg")
    elif fotos == 5:
        await ctx.send("https://vamosahaceralgoporlatierra.com/wp-content/uploads/2019/11/feggo.jpg")
    elif fotos == 6:
        await ctx.send("https://agqcvcudno.cloudimg.io/v7/climatica.coop/wp-content/uploads/2024/01/en-el-divan.jpg")
    elif fotos == 7:
        await ctx.send("https://colegiomontessori.cl/wp2/wp-content/uploads/2021/09/memes-interescolar-agosto-3.jpg")
    elif fotos == 8:
        await ctx.send("https://agenciasanluis.com/wp-content/uploads/2021/11/03-Memes-finalistas.jpg")


@bot.command()
async def video(ctx):
    videos = random.randint(1, 5)
    if videos == 1:
        await ctx.send("https://youtu.be/J9qSv2bwr9o")
    elif videos == 2:
        await ctx.send("https://youtu.be/kcr-Ryq6Nrk?si=zsfzGgZb4tK6rio6")
    elif videos == 3:
        await ctx.send("https://youtu.be/umAGi80FsPM?si=xvKgtanzl_hVrfwi")
    elif videos == 4:
        await ctx.send("https://youtu.be/FeKld35Pxhg?si=VCr821OaqN9LAshZ")
    elif videos == 5:
        await ctx.send("https://youtu.be/GLTCiS6hOT4?si=kEaz0jGL_xrTH4If")


@bot.command()
async def calculadora_co2(ctx):
    await ctx.send("Ingrese al siguiente link para calcualar su consumo de CO2, demora aproximadamente 6-8 mins: https://calculadora-carbono.climatehero.org/")


@bot.command(name='clima', help='Muestra el clima actual para una ubicación.')
async def clima(ctx, *, ubicacion: str):
    """
    Obtiene y muestra el clima actual para la ubicación especificada.
    """
    try:
        # Realiza la petición a la API de wttr.in
        url = f'https://wttr.in/{ubicacion}?format=j1'
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        data = response.json()

        # Extrae la información relevante del clima
        current_condition = data['current_condition'][0]
        temperatura = current_condition['temp_C']
        descripcion = current_condition['weatherDesc'][0]['value']
        humedad = current_condition['humidity']
        viento = current_condition['windspeedKmph']

        # Crea un mensaje embed para mostrar la información
        embed = discord.Embed(
            title=f'Clima actual en {ubicacion}',
            color=discord.Color.blue()
        )
        embed.add_field(name='Temperatura', value=f'{temperatura}°C', inline=False)
        embed.add_field(name='Descripción', value=descripcion, inline=False)
        embed.add_field(name='Humedad', value=f'{humedad}%', inline=False)
        embed.add_field(name='Viento', value=f'{viento} km/h', inline=False)
        embed.set_footer(text='Fuente: wttr.in')

        # Envía el mensaje embed al canal de Discord
        await ctx.send(embed=embed)

    except requests.exceptions.RequestException as e:
        await ctx.send(f'Error al obtener el clima: {e}')
    except (KeyError, IndexError) as e:
        await ctx.send('No se pudo encontrar la información del clima para esa ubicación.')


bot.run("Token")
