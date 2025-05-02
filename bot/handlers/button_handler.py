# bot/handlers/button_handler.py
"""
Processa todas as interações de clique em botões inline (CallbackQuery).

Identifica qual botão foi pressionado através do 'callback_data' e
direciona para a ação apropriada, geralmente exibindo informações estáticas
buscadas de 'static_info.py' e um botão para voltar ao menu principal.
"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import logging

# Importa todas as variáveis estáticas necessárias para as respostas
from bot.data.static_info import (
    LINKS_UTEIS, ELENCO_ATUAL_INFO, RANKING_INFO, NOTICIAS_RECENTES,
    PROXIMO_JOGO_INFO, ULTIMO_RESULTADO_INFO
)

logger = logging.getLogger(__name__)

# --- Definição dos Teclados Inline ---

# Teclado com botão único para voltar ao menu inicial
teclado_voltar = InlineKeyboardMarkup(
    [[InlineKeyboardButton("⬅️ Voltar ao Menu Principal", callback_data='start_menu')]]
)

def gerar_teclado_principal():
    """Gera o InlineKeyboardMarkup para o menu principal de opções."""
    keyboard = [
        [InlineKeyboardButton("📅 Próximo Jogo", callback_data='proximo_jogo'), InlineKeyboardButton("📊 Último Resultado", callback_data='ultimo_resultado')],
        [InlineKeyboardButton("👥 Elenco", callback_data='elenco'), InlineKeyboardButton("🏆 Ranking", callback_data='ranking')],
        [InlineKeyboardButton("📰 Notícias", callback_data='noticias'), InlineKeyboardButton("🔗 Links Úteis", callback_data='links')]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- Handler Principal dos Botões ---

async def handle_button_press(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Função chamada pela biblioteca sempre que um botão inline é clicado.
    Processa o callback_data e edita a mensagem anterior com a resposta.
    """
    query = update.callback_query
    # Responde ao Telegram que o clique foi recebido (evita o "loading" infinito no botão)
    # Essencial para uma boa experiência do usuário.
    await query.answer()

    callback_data = query.data
    chat_id = query.message.chat_id # Guarda para possível mensagem de erro
    logger.info(f"Botão clicado! Callback data: {callback_data} | Chat ID: {chat_id}")

    # Define valores padrão para a resposta que será enviada/editada
    resposta_texto = f"Processando opção: {callback_data}..."
    reply_markup = teclado_voltar # Por padrão, a resposta terá o botão "Voltar"
    parse_mode = None             # Por padrão, sem formatação especial
    disable_preview = True        # Por padrão, desabilitar preview de links

    # Determina a resposta e o teclado correto baseado no botão clicado
    if callback_data == 'start_menu':
        resposta_texto = "Selecione uma opção abaixo:"
        reply_markup = gerar_teclado_principal() # Mostra o menu principal novamente

    elif callback_data == 'proximo_jogo':
        resposta_texto = PROXIMO_JOGO_INFO

    elif callback_data == 'ultimo_resultado':
        resposta_texto = ULTIMO_RESULTADO_INFO

    elif callback_data == 'elenco':
        resposta_texto = ELENCO_ATUAL_INFO

    elif callback_data == 'ranking':
        resposta_texto = RANKING_INFO

    elif callback_data == 'noticias':
        resposta_texto = NOTICIAS_RECENTES
        parse_mode = 'HTML' # As notícias usam links HTML

    elif callback_data == 'links':
        resposta_texto = LINKS_UTEIS
        # Links já são clicáveis, HTML não estritamente necessário, mas ok
        # parse_mode = 'HTML' # Poderia ser None também
        # disable_preview = True # Já é o padrão

    else:
        # Caso um callback_data inesperado seja recebido
        logger.warning(f"Callback_data desconhecido recebido: {callback_data}")
        resposta_texto = f"Opção desconhecida recebida."
        reply_markup = None # Não mostrar botão "Voltar" para um erro

    # Tenta editar a mensagem onde o botão foi clicado com a nova resposta
    try:
        await query.edit_message_text(
            text=resposta_texto,
            reply_markup=reply_markup, # Adiciona o teclado (Voltar ou Principal)
            parse_mode=parse_mode,
            disable_web_page_preview=disable_preview
        )
    except Exception as e:
        # Se a edição falhar (ex: mensagem muito antiga, conteúdo idêntico, erro de API),
        # loga o erro e envia uma mensagem de erro genérica ao usuário.
        # Evita que o bot "trave" para o usuário.
        logger.error(f"Falha ao editar mensagem do botão ({callback_data}): {e}. Enviando msg de erro fallback.")
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text="😕 Desculpe, ocorreu um erro ao tentar mostrar essa informação. Tente usar /start novamente."
            )
        except Exception as send_error:
             logger.error(f"Falha também ao enviar mensagem de erro de fallback: {send_error}.")