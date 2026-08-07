import discord
from discord.ext import commands
from bot_logic import gen_pass, roll_dice
from bot_information import token
import random
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f642')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong')

@bot.command()
async def roll(ctx, lados: int = 6):
    resultado = roll_dice(lados)
    await ctx.send("Você tirou: " + str(resultado))

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def quiz(ctx):
    await ctx.send(f'Quanto tempo aproximadamente uma garrafa plástica pode levar para se decompor?')
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    points = 0
    respond = await bot.wait_for('message', check=check)
    
    if respond.content == '400':
        await ctx.send('Acertou!!')
        points += 1
    else:
        await ctx.send('Errou!!')

    await ctx.send(f'Qual é o processo de transformar materiais usados em novos produtos?')
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    respond = await bot.wait_for('message', check=check)
    
    if respond.content == 'reciclagem':
        await ctx.send('Acertou!!')
        points += 1
    else:
        await ctx.send('Errou!!')

    await ctx.send(f'Qual gás é um dos principais responsáveis pelo efeito estufa causado por atividades humanas?')
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    respond = await bot.wait_for('message', check=check)
    
    if respond.content == 'co2':
        await ctx.send('Acertou!!')
        points += 1
    else:
        await ctx.send('Errou!!')

    await ctx.send(f'Qual é a cor tradicionalmente associada à lixeira de papel?')
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    respond = await bot.wait_for('message', check=check)
    
    if respond.content == 'azul':
        await ctx.send('Acertou!!')
        points += 1
    else:
        await ctx.send('Errou!!')

    await ctx.send(f'Qual é o nome do processo de degradação de um ecossistema devido à perda de nutrientes e cobertura vegetal?')
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    respond = await bot.wait_for('message', check=check)
    
    if respond.content == 'desertificação':
        await ctx.send('Acertou!!')
        points += 1
    else:
        await ctx.send('Errou!!')

    await ctx.send('Total de pontos: ' + str(points))

    if(points == 4):
         await ctx.send('Voce acertou tudo!!') 
    else:
        await ctx.send('Voce errou ' + str(5 - points) + ' pontos') 
bot.run(token)