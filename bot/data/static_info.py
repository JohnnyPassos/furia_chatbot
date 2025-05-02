# bot/data/static_info.py

"""
Armazena todas as informações estáticas utilizadas pelos handlers do bot.

Este arquivo centraliza os textos para facilitar a manutenção e atualização manual,
especialmente para dados que não possuem fontes dinâmicas (APIs/RSS) confiáveis
e gratuitas no contexto deste projeto (como elenco, ranking, jogos e notícias)."""

# --- Para o comando /proximojogo (Exemplo Estático) ---
PROXIMO_JOGO_INFO = """📅 **Próximo Jogo FURIA CS** 🔥

Ainda estamos aguardando a definição do próximo confronto oficial! Fica ligado! 👀

O próximo grande evento no radar é a **PGL Astana 2025**, começando em **10/05**! 🏆 Vai ser insano!

Assim que tivermos data/hora/adversário confirmados, atualizaremos aqui. Enquanto isso, já salva o link do HLTV pra não perder nada:
🔗 https://www.hltv.org/team/8297/furia#tab-matchesBox

#DIADEFURIA ⚫⚪🐾"""

# --- Para o comando /ultimoresultado (Exemplo Estático) ---
ULTIMO_RESULTADO_INFO = """📊 **Último Resultado FURIA CS:**

😥 Fim de linha na PGL Bucharest 2025... Não deu pra pantera dessa vez.
🗓️ Data: 09/04/2025
🆚 Adversário: The MongolZ 🇲🇳
📉 Placar Final: FURIA 0 vs 2 MongolZ

Seguimos fortes para a próxima! 💪 Para ver os detalhes e stats da partida:
🔗 [Link da página da partida no HLTV - *Substitua pela URL correta!*]

#DIADEFURIA ⚫⚪🐾"""


# --- Para o comando /elenco (Exemplo Estático) ---
ELENCO_ATUAL_INFO = """🐾 **Nosso Esquadrão CS2! (Abr/2025 - Confirmar!)** 🐾

🔥 **Line-up Ativa:**
    🇧🇷 Gabriel "FalleN" Toledo (AWP/IGL)
    🇧🇷 Kaike "KSCERATO" Cerato (Rifler)
    🇧🇷 Yuri "yuurih" Santos (Rifler)
    🇰🇿 Danil "molodoy" Golubenko (Rifler)
    🇱🇻 Mareks "YEKINDAR" Gaļinskis (Rifler - Stand-in Temporário!)

🧑‍🏫 **Coach:**
    🇧🇷 Sidnei "sidde" Macedo

**Banco:** (bench)
    🇧🇷 Marcelo "chelo" Cespedes
    🇧🇷 Felipe "skullz" Medeiros

⚠️ *Lembre-se: O cenário muda rápido! Esta line pode ter alterações. Confira a Liquipedia para o status mais recente:*
🔗 https://liquipedia.net/counterstrike/FURIA"""


# --- Para o comando /ranking (Exemplo Estático) ---
RANKING_INFO = """🏆 **Ranking Atual FURIA CS (Verificar!)** 🏆

📈 **HLTV World Ranking:** #16
   Confira: https://www.hltv.org/ranking/teams

📊 **ESL World Ranking:** #16
   Confira: https://pro.eslgaming.com/worldranking/csgo/
"""


# --- Para o comando /links ---
LINKS_UTEIS = """🔗 **Links Oficiais e Úteis da FURIA:** 🔗

🐦 Twitter: https://twitter.com/furia
📸 Instagram: https://www.instagram.com/furiagg/
📺 Twitch: https://www.twitch.tv/furiatv
🎬 YouTube: https://www.youtube.com/@FURIAggCS
🛒 Loja: https://furia.gg
🎵 TikTok: https://www.tiktok.com/@furiagg
👟 Adidas x Furia: https://adidas.furia.gg/  

📊 **CS Stats/Info:**
HLTV: https://www.hltv.org/team/8297/furia
Liquipedia: https://liquipedia.net/counterstrike/FURIA

Use com sabedoria! 😉"""

# --- Para o comando /noticias (Exemplo Estático) ---
NOTICIAS_RECENTES = """📰 **Últimas Notícias Furia CS** 📰

1. <b><a href="https://www.hltv.org/news/41512/furia-bench-skullz-add-yekindar-as-stand-in">YEKINDAR reforça FURIA como stand-in temporário!</a></b>
   <i>Fonte: HLTV.org | Data: 22/04/2025</i>

2. <b><a href="https://draft5.gg/equipe/330-FURIA/campeonatos">Próximos Desafios: FURIA mira PGL Astana, IEM Dallas e Austin Major</a></b>
   <i>Fonte: Calendário Draft5 | Data: Maio/Junho 2025</i>

3. <b><a href="https://draft5.gg/noticia/fallen-analisa-nova-furia-e-fala-sobre-troca-de-funcao-ainda-posso-atuar-em-alto-nivel">FalleN analisa nova FURIA e fala sobre troca de função: "Ainda posso atuar em alto nível"</a></b>
   <i>Fonte: HLTV.org | Data: 26/04/2025</i>

Clique nos títulos para ler mais! 😉 Para outras fontes, use /links."""