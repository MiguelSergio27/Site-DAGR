# D.A.G.R. Company — site

Site do grupo milsim **D.A.G.R. (Direct Assault Ground Ranger Company)** de Arma Reforger.
HTML + CSS + JS puros, sem build — basta abrir `index.html` no navegador.

## Páginas

| Ficheiro | Conteúdo |
|---|---|
| `index.html` | Home — abertura animada, hero, números, resumo das equipas |
| `about.html` | Quem somos, fundador (SWEEP) e comando |
| `teams.html` | HITMAN, WHIPLASH, ANVIL, PROPHET + DISCIPLE |
| `handbook.html` | Standards, code of conduct e progressão (Aspirant → Leader) |
| `recruitment.html` | Vagas abertas (com filtro), passos, requisitos e Discord |
| `gallery.html` | Galeria com visualizador em ecrã inteiro |

## Estrutura

- `css/style.css` — todo o estilo e animações (cores no topo, em `:root`)
- `js/main.js` — menu móvel, abertura, animações de scroll, filtro de vagas, galeria
- `fonts/` — Anton + IBM Plex Mono (locais, licença OFL)
- `video/` — vídeo de abertura "Death walks beside us" (MP4 + WebM, 1080p e 720p para telemóvel). Toca uma vez por sessão na Home.
- `imagens/` — fotos originais; `imagens/cortes/` — fotos recortadas dos cartazes sem texto
- `wireframe/` — protótipo aprovado (referência)

## Atualizar o roster e as vagas

As páginas são geradas por `tools/build.py`. Os dados do roster (quem está em cada vaga,
vagas abertas, aspirantes, comando) estão todos em **`tools/roster.py`**.

1. Edita `tools/roster.py` (ex: trocar `OPEN` pelo nome do jogador e a patente `L/V/R/F`).
2. Corre `python3 tools/build.py`.
3. O estado das vagas (Slots available / Full) no Recruitment e no Teams fica atualizado.

Não edites os `.html` à mão — são reescritos pelo `build.py`.

## Publicar grátis (GitHub Pages)

No GitHub: **Settings → Pages → Source: Deploy from a branch → escolher o branch e a pasta `/ (root)`**.
O site fica em `https://<utilizador>.github.io/Site-DAGR/`.
