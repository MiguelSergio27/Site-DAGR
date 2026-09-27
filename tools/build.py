import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import roster as RS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISCORD = "https://discord.gg/gJeGaH4au"
DISCORD_TXT = "discord.gg/gJeGaH4au"

CUR = ' aria-current="page"'
NAV = [("index.html", "Home"), ("about.html", "About"), ("teams.html", "Teams"),
       ("handbook.html", "Handbook"), ("recruitment.html", "Recruitment"), ("gallery.html", "Gallery")]


def status_pill(status):
    """Só mostra se ainda há vagas ou se está cheio (sem listar funções)."""
    if status == "open":
        return '<span class="pill open">Slots available</span>'
    return '<span class="pill full">Full</span>'


def squad_fact(unit, name):
    sq = dict(unit["squads"])[name]
    lead = next((x[1] for x in sq["groups"][0][1] if x[0] == "LEAD"), None)
    code = sq["code"].split(" // ")[0]
    return (f'<li><span class="k">{name}</span><span>{code} · lead {lead or "open"}<br>'
            f'{status_pill(RS.status_of(RS.squad_open(sq)))}</span></li>')


def group_fact(unit, title, label=None, text=None):
    slots = dict(unit["groups"])[title]
    return (f'<li><span class="k">{label or title}</span><span>{text + "<br>" if text else ""}'
            f'{status_pill(RS.status_of(RS.slots_open(slots)))}</span></li>')



def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#121210">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="imagens/cortes/hero-colina.webp">
<link rel="icon" type="image/png" href="imagens/logo-escudo.png">
<link rel="preload" href="fonts/anton-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
<script>document.documentElement.classList.add("js");</script>
</head>
<body>
"""


def header(active):
    items = "\n".join(
        f'        <li><a href="{h}"{CUR if h == active else ""}>{t}</a></li>'
        for h, t in NAV)
    return f"""<div class="flag"></div>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="D.A.G.R. Company — home">
      <img src="imagens/logo-escudo.png" alt="" width="38" height="48">
      <span>D.A.G.R. CO.</span>
    </a>
    <nav aria-label="Main">
      <ul class="nav-links" id="nav-links">
{items}
        <li class="mobile-join"><a class="btn" href="recruitment.html#apply">Join the company</a></li>
      </ul>
    </nav>
    <a class="btn join" href="recruitment.html#apply">Join</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links">☰ MENU</button>
  </div>
</header>
<main>
"""


def footer():
    items = "\n".join(f'          <li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""</main>

<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="brand" href="index.html"><img src="imagens/logo-escudo.png" alt="" width="38" height="48"><span>D.A.G.R. COMPANY</span></a>
      <div class="motto">Death walks<br><span class="y">beside us</span></div>
      <p class="caps muted" style="margin-top:14px">Смерть іде поруч з нами</p>
    </div>
    <div>
      <h4>// Navigate</h4>
      <ul>
{items}
      </ul>
    </div>
    <div>
      <h4>// Join</h4>
      <ul>
        <li><a href="{DISCORD}" target="_blank" rel="noopener">{DISCORD_TXT}</a></li>
        <li><a href="recruitment.html#positions">Open positions</a></li>
        <li><a href="handbook.html">Member handbook</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© <span data-year>2026</span> D.A.G.R. Company · Direct Assault Ground Ranger Company</span>
    <span>Arma Reforger milsim community · not affiliated with Bohemia Interactive</span>
  </div>
  <div class="flag"></div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""


def cta_band():
    return f"""
<section class="cta-band">
  <div class="container">
    <h2>No one<br>fights alone.</h2>
    <div class="btn-row" style="margin-top:0">
      <a class="btn dark" href="recruitment.html">Apply now</a>
    </div>
  </div>
</section>
"""


TEAMS_CARDS = """
    <div class="grid g4">
      <a class="team-card reveal" href="teams.html#hitman">
        <div class="img"><img src="imagens/cortes/team-hitman.webp" alt="HITMAN operators clearing a building" loading="lazy"></div>
        <div class="body">
          <p class="caps role">SSO Assault Force</p>
          <h3>Hitman</h3>
          <p class="motto">First through the door.</p>
          <p>Three squads — VANGUARD, BANDIT and COBRA — two fireteams each.</p>
          <span class="more">Meet Hitman</span>
        </div>
      </a>
      <a class="team-card reveal" href="teams.html#whiplash">
        <div class="img"><img src="imagens/cortes/team-whiplash.webp" alt="WHIPLASH recon team staging at night" loading="lazy"></div>
        <div class="body">
          <p class="caps role">SSO Recon // Sabotage</p>
          <h3>Whiplash</h3>
          <p class="motto">Small team. Big responsibilities.</p>
          <p>About six operators. Recon, sabotage and forward observation.</p>
          <span class="more">Meet Whiplash</span>
        </div>
      </a>
      <a class="team-card reveal" href="teams.html#anvil">
        <div class="img"><img src="imagens/cortes/team-anvil-veh.webp" alt="ANVIL tank crew resting on their vehicle" loading="lazy"></div>
        <div class="body">
          <p class="caps role">Support &amp; Logistics</p>
          <h3>Anvil</h3>
          <p class="motto">Drive it. Gun it. Crew it.</p>
          <p>Vehicles, firepower — artillery and drones — and logistics.</p>
          <span class="more">Meet Anvil</span>
        </div>
      </a>
      <a class="team-card reveal" href="teams.html#prophet">
        <div class="img"><img src="imagens/cortes/team-prophet.webp" alt="Medic treating a casualty under fire" loading="lazy"></div>
        <div class="body">
          <p class="caps role">Medical + CSAR</p>
          <h3>Prophet + Disciple</h3>
          <p class="motto">Keep them in the fight.</p>
          <p>Medical platoon plus combat search &amp; rescue.</p>
          <span class="more">Meet Prophet + Disciple</span>
        </div>
      </a>
    </div>
"""

# ------------------------------------------------------------------ HOME
home = head("D.A.G.R. Company — Arma Reforger Milsim",
            "D.A.G.R. — Direct Assault Ground Ranger Company. An Arma Reforger milsim unit. Death walks beside us.") + """
<div class="intro" aria-hidden="true">
  <video class="intro-video" muted playsinline preload="auto" poster="video/intro-poster.webp"></video>
  <div class="intro-alt">
    <img src="imagens/logo-escudo.png" alt="">
    <div class="t"><span>D.A.G.R. Company</span></div>
    <div class="bar"></div>
    <div class="m">Death walks beside us</div>
  </div>
  <div class="intro-bar"><span></span></div>
  <button class="intro-skip" type="button">Skip intro ›</button>
</div>
""" + header("index.html") + f"""
<section class="hero">
  <div class="hero-media">
    <img src="imagens/cortes/hero-colina.webp" alt="D.A.G.R. squad advancing up a hill at dusk" fetchpriority="high">
  </div>
  <div class="container hero-content stagger">
    <p class="eyebrow">// Direct Assault Ground Ranger Company</p>
    <h1>D.A.G.R.<br><span class="y">Company</span></h1>
    <p class="motto">Death walks beside us &nbsp;//&nbsp; Arma Reforger</p>
    <p class="lead">A milsim company built on real structure, real training and a team you can count on. Four teams. One fight.</p>
    <div class="btn-row">
      <a class="btn" href="recruitment.html">Apply now</a>
      <a class="btn ghost" href="teams.html">Meet the teams</a>
    </div>
  </div>
  <span class="scroll-cue" aria-hidden="true"></span>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker-track">
    <span>Arma Reforger</span><span>All experience levels welcome</span><span>NA · EU · and more</span><span>Private training server</span><span>Death walks beside us</span>
    <span>Arma Reforger</span><span>All experience levels welcome</span><span>NA · EU · and more</span><span>Private training server</span><span>Death walks beside us</span>
  </div>
</div>

<div class="stats">
  <div class="stat"><div class="n" data-count="4">4</div><div class="l caps muted">Teams</div></div>
  <div class="stat"><div class="n" data-count="18" data-suffix="+">18+</div><div class="l caps muted">Mic required</div></div>
  <div class="stat"><div class="n">2–3</div><div class="l caps muted">Days a week</div></div>
  <div class="stat"><div class="n">PC</div><div class="l caps muted">Preferred · console OK</div></div>
</div>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">// Who we are</p>
      <h2>One company.<br><span class="y">Many fronts.</span></h2>
      <p class="lead">D.A.G.R. is an Arma Reforger milsim unit. We fight on multiple fronts and run training events on our own private server, with members across NA, EU and beyond.</p>
      <p class="lead">Assault, recon, support and medical rotate together. Everyone has a role, everyone knows the chain, and nobody fights alone.</p>
      <div class="btn-row"><a class="btn ghost" href="about.html">About the company</a></div>
    </div>
    <div class="frame reveal" style="aspect-ratio:16/10">
      <img src="imagens/foto-grupo-donetsk.webp" alt="D.A.G.R. members posing for a group photo" loading="lazy">
      <span class="caption">The company</span>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">// The teams</p>
      <h2>Four teams.<br><span class="y">One company.</span></h2>
    </div>
{TEAMS_CARDS}
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="frame reveal" style="aspect-ratio:16/9">
      <img src="imagens/cortes/recruit-earn.webp" alt="A new member receiving his certificate" loading="lazy">
      <span class="caption">This could be you</span>
    </div>
    <div class="reveal">
      <p class="eyebrow">// Join the company</p>
      <h2>Earn your <span class="y">place.</span></h2>
      <p class="lead">Nobody is handed a spot in D.A.G.R. You train for it, you earn it, and the whole company stands up when you do.</p>
      <div class="btn-row">
        <a class="btn" href="recruitment.html">See open positions</a>
        <a class="btn ghost" href="handbook.html">Read the handbook</a>
      </div>
    </div>
  </div>
</section>
""" + cta_band() + footer()

# ------------------------------------------------------------------ ABOUT
about = head("About — D.A.G.R. Company",
             "Who we are, our founder SWEEP and the D.A.G.R. command.") + header("about.html") + f"""
<section class="page-hero">
  <div class="bg"><img src="imagens/banner-death-walks.webp" alt=""></div>
  <div class="container stagger">
    <p class="eyebrow">// About</p>
    <h1>Death walks<br><span class="y">beside us.</span></h1>
    <p class="lead">Direct Assault Ground Ranger Company — an Arma Reforger milsim unit built on structure, training and trust.</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">// Who we are</p>
      <h2>One company.<br><span class="y">Many fronts.</span></h2>
      <p class="lead">D.A.G.R. fights on multiple fronts and runs training events on our own private server. Our members play across NA, EU and beyond — and they all answer to the same chain.</p>
      <p class="lead">We are not a pub squad. Every operator declares a primary and a secondary role, trains for both and earns their tier through action. Assault, recon, support and medical rotate together as one company.</p>
    </div>
    <div class="grid" style="gap:12px">
      <div class="frame reveal" style="aspect-ratio:16/9"><img src="imagens/bunker-escudo.webp" alt="Squad in a bunker in front of the painted D.A.G.R. shield" loading="lazy"></div>
      <div class="grid g2 reveal" style="gap:12px">
        <img src="imagens/equipa-emblema.webp" alt="Four operators with the D.A.G.R. roundel" loading="lazy" style="aspect-ratio:16/10;object-fit:cover;width:100%">
        <img src="imagens/equipa-mrap.webp" alt="Squad lined up in front of an MRAP" loading="lazy" style="aspect-ratio:16/10;object-fit:cover;width:100%">
      </div>
    </div>
  </div>
</section>

<section class="section alt" id="founder">
  <div class="container founder">
    <div class="founder-badge reveal">
      <img src="imagens/logo-escudo.png" alt="D.A.G.R. Co. shield">
      <div class="cs">SWEEP</div>
    </div>
    <div class="reveal">
      <p class="eyebrow">// The founder</p>
      <h2>Sweep</h2>
      <p class="lead">SWEEP is the founder of D.A.G.R. Company.</p>
    </div>
  </div>
</section>

<section class="section" id="command">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">// Command</p>
      <h2>Who to ask</h2>
    </div>
    <div class="grid g4">
      <div class="cmd-card lead-card reveal"><h3>Sweep</h3><p class="caps">07 · Commander / Founder</p><p>Full command of every unit.</p></div>
      <div class="cmd-card reveal"><h3>Growbigger</h3><p class="caps">06 · Lead Cadre // Head Admin</p><p>Training, standards and admin. Cadre FRO$TY works under him.</p></div>
      <div class="cmd-card reveal"><h3>Storm241</h3><p class="caps">05 · Operations Manager</p><p>SSO Recon leader. Runs WHIPLASH selection.</p></div>
      <div class="cmd-card reveal"><h3>CainFPS · Dexter</h3><p class="caps">Anvil · Prophet + Disciple</p><p>Lead the support and medical elements.</p></div>
    </div>
    <p style="margin-top:32px;font-weight:700">Problem? Tell your team leader, or contact <span class="y">GROWBIGGER</span> or <span class="y">SWEEP</span>.</p>
  </div>
</section>
""" + cta_band() + footer()

# ------------------------------------------------------------------ TEAMS
teams = head("Teams — D.A.G.R. Company",
             "HITMAN, WHIPLASH, ANVIL and PROPHET + DISCIPLE — the four teams of D.A.G.R. Company.") + header("teams.html") + f"""
<section class="page-hero">
  <div class="bg"><img src="imagens/ruinas-equipa.webp" alt=""></div>
  <div class="container stagger">
    <p class="eyebrow">// The teams</p>
    <h1>Four teams.<br><span class="y">One company.</span></h1>
    <p class="lead">Assault, recon, support and medical — all rotating together, with a second platoon in reserve. Find where you fit.</p>
  </div>
</section>

<div class="container">
  <article class="team-block" id="hitman">
    <div class="frame team-media reveal"><img src="imagens/cortes/team-hitman.webp" alt="HITMAN operators clearing a building" loading="lazy"></div>
    <div class="reveal">
      <p class="eyebrow">// SSO Assault Force // 1st Platoon</p>
      <h2>Hitman</h2>
      <p class="tagline">First through the door.<br><span class="y">The tip of the spear.</span></p>
      <ul class="facts">
        <li><span class="k">Structure</span><span>Three squads, one assault force. Each squad runs an ALPHA and a BRAVO fireteam.</span></li>
        {squad_fact(RS.HITMAN, "Vanguard")}
        {squad_fact(RS.HITMAN, "Bandit")}
        {squad_fact(RS.HITMAN, "Cobra")}
        <li><span class="k">Selection</span><span>SWEEP</span></li>
      </ul>
    </div>
  </article>

  <article class="team-block" id="whiplash">
    <div class="frame team-media reveal"><img src="imagens/cortes/team-whiplash.webp" alt="WHIPLASH recon team staging at night" loading="lazy"></div>
    <div class="reveal">
      <p class="eyebrow">// SSO Recon // Sabotage</p>
      <h2>Whiplash</h2>
      <p class="tagline">Small team.<br><span class="y">Big responsibilities.</span></p>
      <ul class="facts">
        <li><span class="k">Size</span><span>Small by design. By selection only.</span></li>
        {group_fact(RS.WHIPLASH, None, "Status")}
        <li><span class="k">Selection</span><span>STORM241 chooses who joins.</span></li>
      </ul>
    </div>
  </article>

  <article class="team-block" id="anvil">
    <div class="frame team-media reveal"><img src="imagens/cortes/team-anvil-drone.webp" alt="ANVIL drone pilots at work" loading="lazy"></div>
    <div class="reveal">
      <p class="eyebrow">// Support &amp; Logistics</p>
      <h2>Anvil</h2>
      <p class="tagline">Eyes in the sky. Drive it. Gun it.<br><span class="y">We train you.</span></p>
      <ul class="facts">
        <li><span class="k">Mission</span><span>Vehicles, firepower (artillery, drones) and logistics.</span></li>
        {group_fact(RS.ANVIL, None, "HQ", "Led by CAINFPS · radio &amp; comms.")}
        {group_fact(RS.ANVIL, "Vehicle crew", None, "Commander · driver · gunner.")}
        {group_fact(RS.ANVIL, "Artillery", None, "Fire support.")}
        {group_fact(RS.ANVIL, "Drones", None, "Fly recon &amp; strike drones.")}
        <li><span class="k">Selection</span><span>CAINFPS · team-oriented players with strong, concise comms. Training offered.</span></li>
      </ul>
    </div>
  </article>

  <article class="team-block" id="prophet">
    <div class="frame team-media reveal"><img src="imagens/cortes/team-prophet.webp" alt="Medic treating a casualty under fire" loading="lazy"></div>
    <div class="reveal">
      <p class="eyebrow">// Medical + Combat Search &amp; Rescue</p>
      <h2>Prophet + Disciple</h2>
      <p class="tagline">Keep them in the fight.<br><span class="y">Bring them home.</span></p>
      <ul class="facts">
        <li><span class="k">Prophet</span><span>Medical platoon.</span></li>
        <li><span class="k">Disciple</span><span>Combat search &amp; rescue.</span></li>
        <li><span class="k">We want</span><span>Medics · rescue operators</span></li>
        <li><span class="k">Lead</span><span>Co-led by DEXTER — seeking a co-leader.</span></li>
        <li><span class="k">Status</span><span>{status_pill(RS.status_of(RS.open_count(RS.PROPHET)))}</span></li>
      </ul>
    </div>
  </article>

  <article class="team-block" id="bulwark">
    <div class="frame team-media reveal"><img src="imagens/equipa-mrap.webp" alt="Squad lined up in front of an MRAP" loading="lazy"></div>
    <div class="reveal">
      <p class="eyebrow">// Second Platoon // Reserve</p>
      <h2>Bulwark</h2>
      <p class="tagline">The next line.<br><span class="y">Built from the reserve.</span></p>
      <ul class="facts">
        <li><span class="k">Structure</span><span>Second platoon under SWEEP. Three squads — BASTION, RAMPART and CITADEL — each with an ALPHA and a BRAVO fireteam.</span></li>
        {squad_fact(RS.BULWARK, "Bastion")}
        {squad_fact(RS.BULWARK, "Rampart")}
        {squad_fact(RS.BULWARK, "Citadel")}
        <li><span class="k">Reserve</span><span>Standby players on the reserve list feed BULWARK as slots open.</span></li>
      </ul>
    </div>
  </article>
</div>
""" + cta_band() + footer()

# ------------------------------------------------------------------ HANDBOOK
standards = [
    ("Know your role", "Declare a primary and a secondary. Become proficient with both."),
    ("Follow the chain", "Orders come from your team leader. Leaders answer to Command."),
    ("Keep comms clean", "Short, clear, on the net. Say what matters and get off."),
    ("Show up ready", "Aim for 2 to 3 days a week. Share your availability and timezone."),
    ("One company", "Your team serves the fight. Remember the mission."),
    ("Earn your tier", "FNG, Regular, Veteran, Leader. Promotions are earned through action."),
]
conduct = [
    ("Respect everyone", "No harassment, hate or slurs. Disagree without the drama."),
    ("Play clean", "No cheats, exploits or griefing. Ever."),
    ("Mission first on comms", "Keep the net clear. Save banter for downtime."),
    ("Take issues to leaders", "Tell your team leader. About a leader? Contact GROWBIGGER or SWEEP."),
    ("Be honest", "Give real availability and real quals. Own your mistakes."),
    ("Help the new guys", "Everyone was an FNG once. Teach, do not gatekeep."),
]


def rules(lst):
    return "\n".join(
        f'        <div class="rule"><span class="num">{i+1:02d}</span><div><b>{t}</b><p>{d}</p></div></div>'
        for i, (t, d) in enumerate(lst))


handbook = head("Member Handbook — D.A.G.R. Company",
                "Standards, code of conduct and the path from Aspirant to Leader in D.A.G.R. Company.") + header("handbook.html") + f"""
<div class="paper">
<section class="section" style="padding-bottom:40px">
  <div class="container stagger">
    <p class="eyebrow">// Member handbook</p>
    <h1 style="font-size:clamp(52px,9vw,120px)">Standards<br>&amp; conduct</h1>
    <p class="lead">What we expect from every member of D.A.G.R. — and what you can expect from us.</p>
    <div class="req-band" style="margin-top:36px">18+ · Microphone · PC preferred, console OK · 2–3 days a week</div>
  </div>
</section>

<section class="section" id="rules" style="padding-top:40px">
  <div class="container grid g2" style="gap:56px">
    <div class="rules-col reveal">
      <h3>// Standards</h3>
{rules(standards)}
    </div>
    <div class="rules-col reveal">
      <h3>// Code of conduct</h3>
{rules(conduct)}
    </div>
  </div>
  <div class="container"><div class="big-line reveal">Respect is not optional.</div></div>
</section>

<section class="section" id="path">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">// The path</p>
      <h2>Earn your tier</h2>
      <p class="lead">Nobody is handed a spot. Every promotion is earned through action.</p>
    </div>
    <div class="path reveal">
      <div class="path-step"><div class="ico">▶</div><b>ASPIRANT</b><span>1–3 weeks, 2 sponsors</span></div>
      <div class="path-step"><div class="ico">○</div><b>FNG</b><span>Learning how we roll</span></div>
      <div class="path-step"><div class="ico">◇</div><b>REGULAR</b><span>Trusted in your role</span></div>
      <div class="path-step"><div class="ico">◆</div><b>VETERAN</b><span>Proven over time</span></div>
      <div class="path-step star"><div class="ico">★</div><b>LEADER</b><span>Leads a team or element</span></div>
    </div>
  </div>
</section>

<section class="section" id="structure">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">// Structure &amp; contacts</p>
      <h2>The teams</h2>
    </div>
    <div class="reveal">
      <div class="rule" style="grid-template-columns:minmax(200px,1fr) 2fr"><h3 style="font-size:36px">Hitman</h3><p>SSO assault force. VANGUARD, BANDIT and COBRA, two fireteams each.</p></div>
      <div class="rule" style="grid-template-columns:minmax(200px,1fr) 2fr"><h3 style="font-size:36px">Whiplash</h3><p>SSO recon and sabotage. Small team, selected by STORM241.</p></div>
      <div class="rule" style="grid-template-columns:minmax(200px,1fr) 2fr"><h3 style="font-size:36px">Anvil</h3><p>Support and logistics. Vehicles, firepower (artillery, drones) and logistics. Led by CAINFPS.</p></div>
      <div class="rule" style="grid-template-columns:minmax(200px,1fr) 2fr"><h3 style="font-size:36px">Prophet + Disciple</h3><p>Medical platoon plus combat search and rescue. Co-led by DEXTER.</p></div>
      <div class="rule" style="grid-template-columns:minmax(200px,1fr) 2fr"><h3 style="font-size:36px">Bulwark</h3><p>Second platoon, in reserve under SWEEP. BASTION, RAMPART and CITADEL, fed by the reserve list.</p></div>
    </div>
    <p style="margin-top:36px;font-weight:700">Problem? Tell your team leader, or contact GROWBIGGER or SWEEP.</p>
  </div>
</section>
</div>
""" + cta_band() + footer()

# ------------------------------------------------------------------ RECRUITMENT
positions = RS.positions()
UNIT_STATUS = " · ".join(
    f"{u['name'].upper()} <b class='{'y' if RS.open_count(u) else 'muted'}'>{'OPEN' if RS.open_count(u) else 'FULL'}</b>"
    for u in RS.ALL_UNITS)


def role_key():
    return RS.role_key_html()


def pos_rows():
    out = []
    for team, status, name, el, sub, sel in positions:
        pills = status_pill(status)
        out.append(f"""        <tr data-team="{team}" data-status="{status}">
          <td class="team" data-label="Team">{name}</td>
          <td data-label="Element">{el}<span class="sub">{sub}</span></td>
          <td data-label="Status">{pills}</td>
          <td data-label="Selection">{sel}</td>
        </tr>""")
    return "\n".join(out)


recruit = head("Recruitment — D.A.G.R. Company",
               "D.A.G.R. Company is recruiting. Open positions in assault, recon, vehicles, drones and medical. Apply in Discord.") + header("recruitment.html") + f"""
<section class="recruit-hero">
  <div class="bg"><img src="imagens/cortes/recruit-nofa.webp" alt="Squad dismounting from an armoured vehicle under fire"></div>
  <div class="container stagger">
    <span class="tag-box">RECRUITMENT</span>
    <p class="eyebrow">// D.A.G.R. Company is recruiting</p>
    <h1>No one<br>fights alone</h1>
    <p class="lead">Assault, recon, support and medical — one company, four teams, all rotating together. Real structure. Real training. Real team you can count on.</p>
    <div class="btn-row">
      <a class="btn" href="#apply">Apply in Discord</a>
      <a class="btn ghost" href="#positions">Open positions</a>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker-track">
    <span>Apply now</span><span>Arma Reforger</span><span>All experience levels welcome</span><span>New players enter as Aspirants</span>
    <span>Apply now</span><span>Arma Reforger</span><span>All experience levels welcome</span><span>New players enter as Aspirants</span>
  </div>
</div>

<section class="section" id="positions">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">// Open now</p>
      <h2>Open positions</h2>
    </div>
    <div class="open-summary reveal">
      <div class="big"><span class="n">{RS.TARGET}</span><span class="caps">Target player base</span></div>
      <div>
        <p>{UNIT_STATUS}</p>
        <p class="muted">Slots are still open. Interested? Message SWEEP or GROWBIGGER on Discord.</p>
      </div>
    </div>
    <div class="filters" role="group" aria-label="Filter positions">
      <button data-filter="all" aria-pressed="true">All</button>
      <button data-filter="open" aria-pressed="false">Open only</button>
      <button data-filter="hitman" aria-pressed="false">Hitman</button>
      <button data-filter="whiplash" aria-pressed="false">Whiplash</button>
      <button data-filter="anvil" aria-pressed="false">Anvil</button>
      <button data-filter="prophet" aria-pressed="false">Prophet + Disciple</button>
      <button data-filter="bulwark" aria-pressed="false">Bulwark</button>
    </div>
    <table class="positions">
      <thead><tr><th>Team</th><th>Element</th><th>Status</th><th>Selection</th></tr></thead>
      <tbody>
{pos_rows()}
      </tbody>
    </table>
  </div>
</section>

<section class="section tight" id="roles">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">// Role key</p>
      <h2>Know the <span class="y">roles.</span></h2>
      <p class="lead">Every slot on the roster uses these codes. New roles are marked in yellow.</p>
    </div>
    <div class="role-key">
{role_key()}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">// Join the company</p>
      <h2>Earn your <span class="y">place.</span></h2>
      <p class="lead">Nobody is handed a spot in D.A.G.R. You train for it, you earn it, and the whole company stands up when you do.</p>
    </div>
    <div class="frame reveal" style="aspect-ratio:3/1"><img src="imagens/cortes/recruit-earn.webp" alt="A new member receiving his certificate" loading="lazy"></div>
  </div>
  <div class="container" style="margin-top:56px">
    <div class="steps">
      <div class="reveal"><div class="n">01</div><b>APPLY</b><p>Join the Discord and apply for the team you want. New players enter as Aspirants.</p></div>
      <div class="reveal"><div class="n">02</div><b>TRAIN</b><p>1–3 weeks with two sponsors. Learn our comms, how we roll and your role.</p></div>
      <div class="reveal"><div class="n">03</div><b>GRADUATE</b><p>Earn your FNG tier and take your place in the company.</p></div>
    </div>
  </div>
</section>

<section class="section tight">
  <div class="container">
    <p class="eyebrow">// Requirements</p>
    <div class="req-list reveal">
      <div><div class="n" data-count="18" data-suffix="+">18+</div><div class="l">Age</div></div>
      <div><div class="n">MIC</div><div class="l">Required</div></div>
      <div><div class="n">PC</div><div class="l">Preferred · console OK</div></div>
      <div><div class="n">2–3</div><div class="l">Days a week</div></div>
    </div>
  </div>
</section>

<section class="section" id="apply">
  <div class="container">
    <div class="reply-box reveal">
      <div>
        <p class="eyebrow">// How to reply</p>
        <h3>Post in the role selection channel</h3>
        <p class="muted" style="font-size:14px;margin:12px 0 0">Copy this format, fill it in and post it in <b>#role-selection</b> on Discord.</p>
        <button class="copy-btn light" data-copy="CALLSIGN:&#10;PRIMARY:&#10;SECONDARY:&#10;UNIT (optional):&#10;QUALS:&#10;AVAILABILITY (with timezone):">Copy format</button>
      </div>
      <pre class="reply-format">CALLSIGN:
PRIMARY:
SECONDARY:
UNIT (optional):
QUALS:
AVAILABILITY (with timezone):</pre>
    </div>
    <div class="cta-box reveal">
      <div>
        <p class="label">Apply in Discord</p>
        <a class="link" href="{DISCORD}" target="_blank" rel="noopener">{DISCORD_TXT}</a>
        <p class="small">New players enter as Aspirants · already a member? use #role-selection</p>
      </div>
      <div class="actions">
        <a class="btn dark" href="{DISCORD}" target="_blank" rel="noopener">Open Discord</a>
        <button class="copy-btn" data-copy="{DISCORD}">Copy link</button>
      </div>
    </div>
  </div>
</section>
""" + footer()

# ------------------------------------------------------------------ GALLERY
gal = [
    ("banner-death-walks.webp", "D.A.G.R. — Death walks beside us", "w2 h2"),
    ("ruinas-equipa.webp", "Squad in the ruins", ""),
    ("visao-noturna-cqb.webp", "CQB through night vision", ""),
    ("foto-grupo-donetsk.webp", "Group photo", "w2"),
    ("assalto-edificio.webp", "Stacked up on a building at sunset", ""),
    ("floresta-nevoeiro.webp", "Patrol in the foggy forest", "h2"),
    ("equipa-mrap.webp", "Squad in front of an MRAP", ""),
    ("trincheira-nevoeiro.webp", "Trenches in the fog", "w2"),
    ("equipa-veiculo-pb.webp", "Squad around the armoured vehicle", ""),
    ("bunker-escudo.webp", "Bunker with the D.A.G.R. shield", ""),
    ("equipa-escudo-cidade.webp", "In the city", "w2"),
    ("equipa-emblema.webp", "Fireteam with the roundel", ""),
    ("company-poster.webp", "D.A.G.R. Company", ""),
    ("cortes/hero-colina.webp", "Advancing at dusk", "w2"),
    ("cortes/team-hitman.webp", "HITMAN clearing a building", ""),
    ("cortes/team-anvil-veh.webp", "ANVIL tank crew", ""),
    ("cortes/team-prophet.webp", "Care under fire", ""),
    ("cortes/team-whiplash.webp", "WHIPLASH night staging", "w2"),
]
gal_html = "\n".join(
    f'      <button class="{c}" data-full="imagens/{f}"><img src="imagens/{f}" alt="{a}" loading="lazy"></button>'
    for f, a, c in gal)

gallery = head("Gallery — D.A.G.R. Company",
               "Field photos from D.A.G.R. Company operations in Arma Reforger.") + header("gallery.html") + f"""
<section class="page-hero">
  <div class="bg"><img src="imagens/floresta-nevoeiro.webp" alt=""></div>
  <div class="container stagger">
    <p class="eyebrow">// Field photos</p>
    <h1>Gallery</h1>
    <p class="lead">Moments from our operations and training. Click any photo to view it full screen.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="gallery">
{gal_html}
    </div>
  </div>
</section>

<div class="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer">
  <button class="lb-close" aria-label="Close">✕</button>
  <button class="lb-prev" aria-label="Previous photo">←</button>
  <img src="" alt="">
  <button class="lb-next" aria-label="Next photo">→</button>
  <div class="lb-count"></div>
</div>
""" + cta_band() + footer()

for name, html in [("index.html", home), ("about.html", about), ("teams.html", teams),
                   ("handbook.html", handbook), ("recruitment.html", recruit), ("gallery.html", gallery)]:
    with open(os.path.join(ROOT, name), "w") as f:
        f.write(html)
    print("wrote", name, len(html))
