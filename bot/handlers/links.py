# bot/handlers/links.py
"""
Contém o handler para o comando /links.

Este handler busca a lista de links úteis pré-definida
no arquivo 'bot.data.static_info' e a envia ao usuário.
Responde apenas à invocação direta do comando /links.
"""
from telegram import Update
from telegram.ext import ContextTypes
import logging # Importação do logging

# Importa a variável estática com a lista de links
from bot.data.static_info import LINKS_UTEIS

logger = logging.getLogger(__name__) # Logger para este módulo

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia a lista de links úteis (dados estáticos) via comando."""
    # Verifica se o update veio de uma mensagem de comando válida
    if update.message:
        logger.info(f"Comando /links recebido por {update.effective_user.username}")
        # Envia o texto formatado da variável LINKS_UTEIS
        # disable_web_page_preview=True evita que o Telegram gere prévias
        # grandes para cada link, deixando a mensagem mais limpa.
        await update.message.reply_text(LINKS_UTEIS, disable_web_page_preview=True)
    else:
        # Log caso esta função seja chamada inesperadamente sem uma mensagem
        logger.warning("Handler 'links' chamado sem 'update.message'.")