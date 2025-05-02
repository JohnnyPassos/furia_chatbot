# bot/handlers/start_help.py
"""
Contém os handlers para o comando inicial /start (que exibe o menu de botões)
e para lidar com comandos desconhecidos enviados ao bot.
"""
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import logging

# Importa a função que cria o teclado principal do handler de botões
from .button_handler import gerar_teclado_principal

logger = logging.getLogger(__name__) # Logger para este módulo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia mensagem de boas-vindas personalizada com botões inline."""
    # Verifica se o update contém uma mensagem (esperado para /start)
    if update.message:
        user = update.effective_user
        logger.info(f"Comando /start recebido por {user.username}")

        # Mensagens definidas
        mensagem_boas_vindas = rf"🐾 Fala, Guerreiro(a) {user.mention_html()}! 🎮 Bem-vindo(a) ao Bot Furia CS! Infos sobre jogos, elenco, notícias e mais, tudo na mão! ⚫⚪"
        mensagem_prompt = "O que você quer saber agora? Clica aí! 👇"

        # Gera o teclado principal usando a função importada
        reply_markup = gerar_teclado_principal()

        # Envia as mensagens
        await update.message.reply_html(mensagem_boas_vindas)
        await update.message.reply_text(mensagem_prompt, reply_markup=reply_markup)
    else:
        logger.warning("Handler 'start' chamado sem 'update.message'.")


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde a comandos /comandos que não foram reconhecidos pelos outros handlers."""
    # Verifica se o update contém uma mensagem (esperado para comandos)
    if update.message:
        # Log para registrar qual comando inválido foi recebido e por quem
        logger.info(f"Comando desconhecido '{update.message.text}' recebido por {update.effective_user.username}")
        await update.message.reply_text(
            "Comando não reconhecido, guerreiro(a)! 🤔\n"
            "Digite /start para ver as opções disponíveis nos botões."
        )
    else:
        logger.warning("Handler 'unknown_command' chamado sem 'update.message'.")