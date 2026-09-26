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

## Atualizar vagas

Em `recruitment.html`, cada vaga é uma linha `<tr>` da tabela `.positions`.
Para uma vaga aberta usa `<span class="pill open">GL</span>`; para cheia `<span class="pill full">Full</span>`.
Lembra-te de atualizar também as "pills" em `teams.html`.

## Publicar grátis (GitHub Pages)

No GitHub: **Settings → Pages → Source: Deploy from a branch → escolher o branch e a pasta `/ (root)`**.
O site fica em `https://<utilizador>.github.io/Site-DAGR/`.
