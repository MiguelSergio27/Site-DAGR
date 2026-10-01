"""
D.A.G.R. COMPANY — dados do roster (fonte única).

Para atualizar o site: altera os dados aqui e corre `python3 tools/build.py`.
As páginas Roster, Teams e Recruitment (vagas) são geradas a partir destes dados.

Cada vaga é um tuplo (função, nome, patente):
  - nome None       -> vaga aberta  [ OPEN ]
  - nome "RESERVED" -> reservada
  - patente: "L" leader ★ · "V" veteran ◆ · "R" regular ◇ · "F" FNG ○ · None (sem patente)
Uma vaga pode ter um 4.º elemento com o número de vagas abertas extra (ex: CREW Dunks +4 open).
"""

UPDATED = "Sep 21, 2026"
TARGET = "70–90"

COMMAND = [
    # (número, nome, título, descrição)
    ("06", "GROWBIGGER", "Lead Cadre // Head Admin", "Training, standards and admin. Your contact for any issue."),
    ("07", "SWEEP", "Commander / Founder", "Full command of every unit."),
    ("05", "STORM241", "Operations Manager", "SSO Recon leader. Runs WHIPLASH selection."),
]
CADRE = [("FRO$TY", "Cadre", "Under GROWBIGGER")]

L, V, R, F = "L", "V", "R", "F"
OPEN = None


def squad(code, lead, rto, alpha, bravo, a_name, b_name):
    return {
        "code": code,
        "groups": [
            (None, [("LEAD",) + lead, ("RTO",) + rto]),
            (a_name, alpha),
            (b_name, bravo),
        ],
    }


HITMAN = {
    "id": "hitman", "name": "Hitman", "sub": "SSO Assault Force // 1st Platoon",
    "squads": [
        ("Vanguard", squad("DAGR 1 // Hitman",
                           ("Sweep", L), (OPEN, None),
                           [("TL", "BOYBLUE", L), ("AR", "Witch", None), ("GL", "BLU", None), ("RM", "Spl_sh", V)],
                           [("TL", "KNIGHT", L), ("AT", "Nxxy", V), ("MED", "marbs", V), ("RM", "DOPENATION", R)],
                           "Alpha 1-1", "Bravo 1-2")),
        ("Bandit", squad("DAGR 2 // Hitman",
                         ("Overlord", V), ("GROWBIGGER", L),
                         [("TL", "AXE", V), ("MG", "Gavino", V), ("GL", "Bradz", None), ("RM", "BRAXXY", F)],
                         [("TL", "Snow", None), ("AT", "lando", V), ("MED", "Foo", V), ("RM", "Six", V)],
                         "Alpha 2-1", "Bravo 2-2")),
        ("Cobra", squad("DAGR 3 // Hitman",
                        ("Carrots", R), (OPEN, None),
                        [("TL", "FRO$TY (CADRE)", L), ("AR", "Porky", None), ("GL", "Echo", None), ("RM", "lx.66", V)],
                        [("TL", "Salty", V), ("AT", "strike", None), ("MED", "Apois", None), ("RM", "DayneBPiss", V)],
                        "Alpha 3-1", "Bravo 3-2")),
    ],
}

BULWARK = {
    "id": "bulwark", "name": "Bulwark", "sub": "Second Platoon // Reserve // Under Sweep",
    "squads": [
        (name, squad(f"DAGR {n} // Bulwark",
                     (OPEN, None), (OPEN, None),
                     [("TL", OPEN, None), ("AR", OPEN, None), ("GL", OPEN, None), ("RM", OPEN, None)],
                     [("TL", OPEN, None), ("AT", OPEN, None), ("MED", OPEN, None), ("RM", OPEN, None)],
                     f"Alpha {n}-1", f"Bravo {n}-2"))
        for name, n in (("Bastion", 4), ("Rampart", 5), ("Citadel", 6))
    ],
}

WHIPLASH = {
    "id": "whiplash", "name": "Whiplash", "sub": "SSO Recon // Sabotage · by selection only",
    "groups": [
        (None, [("LDR", "STORM241", L), ("RTO", "Digital_smoke7", R), ("FO", "RESERVED", None),
                ("RCN", "Feezy.eg", V), ("MBR", "Booby", R), ("MBR", "Ski", None), ("MBR", "Piloto", F)]),
    ],
}

ANVIL = {
    "id": "anvil", "name": "Anvil", "sub": "Support & Logistics",
    "groups": [
        (None, [("LDR", "CainFPS", V), ("RTO", OPEN, None)]),
        ("Vehicle crew", [("VC", "Sham", V), ("GNR", "widow", None), ("DRV", OPEN, None), ("CREW", "Dunks", None, 4)]),
        ("Artillery", [("TL", OPEN, None), ("ARTY", "Proxy", None), ("ARTY", OPEN, None), ("ARTY", OPEN, None), ("ARTY", OPEN, None)]),
        ("Drones", [("TL", OPEN, None), ("PLT", "Convey", None), ("PLT", OPEN, None), ("PLT", OPEN, None), ("ASST", OPEN, None)]),
    ],
}

PROPHET = {
    "id": "prophet", "name": "Prophet + Disciple", "sub": "Medical + Combat Search &amp; Rescue",
    "groups": [
        (None, [("LDR", "DEXTER", None), ("CO-LDR", OPEN, None), ("RTO", OPEN, None)]),
        ("Prophet · Medical platoon", [("MED", "RAMBO", None), ("MED", OPEN, None)]),
        ("Disciple · Combat search &amp; rescue", [("CSAR", OPEN, None)]),
    ],
}

RESERVE_SLOTS = 16

ASPIRANTS = [
    "Tickler", "TheKushWizard", "+Red+", "THCloudz", "Hatred",
    "GRXXN", "TwiiSTFAME", "voixdv", "JFSmith09", "UnknownNazzyyy",
    "PastelPanduh", "StarFins", "Hairzyballz", "viper2846", "66",
    "Miltoc", "Aiden", "Treto", "Xavier", "Dankttv",
    "strike",
]

ROLE_KEY = [
    ("LDR", "Leader"), ("TL", "Team Leader"), ("RM", "Rifleman"), ("AR", "Automatic Rifleman"),
    ("GL", "Grenadier"), ("AT", "Anti-Tank"), ("MED", "Medic"), ("RTO", "Radio Operator"),
    ("FO", "Forward Observer"), ("RCN", "Recon"), ("DEM", "Demolitions"), ("DRN", "Drone Operator"),
    ("VC", "Vehicle Commander"), ("DRV", "Driver"), ("GNR", "Gunner"), ("ARTY", "Artillery"),
    ("CSAR", "Search &amp; Rescue"), ("MBR", "Member"),
    ("MG", "Machine Gunner", 1), ("AMG", "MG Assistant", 1), ("HAT", "Heavy AT", 1),
    ("AHAT", "Heavy AT Assistant", 1), ("DMR", "Designated Marksman", 1),
]

TIER_ICON = {"L": "★", "V": "◆", "R": "◇", "F": "○"}
TIER_NAME = {"L": "Leader", "V": "Veteran", "R": "Regular", "F": "FNG"}


# ------------------------------------------------------------------ contagens

def unit_groups(unit):
    """Todos os grupos (título, vagas) de uma unidade, incluindo esquadras."""
    if "squads" in unit:
        for sq_name, sq in unit["squads"]:
            for title, slots in sq["groups"]:
                yield sq_name, title, slots
    else:
        for title, slots in unit["groups"]:
            yield None, title, slots


def open_roles(slots):
    """Lista de funções abertas num grupo, agregadas: ['TL', 'ARTY ×3']."""
    counts = {}
    for s in slots:
        role, name = s[0], s[1]
        n = (1 if name is None else 0) + (s[3] if len(s) > 3 else 0)
        if n:
            counts[role] = counts.get(role, 0) + n
    return [r if c == 1 else f"{r} ×{c}" for r, c in counts.items()]


def open_count(unit):
    total = 0
    for _, _, slots in unit_groups(unit):
        for s in slots:
            total += (1 if s[1] is None else 0) + (s[3] if len(s) > 3 else 0)
    return total


ACTIVE_UNITS = [HITMAN, WHIPLASH, ANVIL, PROPHET]
ALL_UNITS = ACTIVE_UNITS + [BULWARK]


def lead_of(unit_or_squad_groups):
    for s in unit_or_squad_groups[0][1]:
        if s[0] in ("LEAD", "LDR") and s[1]:
            return s[1]
    return None


# ------------------------------------------------------------------ HTML

def slot_html(s):
    role, name, tier = s[0], s[1], s[2]
    extra = s[3] if len(s) > 3 else 0
    if name is None:
        who = '<span class="slot-open">[ OPEN ]</span>'
    elif name == "RESERVED":
        who = '<span class="slot-reserved">Reserved</span>'
    else:
        who = f'<span class="slot-name">{name}</span>'
    if extra:
        who += f' <span class="slot-extra">+{extra} open</span>'
    icon = f'<span class="tier t-{tier}" title="{TIER_NAME[tier]}">{TIER_ICON[tier]}</span>' if tier else ""
    return f'<li><span class="slot-role">{role}</span>{who}{icon}</li>'


def group_html(title, slots):
    head = f'<p class="grp-title">// {title}</p>' if title else ""
    cls = "grp boxed" if title else "grp"
    return f'<div class="{cls}">{head}<ul>{"".join(slot_html(s) for s in slots)}</ul></div>'


def squad_card(name, sq):
    body = "".join(group_html(t, s) for t, s in sq["groups"])
    return (f'<div class="r-card reveal"><div class="r-head"><h3>{name}</h3><p>{sq["code"]}</p></div>'
            f'{body}</div>')


def unit_card(unit):
    body = "".join(group_html(t, s) for t, s in unit["groups"])
    return (f'<div class="r-card reveal" id="r-{unit["id"]}"><div class="r-head"><h3>{unit["name"]}</h3><p>{unit["sub"]}</p></div>'
            f'{body}</div>')


def platoon_html(unit):
    cards = "\n".join(squad_card(n, sq) for n, sq in unit["squads"])
    return (f'<div class="r-platoon" id="r-{unit["id"]}"><div class="r-plhead reveal"><h3>{unit["name"]}</h3>'
            f'<p>{unit["sub"]}</p></div><div class="r-squads">{cards}</div></div>')


def role_key_html():
    out = []
    for r in ROLE_KEY:
        new = len(r) > 2
        out.append(f'<div class="role{" new" if new else ""}"><b>{r[0]}</b><span>{r[1]}</span></div>')
    return "\n".join(out)


# função de cada esquadra (aparece no site em vez do código DAGR e do nome do SL,
# que podem mudar). Troca o texto quando souberes a função certa de cada uma.
SQUAD_ROLE = {
    "Vanguard": "Assault squad",
    "Bandit": "Assault squad",
    "Cobra": "Assault squad",
    "Bastion": "Reserve squad",
    "Rampart": "Reserve squad",
    "Citadel": "Reserve squad",
}

SELECTION = {"hitman": "SWEEP", "whiplash": "STORM241", "anvil": "CAINFPS", "prophet": "DEXTER", "bulwark": "SWEEP"}

# texto fixo de cada elemento na tabela de vagas (não muda quando entra/sai alguém)
ELEMENT_INFO = {
    ("anvil", None): ("HQ", "Leadership &amp; comms"),
    ("anvil", "Vehicle crew"): ("Vehicle crew", "Commander · driver · gunner — training offered"),
    ("anvil", "Artillery"): ("Artillery", "Fire support — training offered"),
    ("anvil", "Drones"): ("Drones", "Fly recon &amp; strike drones — training offered"),
    ("whiplash", None): ("Recon // Sabotage", "Small team · by selection only"),
    ("prophet", None): ("Medical + CSAR", "Medics · rescue operators · seeking co-leader — co-led by DEXTER"),
}


def status_of(n_open):
    """'open' se ainda há vagas, 'full' se está cheio."""
    return "open" if n_open else "full"


def slots_open(slots):
    return sum((1 if s[1] is None else 0) + (s[3] if len(s) > 3 else 0) for s in slots)


def squad_open(sq):
    return sum(slots_open(sl) for _, sl in sq["groups"])


def positions():
    """Linhas da tabela de vagas: (team_id, status, equipa, elemento, detalhe, seleção).
    Só diz se há vagas ('open') ou se está cheio ('full') — sem listar funções."""
    rows = []
    for unit in ALL_UNITS:
        uid = unit["id"]
        if "squads" in unit:
            for sq_name, sq in unit["squads"]:
                detail = SQUAD_ROLE[sq_name]
                rows.append((uid, status_of(squad_open(sq)), unit["name"], sq_name.upper(), detail, SELECTION[uid]))
        elif uid == "anvil":
            for title, slots in unit["groups"]:
                el, detail = ELEMENT_INFO[(uid, title)]
                rows.append((uid, status_of(slots_open(slots)), unit["name"], el, detail, SELECTION[uid]))
        else:
            el, detail = ELEMENT_INFO[(uid, None)]
            rows.append((uid, status_of(open_count(unit)), unit["name"], el, detail, SELECTION[uid]))
    return rows


def merge(roles):
    counts = {}
    for r in roles:
        if " ×" in r:
            k, n = r.split(" ×")
            n = int(n)
        else:
            k, n = r, 1
        counts[k] = counts.get(k, 0) + n
    return [k if n == 1 else f"{k} ×{n}" for k, n in counts.items()]
