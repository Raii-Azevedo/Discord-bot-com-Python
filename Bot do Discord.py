#  CONECTANDO O BOT DENTRO DA SUA GUILDA NO DISCORD
import os

import discord,asyncio,random

client = discord.Client()
guild = "COLOQUE O NOME DO SEU SERVIDOR AQUI"

@client.event
async def on_ready():
    print (f'{client.user} está conectado ao seguinte servidor/guilda:\n'
    f'{guild}'
        )


@client.event
async def on_message(message):
    # COLOQUE AQUI A MSG QUE IRÁ DÁ O GATILHO DE START PARA SEU BOT
    if message.content.startswith("MSG DE GATILHO START"):
        channel = message.channel
        # COLOQUE AQUI A MSG DE SAUDAÇÃO INICIAL QUE SEU BOT IRÁ RESPONDER
        await channel.send("MSG DE SAUDAÇÃO DO BOT")

    # ADICIONANDO OUTRAS REAÇÕES A SEU BOT
    if message.content.lower().startswith('?humor'):
        # ADICIONANDO UMA FUNÇÃO DE PERMISSÃO NO CÓDIGO
        if message.author.id == "COLE SUA ID AQUI":
            escolha = random.randint(1,2)
            if escolha == 1:
                await message.add_reaction('😀')
                await message.channel.send("Robôs não sentem emoção")
            if escolha == 2:
                await message.add_reaction('😞')
                await message.channel.send("Robôs não sentem emoção")
            else:
                # MENSAGEM CASO NÃO HAJA PERMISSÃO DE COMANDO
                await message.channel.send("Você não tem permissão pra usar esse comando")



client.run("COLOQUE O TOKEN DO SEU BOT AQUI")
# Após esse processo seu Bot estará online dentro da sua guilda no Discord