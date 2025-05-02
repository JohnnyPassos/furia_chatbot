# bot/config.py
"""
Módulo de configuração para o bot.

Responsável por carregar variáveis de ambiente (especialmente o token da API do Telegram)
a partir de um arquivo .env localizado na raiz do projeto.
Garante que o token essencial do Telegram esteja presente antes da execução.
"""
import os
from dotenv import load_dotenv
import logging # Adicionado para logar o status

logger = logging.getLogger(__name__) # Logger para este módulo

# Define o caminho absoluto para o arquivo .env na pasta raiz do projeto
# (um nível acima da pasta 'bot' onde este arquivo está)
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Tenta carregar as variáveis do arquivo .env especificado
logger.info(f"Tentando carregar variáveis de ambiente de: {dotenv_path}")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)
    logger.info("Arquivo .env encontrado e carregado.")
else:
    logger.warning(f"Arquivo .env não encontrado em {dotenv_path}. O token deve ser definido como variável de ambiente do sistema.")

# Busca o token da variável de ambiente 'TELEGRAM_BOT_TOKEN'
# os.getenv retorna None se a variável não estiver definida.
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Verifica se o token foi efetivamente carregado. É essencial para o bot funcionar.
if TELEGRAM_TOKEN is None:
    error_message = (
        "CRÍTICO: Token do Telegram (TELEGRAM_BOT_TOKEN) não encontrado no ambiente! "
        "Verifique se:\n"
        "1. O arquivo .env existe na pasta raiz ('furia_chatbot/').\n"
        "2. Ele contém a linha EXATA: TELEGRAM_BOT_TOKEN=SEU_TOKEN_REAL\n"
        "3. As permissões de leitura do arquivo .env estão corretas.\n"
        "O bot não pode iniciar sem o token."
    )
    logger.critical(error_message)
    # Levanta um erro claro que interrompe a execução do programa.
    raise ValueError(error_message)
else:
    # Log de sucesso (mostrando apenas o final do token por segurança)
    logger.info("Token do Telegram carregado com sucesso (final: ...%s).", TELEGRAM_TOKEN[-4:])

# Poderíamos adicionar aqui carregamento de outras chaves de API (PandaScore, NewsAPI)
# se tivéssemos decidido usá-las, com verificações semelhantes.