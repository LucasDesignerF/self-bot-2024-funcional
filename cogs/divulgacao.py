import discord
from discord.ext import commands, tasks
import asyncio
import os


class Divulgacao(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.servidor_id = None
        self.intervalo = 60  # Intervalo padrão de 60 segundos
        self.canal_logs = None  # Canal de logs
        self.divulgar_membros.start()  # Inicializar a tarefa de divulgação

    @commands.slash_command(
        name="config",
        description="Configurar o servidor, intervalo de divulgação e canal de logs")
    async def configurar(self, ctx: discord.ApplicationContext,
                         servidor: discord.Guild, intervalo: int, canal_logs: discord.TextChannel):
        """Configura o servidor, o intervalo e o canal de logs para divulgações"""
        self.servidor_id = servidor.id
        self.intervalo = intervalo
        self.canal_logs = canal_logs  # Salvar o canal de logs

        await ctx.respond(
            f"Configurações definidas: Servidor = {servidor.name} (ID: {servidor.id}), Intervalo = {intervalo} segundos, Canal de Logs = {canal_logs.mention}."
        )

    @tasks.loop(seconds=60)
    async def divulgar_membros(self):
        """Enviar mensagem de divulgação para cada membro do servidor"""
        if self.servidor_id is None or self.canal_logs is None:
            return

        guild = self.bot.get_guild(self.servidor_id)
        if not guild:
            print("Servidor não encontrado.")
            return

        try:
            for member in guild.members:
                # Ignora bots e membros já divulgados
                if member.bot or self.ja_divulgado(member.id):
                    continue

                # Envia a mensagem de divulgação
                await member.send(
                    "Olá! Sou eu, CEO Lucas Fortes, mandando essa mensagem pelo nosso bot. \n Como o Discord da Graf foi invadido a uns meses atrás, precisamos de sua ajuda para manter o servidor ativo e com o máximo de membros possíveis. \n Se você também é um membro da Graf, por favor, entre no nosso servidor de suporte e ajude o servidor a crescer novamente! \n Estamos com um novo nome e um novo discord: https://dub.sh/codeconnect \n \n Obrigado pela sua ajuda!"
                )
                self.salvar_membro_divulgado(member.id)
                
                # Envia log de divulgação para o canal designado
                await self.canal_logs.send(f"✅ Mensagem enviada para {member.name} ({member.id})")

                await asyncio.sleep(self.intervalo)  # Intervalo entre as mensagens

        except Exception as e:
            print(f"Erro ao divulgar: {e}")

    def ja_divulgado(self, member_id):
        """Verificar se o membro já foi divulgado"""
        if not os.path.exists("membros_divulgados.txt"):
            return False
        with open("membros_divulgados.txt", "r") as f:
            ids_divulgados = f.read().splitlines()
        return str(member_id) in ids_divulgados

    def salvar_membro_divulgado(self, member_id):
        """Salvar o ID do membro divulgado no arquivo"""
        with open("membros_divulgados.txt", "a") as f:
            f.write(f"{member_id}\n")


def setup(bot):
    bot.add_cog(Divulgacao(bot))
