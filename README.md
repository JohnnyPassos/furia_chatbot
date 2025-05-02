# Bot Furia CS - Desafio Furia Tech (Assistente de Eng. Software)

## Descrição

Este é um bot para Telegram desenvolvido como parte do processo seletivo para a vaga de Assistente de Engenharia de Software na Furia Tech (Abril/Maio 2025).

O objetivo principal é criar uma experiência conversacional para os fãs do time de Counter-Strike (CS2) da FURIA, permitindo acompanhar informações relevantes e interagir de forma simples através do Telegram.

## Funcionalidades

O bot oferece as seguintes funcionalidades através de comandos diretos ou botões inline (acionados via `/start`):

* **`/start`**: Inicia a conversa, exibe uma mensagem de boas-vindas personalizada e o menu principal com botões.
* **`/proximojogo`** (Botão: `📅 Próximo Jogo`): Mostra informações sobre a próxima partida agendada ou o próximo grande torneio da equipe de CS.
* **`/ultimoresultado`** (Botão: `📊 Último Resultado`): Exibe o resultado (placar, adversário, torneio) da última partida importante disputada pelo time de CS.
* **`/elenco`** (Botão: `👥 Elenco`): Apresenta a line-up atual da equipe de CS, incluindo jogadores ativos, stand-ins (se houver), coach e jogadores no banco.
* **`/ranking`** (Botão: `🏆 Ranking`): Mostra a posição atual da FURIA nos rankings mundiais de CS (HLTV e ESL).
* **`/links`** (Botão: `🔗 Links Úteis`): Fornece uma lista de links úteis relacionados à FURIA (redes sociais, loja oficial, site, HLTV, Liquipedia, etc.).
* **`/noticias`** (Botão: `📰 Notícias`): Exibe 2-3 das manchetes de notícias mais recentes e relevantes sobre a FURIA CS, com links para as fontes.
* **Comandos Inválidos:** O bot responde com uma mensagem de ajuda se um comando não reconhecido for enviado.
* **Navegação:** Botão "⬅️ Voltar ao Menu Principal" permite retornar ao menu inicial após visualizar uma informação.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Biblioteca Telegram:** `python-telegram-bot` v20+ (Assíncrona)
* **Variáveis de Ambiente:** `python-dotenv` (para carregar o Token da API)
* **Controle de Versão:** Git & GitHub
* **Ambiente Virtual:** `venv`


## Como Configurar e Rodar o Projeto

Siga os passos abaixo para configurar e executar o bot localmente:

1.  **Clonar o Repositório:**
    ```bash
    git clone https://github.com/JohnnyPassos/furia_chatbot.git
    cd furia_chatbot
    ```

2.  **Criar e Ativar Ambiente Virtual:**
    ```bash
    # Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows (cmd/powershell)
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Instalar Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Criar Arquivo `.env`:**
    * Crie um arquivo chamado `.env` na pasta raiz do projeto (no mesmo nível que `main.py`).
    * Adicione a seguinte linha dentro dele, substituindo `SEU_TOKEN_OBTIDO_NO_BOTFATHER` pelo token **real** do seu bot que você obteve via @BotFather:
      ```dotenv
      TELEGRAM_BOT_TOKEN=SEU_TOKEN_OBTIDO_NO_BOTFATHER
      ```
    * **Importante:** Este arquivo `.env` com seu token real **nunca** deve ser enviado para o GitHub. O `.gitignore` do projeto já está configurado para evitar isso.

5.  **(Recomendado) Atualizar Dados Estáticos:**
    * As informações de jogos, elenco, ranking e notícias são definidas como variáveis no arquivo `bot/data/static_info.py`.
    * Antes de rodar, é recomendado verificar e atualizar manualmente essas informações buscando dados recentes em fontes como HLTV.org, Liquipedia, Draft5, etc.

6.  **Executar o Bot:**
    ```bash
    python main.py
    ```
    * O bot iniciará e começará a escutar por mensagens no Telegram. Use `Ctrl + C` no terminal para pará-lo.

## Observações / Limitações

* Os dados de jogos, elenco, ranking e notícias são **estáticos** e baseados na última atualização manual feita pelo desenvolvedor (última atualização em: **02/05/2025**). Para informações 100% em tempo real, consulte as fontes nos `/links`.
* Este bot foi desenvolvido como um exercício para um processo seletivo e não é um produto oficial da FURIA Esports.

## Autor

* **Johnny Passos Galdino**
* **https://github.com/JohnnyPassos**
* **https://www.linkedin.com/in/johnny-passos-1aa06359/**