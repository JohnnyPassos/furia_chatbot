# bot/handlers/info.py
"""
Contém os handlers para os comandos que fornecem informações
estáticas sobre o time de CS da Furia (próximo jogo, último resultado,
elenco, ranking), buscando os dados de 'bot.data.static_info'.

Estes handlers respondem apenas às invocações diretas de comando (/comando).
As respostas aos cliques nos botões inline são tratadas em 'button_handler.py'.
"""
from telegram import Update
from telegram.ext import ContextTypes
import logging

# Importa os dados estáticos necessários
from bot.data.static_info import (
    PROXIMO_JOGO_INFO, ULTIMO_RESULTADO_INFO,
    ELENCO_ATUAL_INFO, RANKING_INFO
)

logger = logging.getLogger(__name__) # Logger para este módulo

async def proximojogo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações estáticas sobre o próximo jogo via comando."""
    # Só responde se for uma mensagem de comando válida
    if update.message:
        logger.info(f"Comando /proximojogo recebido por {update.effective_user.username}")
        await update.message.reply_text(PROXIMO_JOGO_INFO)
    else:
        # Log caso esta função seja chamada inesperadamente sem uma mensagem
        logger.warning("Handler 'proximojogo' chamado sem 'update.message'.")

async def ultimoresultado(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações estáticas sobre o último resultado via comando."""
    if update.message:
        logger.info(f"Comando /ultimoresultado recebido por {update.effective_user.username}")
        await update.message.reply_text(ULTIMO_RESULTADO_INFO)
    else:
        logger.warning("Handler 'ultimoresultado' chamado sem 'update.message'.")

async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia a line-up atual (dados estáticos) via comando."""
    if update.message:
        logger.info(f"Comando /elenco recebido por {update.effective_user.username}")
        await update.message.reply_text(ELENCO_ATUAL_INFO)
    else:
        logger.warning("Handler 'elenco' chamado sem 'update.message'.")

async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia o ranking atual (dados estáticos) via comando."""
    if update.message:
        logger.info(f"Comando /ranking recebido por {update.effective_user.username}")
        await update.message.reply_text(RANKING_INFO)
    else:
        logger.warning("Handler 'ranking' chamado sem 'update.message'.")