# bot/handlers/news.py
"""
Contém o handler para o comando /noticias.

Este handler busca a lista de notícias recentes pré-definida (com links HTML)
no arquivo 'bot.data.static_info' e a envia ao usuário via comando direto.
A resposta ao botão correspondente ('noticias') é tratada em 'button_handler.py'.
"""
from telegram import Update
from telegram.ext import ContextTypes
import logging

# Importa a variável estática de notícias
from bot.data.static_info import NOTICIAS_RECENTES

logger = logging.getLogger(__name__) # Logger para este módulo

async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia as notícias estáticas recentes via comando."""
    # Verifica se o update veio de uma mensagem de comando válida
    if update.message:
        logger.info(f"Comando /noticias (estático) recebido por {update.effective_user.username}")
        # Envia diretamente o conteúdo da variável NOTICIAS_RECENTES.
        # Usa reply_html porque a string contém tags <a> para os links.
        # Desabilita o preview para não poluir a mensagem com prévias das notícias.
        await update.message.reply_html(NOTICIAS_RECENTES, disable_web_page_preview=True)
    else:
        # Log caso esta função seja chamada inesperadamente sem uma mensagem
        logger.warning("Handler 'noticias' chamado sem 'update.message'.")
