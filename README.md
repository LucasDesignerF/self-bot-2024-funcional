**Documentação do Bot de Divulgações**


# Visão Geral
Este bot de Discord foi desenvolvido para ajudar na divulgação de um servidor específico através de mensagens diretas (DM) para os membros. Além disso, ele permite o registro de logs de envio em um canal designado, possibilitando monitorar as mensagens enviadas.

#Funcionalidades
:small_blue_diamond: **Comandos**

**/config**
`Descrição:` Configura o servidor, intervalo de divulgação e canal de logs para as mensagens enviadas.

**Parâmetros:**
`servidor:` O servidor onde o bot irá operar (tipo: discord.Guild).
`intervalo:` O intervalo em segundos entre o envio de mensagens diretas.
`canal_logs`: O canal onde os logs de envio das mensagens serão registrados (tipo: discord.TextChannel).

# Tarefas Automáticas
-** Divulgação de Membros: **O bot percorre todos os membros do servidor especificado e envia uma mensagem direta de divulgação, respeitando o intervalo configurado. Ele ignora bots e membros que já receberam a mensagem.

# Logs de Divulgação
- O bot registra cada mensagem enviada em um canal designado, permitindo que os administradores acompanhem as ações do bot em tempo real.

# Estrutura do Código
**Classe Divulgacao**
A classe principal que contém a lógica do bot.

**Métodos**
__init__(self, bot): Inicializa o bot, define variáveis de configuração e inicia a tarefa de divulgação.

- configurar(self, ctx, servidor, intervalo, canal_logs): Método que define as configurações do bot. Salva o ID do servidor, intervalo de tempo e o canal para logs.

- divulgar_membros(self): Tarefa em loop que envia mensagens diretas para os membros do servidor. Usa await asyncio.sleep(self.intervalo) para respeitar o intervalo definido entre as mensagens.

- ja_divulgado(self, member_id): Verifica se um membro já recebeu a mensagem de divulgação, lendo os IDs de um arquivo de texto.

- salvar_membro_divulgado(self, member_id): Salva o ID do membro que já foi divulgado em um arquivo de texto para evitar reenvios.

# Arquivos
- membros_divulgados.txt: Um arquivo de texto que armazena os IDs dos membros que já receberam a mensagem de divulgação. Esse arquivo é usado para verificar se um membro já foi contatado.
# Uso
Instalação: Certifique-se de ter a biblioteca discord.py instalada em seu ambiente Python.
```py
pip install discord.py
```
- Adicionar o Bot ao Servidor: Use o link de autorização do bot para adicioná-lo ao seu servidor Discord.

- Configuração: Após adicionar o bot, use o comando /config para definir o servidor, o intervalo de mensagens e o canal de logs. Exemplo:

/config servidor:<nome do servidor> intervalo:60 canal_logs:<#canal>
Execução: Após a configuração, o bot começará a enviar mensagens diretas para os membros do servidor no intervalo definido. Os logs de envio aparecerão no canal designado.

# Considerações Finais
**Limites do Discord:** É importante respeitar os limites de envio de mensagens diretas do Discord para evitar que o bot seja penalizado ou bloqueado.
**Segurança:** Certifique-se de que o bot tenha as permissões necessárias para enviar mensagens diretas e acessar os canais.
# Contribuição
Se você deseja contribuir para o desenvolvimento do bot, sinta-se à vontade para fazer pull requests ou abrir issues no repositório.
