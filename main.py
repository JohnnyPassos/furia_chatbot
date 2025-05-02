# main.py
"""
Ponto de entrada principal para iniciar o Bot Telegram da Furia CS.

Este script configura o logging, carrega o token da API do Telegram,
registra todos os handlers (comandos, botões, mensagens desconhecidas)
e inicia o bot em modo polling para receber atualizações.
"""
import logging
# É uma boa prática importar 'os' se você usa variáveis de ambiente
import os
from dotenv import load_dotenv
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

# Carregar variáveis de ambiente do .env (redundante se config.py já faz, mas garante)
# load_dotenv() # Descomente se config.py não carregar de forma confiável

# Importa a configuração (principalmente o token)
from bot.config import TELEGRAM_TOKEN

# Importa as funções handler dos seus respectivos módulos
from bot.handlers.start_help import start, unknown_command
from bot.handlers.info import proximojogo, ultimoresultado, elenco, ranking
from bot.handlers.links import links
from bot.handlers.news import noticias
from bot.handlers.button_handler import handle_button_press

# --- Configuração do Logging ---
# Define o formato e o nível (INFO mostra mensagens de status, WARNING só avisos/erros)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# Reduz o nível de log da biblioteca 'httpx' para evitar poluição no terminal
logging.getLogger("httpx").setLevel(logging.WARNING)
# Obtém um logger específico para este módulo (main)
logger = logging.getLogger(__name__)
# --- Fim do Logging ---

def main() -> None:
    """Configura e inicia a aplicação do bot."""

    # Verifica se o token foi carregado. Sem token, o bot não funciona.
    if not TELEGRAM_TOKEN:
         logger.critical("CRÍTICO: Token do Telegram não encontrado. Verifique o .env e config.py")
         return # Encerra a execução se não houver token

    logger.info("Token carregado com sucesso.")
    logger.info("Criando a instância da Application...")

    # Cria a 'Application' usando o ApplicationBuilder e passa o token
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    logger.info("Aplicação criada.")

    # --- Registro dos Handlers ---
    # A ordem importa! Handlers específicos primeiro, depois os mais gerais.

    # 1. CommandHandlers: Respondem a comandos específicos (ex: /start)
    logger.info("Registrando CommandHandlers...")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("proximojogo", proximojogo))
    application.add_handler(CommandHandler("ultimoresultado", ultimoresultado))
    application.add_handler(CommandHandler("elenco", elenco))
    application.add_handler(CommandHandler("ranking", ranking))
    application.add_handler(CommandHandler("links", links))
    application.add_handler(CommandHandler("noticias", noticias))
    # application.add_handler(CommandHandler("hype", hype_command)) # Descomente se implementar

    # 2. CallbackQueryHandler: Responde a cliques em botões inline
    logger.info("Registrando CallbackQueryHandler...")
    application.add_handler(CallbackQueryHandler(handle_button_press))

    # 3. MessageHandler para Comandos Desconhecidos:
    #    Pega qualquer comando (/) que NÃO foi tratado pelos CommandHandlers acima.
    #    Importante registrar depois dos CommandHandlers específicos.
    logger.info("Registrando MessageHandler para comandos desconhecidos...")
    application.add_handler(MessageHandler(filters.COMMAND & ~filters.UpdateType.EDITED_MESSAGE, unknown_command))
    # --- Fim do Registro ---

    # Inicia o Bot em modo Polling
    logger.info("Iniciando o bot em modo polling...")
    # run_polling busca continuamente por novas atualizações (mensagens) no Telegram.
    # É um processo bloqueante até que o bot seja parado (Ctrl+C).
    application.run_polling()

    # Esta linha normalmente só é alcançada ao parar o bot manualmente
    logger.info("Bot finalizado.")


# Este é o ponto de entrada padrão para scripts Python.
# O código aqui só roda quando você executa 'python main.py' diretamente.
if __name__ == "__main__":
    logger.info("Executando script principal (main.py)...")
    try:
        # Chama a função principal que configura e roda o bot
        main()
    except Exception as e:
        # Captura qualquer erro MUITO grave que possa ocorrer e não foi tratado
        # É crucial logar isso para depuração em caso de falha total.
        logger.critical(f"Erro CRÍTICO não capturado no loop principal: {e}", exc_info=True)