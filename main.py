import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Logo ASCII
print(r"""
███████ ███████ ██      ███████     ██████   ██████  ████████     ██████   ██████  ██████  ██   ██ 
██      ██      ██      ██          ██   ██ ██    ██    ██             ██ ██  ████      ██ ██   ██ 
███████ █████   ██      █████       ██████  ██    ██    ██         █████  ██ ██ ██  █████  ███████ 
     ██ ██      ██          ██   ██ ██    ██    ██        ██        ██      ████  ██ ██           ██ 
███████ ███████ ███████ ██          ██████   ██████     ██        ███████  ██████  ███████      ██ 
""")

# Configuração do bot
intents = discord.Intents.all()  # Ativar todas as intents
bot = commands.Bot(intents=intents)


# Evento ao iniciar
@bot.event
async def on_ready():
    print("✅ Bot está online")
    print(f"✅ Conectado como {bot.user}")

    # Exibir todos os servidores em que o bot está conectado
    print("🌐 Conectado aos seguintes servidores:")
    for guild in bot.guilds:
        print(f" - {guild.name} (ID: {guild.id})")

    # Definir o status do bot como "Online"
    await bot.change_presence(activity=discord.Game(name="To divulgando a porra toda! 🧪"))
    print("🔄 Status do bot definido para 'To divulgando a porra toda! 🧪'")

    # Carrega as cogs e registra os comandos Slash
    for cog in os.listdir("./cogs"):
        if cog.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{cog[:-3]}")
                print(f"✅ Cog carregada: {cog}")
            except Exception as e:
                print(f"❌ Erro ao carregar cog {cog}: {e}")

    # Sincroniza os comandos Slash
    await bot.sync_commands()
    print("✅ Comandos Slash sincronizados!")


# Verificação diária do status de ativação do servidor
@tasks.loop(hours=24)
async def check_activation_status():
    print("🔄 Verificando status de ativação dos servidores...")
    # Aqui, você pode adicionar lógica para verificar o status dos servidores e agir conforme necessário.


# Iniciar a tarefa de verificação de status de ativação
check_activation_status.start()

bot.run(TOKEN)
