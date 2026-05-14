"""Power Rangers – Character Showcase
Reemplaza el archivo por defecto de Reflex
"""

import reflex as rx
from pydantic import BaseModel


# ─────────────────────────────────────────────
# Google Fonts
# ─────────────────────────────────────────────
GFONT_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Permanent+Marker&"
    "family=Rajdhani:wght@400;500;600;700&"
    "family=Cinzel+Decorative:wght@700&"
    "display=swap"
)


# ─────────────────────────────────────────────
# Data models
# ─────────────────────────────────────────────
class ClipData(BaseModel):
    title: str = ""
    duration: str = ""


class RangerData(BaseModel):
    id: str = ""
    name: str = ""
    real_name: str = ""
    role: str = ""
    zord: str = ""
    weapon: str = ""
    affiliation: str = ""
    description: str = ""
    abilities: list[str] = []
    color: str = ""
    bg_from: str = ""
    bg_to: str = ""
    glow: str = ""
    image: str = ""
    clips: list[ClipData] = []


# ─────────────────────────────────────────────
# Imágenes externas
# Puedes cambiarlas luego por imágenes tuyas en assets/
# ─────────────────────────────────────────────
RANGERS_RAW = [
    {
        "id": "red",
        "image": "/Red Ranger.png",
        "name": "Red Ranger",
        "real_name": "Jason Lee Scott",
        "role": "Líder del equipo · Mighty Morphin",
        "zord": "Tyrannosaurus Dinozord",
        "weapon": "Power Sword",
        "affiliation": "Angel Grove Power Rangers",
        "description": (
            "El Red Ranger representa el valor, la fuerza y el liderazgo. Jason Lee Scott fue "
            "elegido por Zordon para dirigir al equipo original de Power Rangers y defender la "
            "Tierra contra Rita Repulsa y Lord Zedd."
        ),
        "abilities": [
            "Power Sword",
            "Martial Arts",
            "Leadership",
            "Tyrannosaurus Dinozord",
            "Megazord Formation",
        ],
        "color": "#E11D48",
        "bg_from": "#230007",
        "bg_to": "#7F1D1D",
        "glow": "rgba(225,29,72,0.65)",
        "clips": [
            {"title": "Jason becomes Red Ranger", "duration": "3:45"},
            {"title": "Red Ranger best fights", "duration": "8:12"},
            {"title": "Tyrannosaurus Dinozord call", "duration": "2:33"},
            {"title": "Power Sword moments", "duration": "5:20"},
        ],
    },
    {
        "id": "green",
        "image": "/Green Ranger.png",
        "name": "Green Ranger",
        "real_name": "Tommy Oliver",
        "role": "Guerrero legendario · Dragon Power",
        "zord": "Dragonzord",
        "weapon": "Dragon Dagger",
        "affiliation": "Angel Grove Power Rangers",
        "description": (
            "Tommy Oliver inició como enemigo bajo el control de Rita Repulsa, pero luego se convirtió "
            "en uno de los Rangers más legendarios. Su Dragon Dagger y el Dragonzord lo hicieron "
            "uno de los personajes más icónicos de la saga."
        ),
        "abilities": [
            "Dragon Dagger",
            "Dragon Shield",
            "Dragonzord",
            "Elite Combat",
            "Green Ranger Power",
        ],
        "color": "#16A34A",
        "bg_from": "#001a0b",
        "bg_to": "#064E3B",
        "glow": "rgba(22,163,74,0.65)",
        "clips": [
            {"title": "Green Ranger first appearance", "duration": "6:15"},
            {"title": "Dragonzord battle", "duration": "4:48"},
            {"title": "Tommy joins the team", "duration": "7:10"},
            {"title": "Dragon Dagger theme", "duration": "2:05"},
        ],
    },
    {
        "id": "blue",
        "image": "/Blue Ranger.png",
        "name": "Blue Ranger",
        "real_name": "Billy Cranston",
        "role": "Genio tecnológico · Estratega",
        "zord": "Triceratops Dinozord",
        "weapon": "Power Lance",
        "affiliation": "Angel Grove Power Rangers",
        "description": (
            "Billy Cranston es el cerebro del equipo. Su inteligencia, conocimiento científico y "
            "capacidad para crear soluciones tecnológicas lo convierten en una pieza esencial en "
            "cada batalla."
        ),
        "abilities": [
            "Power Lance",
            "Technology Expert",
            "Triceratops Dinozord",
            "Strategic Analysis",
            "Team Support",
        ],
        "color": "#2563EB",
        "bg_from": "#020617",
        "bg_to": "#1D4ED8",
        "glow": "rgba(37,99,235,0.65)",
        "clips": [
            {"title": "Billy genius moments", "duration": "5:31"},
            {"title": "Blue Ranger fight scenes", "duration": "8:05"},
            {"title": "Triceratops Dinozord", "duration": "3:19"},
            {"title": "Power Lance action", "duration": "2:58"},
        ],
    },
    {
        "id": "pink",
        "image": "/Pink Ranger.png",
        "name": "Pink Ranger",
        "real_name": "Kimberly Hart",
        "role": "Ágil, valiente y precisa",
        "zord": "Pterodactyl Dinozord",
        "weapon": "Power Bow",
        "affiliation": "Angel Grove Power Rangers",
        "description": (
            "Kimberly Hart destaca por su agilidad, precisión y actitud positiva. Como Pink Ranger, "
            "usa el Power Bow y el Pterodactyl Dinozord para atacar desde el aire."
        ),
        "abilities": [
            "Power Bow",
            "Gymnastics",
            "Pterodactyl Dinozord",
            "Air Combat",
            "Precision Attacks",
        ],
        "color": "#EC4899",
        "bg_from": "#2A0018",
        "bg_to": "#9D174D",
        "glow": "rgba(236,72,153,0.65)",
        "clips": [
            {"title": "Kimberly best moments", "duration": "6:03"},
            {"title": "Pink Ranger bow attacks", "duration": "3:44"},
            {"title": "Pterodactyl Dinozord", "duration": "2:39"},
            {"title": "Pink Ranger fights", "duration": "7:25"},
        ],
    },
    {
        "id": "black",
        "image": "/Black Ranger.png",
        "name": "Black Ranger",
        "real_name": "Zack Taylor",
        "role": "Energía, ritmo y combate",
        "zord": "Mastodon Dinozord",
        "weapon": "Power Axe",
        "affiliation": "Angel Grove Power Rangers",
        "description": (
            "Zack Taylor combina carisma, fuerza y estilo. Su forma de pelear tiene ritmo y "
            "personalidad, usando el Power Axe y el Mastodon Dinozord como armas principales."
        ),
        "abilities": [
            "Power Axe",
            "Hip Hop Kido",
            "Mastodon Dinozord",
            "Close Combat",
            "High Mobility",
        ],
        "color": "#111827",
        "bg_from": "#020617",
        "bg_to": "#111827",
        "glow": "rgba(156,163,175,0.55)",
        "clips": [
            {"title": "Zack fight scenes", "duration": "5:43"},
            {"title": "Black Ranger best moments", "duration": "6:50"},
            {"title": "Mastodon Dinozord call", "duration": "2:41"},
            {"title": "Power Axe attacks", "duration": "3:36"},
        ],
    },
    {
        "id": "yellow",
        "image": "/Yellow Ranger.png",
        "name": "Yellow Ranger",
        "real_name": "Trini Kwan",
        "role": "Equilibrio, disciplina y fuerza",
        "zord": "Sabertooth Tiger Dinozord",
        "weapon": "Power Daggers",
        "affiliation": "Angel Grove Power Rangers",
        "description": (
            "Trini Kwan es calmada, disciplinada y poderosa. Como Yellow Ranger, aporta equilibrio "
            "al equipo y domina sus Power Daggers con gran precisión."
        ),
        "abilities": [
            "Power Daggers",
            "Kung Fu",
            "Sabertooth Tiger Dinozord",
            "Speed",
            "Team Balance",
        ],
        "color": "#EAB308",
        "bg_from": "#1C1200",
        "bg_to": "#854D0E",
        "glow": "rgba(234,179,8,0.65)",
        "clips": [
            {"title": "Trini best moments", "duration": "5:02"},
            {"title": "Yellow Ranger fights", "duration": "6:44"},
            {"title": "Power Daggers action", "duration": "3:18"},
            {"title": "Sabertooth Tiger Dinozord", "duration": "2:51"},
        ],
    },
]

RANGERS = [RangerData(**item) for item in RANGERS_RAW]


# ─────────────────────────────────────────────
# State
# ─────────────────────────────────────────────
class State(rx.State):
    selected_id: str = "red"

    def select_ranger(self, ranger_id: str):
        self.selected_id = ranger_id

    @rx.var
    def selected_ranger(self) -> RangerData:
        for ranger in RANGERS:
            if ranger.id == self.selected_id:
                return ranger
        return RANGERS[0]


# ─────────────────────────────────────────────
# Components
# ─────────────────────────────────────────────
def page_style():
    return rx.el.style(
        f"""
        @import url('{GFONT_URL}');

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            margin: 0;
            background: #030303;
        }}

        .ranger-card {{
            transition: all .28s ease;
        }}

        .ranger-card:hover {{
            transform: translateY(-8px) scale(1.02);
        }}

        .glass {{
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.12);
            backdrop-filter: blur(18px);
        }}
        """
    )


def navbar():
    return rx.hstack(
        rx.hstack(
            rx.text("⚡", font_size="2em"),
            rx.heading(
                "POWER RANGERS",
                color="white",
                font_family="Permanent Marker",
                font_size="1.9em",
            ),
            spacing="3",
            align="center",
        ),
        rx.spacer(),
        rx.hstack(
            rx.link("Inicio", href="#inicio", color="white"),
            rx.link("Rangers", href="#rangers", color="white"),
            rx.link("Zords", href="#zords", color="white"),
            rx.link("Clips", href="#clips", color="white"),
            spacing="6",
            display=["none", "none", "flex"],
        ),
        rx.button(
            "Morphin Time",
            background="#E11D48",
            color="white",
            border_radius="999px",
            padding_x="1.4em",
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="999",
        padding="1.1em 3em",
        background="rgba(3,3,3,0.68)",
        backdrop_filter="blur(16px)",
        border_bottom="1px solid rgba(255,255,255,0.08)",
    )


def hero():
    return rx.box(
        rx.vstack(
            rx.badge(
                "MIGHTY MORPHIN CHARACTER SHOWCASE",
                color_scheme="red",
                variant="solid",
                font_size="0.9em",
                padding="0.6em 1em",
            ),
            rx.heading(
                "IT'S MORPHIN TIME!",
                color="white",
                text_align="center",
                font_family="Permanent Marker",
                font_size=["3.5em", "5em", "7em"],
                line_height="0.95",
                text_shadow="0 0 35px rgba(225,29,72,.8)",
            ),
            rx.text(
                "Una landing page inspirada en un showcase de personajes, reimaginada con el universo de los Power Rangers.",
                color="#D1D5DB",
                text_align="center",
                font_size="1.25em",
                max_width="820px",
                line_height="1.7",
            ),
            rx.hstack(
                rx.button(
                    "Ver Rangers",
                    size="4",
                    background="#E11D48",
                    color="white",
                    border_radius="999px",
                    padding_x="2em",
                ),
                rx.button(
                    "Explorar Zords",
                    size="4",
                    variant="outline",
                    color="white",
                    border_radius="999px",
                    padding_x="2em",
                ),
                spacing="4",
                flex_wrap="wrap",
                justify="center",
            ),
            spacing="6",
            align="center",
        ),
        id="inicio",
        min_height="100vh",
        display="flex",
        align_items="center",
        justify_content="center",
        padding="8em 2em 4em 2em",
        background=(
            "linear-gradient(rgba(0,0,0,.60), rgba(0,0,0,.86)), "
            "url('https://wallpapers.com/images/hd/mighty-morphin-power-rangers-team-84cc4b3fg5pf147y.jpg')"
        ),
        background_size="cover",
        background_position="center",
    )


def stat_box(label: str, value: str):
    return rx.box(
        rx.text(label, color="#9CA3AF", font_size="0.85em", text_transform="uppercase"),
        rx.text(value, color="white", font_size="1.05em", font_weight="700"),
        class_name="glass",
        border_radius="18px",
        padding="1em",
        width="100%",
    )


def ability_tag(text: str, color: str):
    return rx.badge(
        text,
        background=f"{color}22",
        color="white",
        border=f"1px solid {color}",
        padding="0.55em 0.8em",
        border_radius="999px",
    )


def ranger_selector_card(ranger: RangerData):
    return rx.box(
        rx.vstack(
            rx.image(
                src=ranger.image,
                width="100%",
                height="180px",
                object_fit="contain",
                filter=f"drop-shadow(0 0 22px {ranger.glow})",
            ),
            rx.heading(ranger.name, color="white", size="4", text_align="center"),
            rx.text(ranger.real_name, color="#D1D5DB", text_align="center"),
            spacing="3",
            align="center",
        ),
        on_click=lambda: State.select_ranger(ranger.id),
        class_name="ranger-card",
        cursor="pointer",
        border_radius="28px",
        padding="1.3em",
        background=f"linear-gradient(145deg, {ranger.bg_from}, {ranger.bg_to})",
        border=f"1px solid {ranger.color}",
        box_shadow=f"0 0 35px {ranger.glow}",
        min_height="300px",
    )


def selected_ranger_panel():
    return rx.box(
        rx.grid(
            rx.vstack(
                rx.badge(
                    State.selected_ranger.role,
                    background=State.selected_ranger.color,
                    color="white",
                    padding="0.55em 1em",
                    border_radius="999px",
                ),
                rx.heading(
                    State.selected_ranger.name,
                    color="white",
                    font_family="Permanent Marker",
                    font_size=["2.8em", "4.5em"],
                    line_height="1",
                ),
                rx.text(
                    State.selected_ranger.real_name,
                    color=State.selected_ranger.color,
                    font_size="1.6em",
                    font_weight="700",
                ),
                rx.text(
                    State.selected_ranger.description,
                    color="#D1D5DB",
                    font_size="1.1em",
                    line_height="1.8",
                ),
                rx.grid(
                    stat_box("Zord", State.selected_ranger.zord),
                    stat_box("Arma", State.selected_ranger.weapon),
                    stat_box("Afiliación", State.selected_ranger.affiliation),
                    columns="3",
                    spacing="4",
                    width="100%",
                ),
                rx.flex(
                    rx.foreach(
                        State.selected_ranger.abilities,
                        lambda item: ability_tag(item, State.selected_ranger.color),
                    ),
                    gap="0.7em",
                    flex_wrap="wrap",
                ),
                spacing="5",
                align="start",
            ),
            rx.center(
                rx.image(
                    src=State.selected_ranger.image,
                    width="100%",
                    max_width="430px",
                    height="560px",
                    object_fit="contain",
                    filter=f"drop-shadow(0 0 55px {State.selected_ranger.glow})",
                ),
            ),
            columns="2",
            spacing="8",
            align_items="center",
        ),
        class_name="glass",
        border_radius="38px",
        padding=["2em", "3em"],
        width="100%",
        max_width="1250px",
        background=f"linear-gradient(135deg, {State.selected_ranger.bg_from}, #050505 55%, {State.selected_ranger.bg_to})",
        box_shadow=f"0 0 70px {State.selected_ranger.glow}",
    )


def rangers_section():
    return rx.box(
        rx.vstack(
            rx.badge("SELECCIONA TU RANGER", color_scheme="red", variant="soft"),
            rx.heading(
                "Character Showcase",
                color="white",
                font_family="Permanent Marker",
                font_size=["2.6em", "4em"],
                text_align="center",
            ),
            selected_ranger_panel(),
            rx.grid(
                *[ranger_selector_card(ranger) for ranger in RANGERS],
                columns="6",
                spacing="5",
                width="100%",
                max_width="1250px",
            ),
            spacing="8",
            align="center",
        ),
        id="rangers",
        padding="6em 2em",
        background="radial-gradient(circle at top, #450A0A 0%, #050505 45%, #020617 100%)",
    )


def zord_card(title: str, desc: str, icon: str, color: str):
    return rx.box(
        rx.vstack(
            rx.text(icon, font_size="4em"),
            rx.heading(title, color="white", size="5", text_align="center"),
            rx.text(desc, color="#D1D5DB", text_align="center", line_height="1.6"),
            spacing="4",
            align="center",
        ),
        class_name="glass ranger-card",
        border_radius="28px",
        padding="2em",
        border=f"1px solid {color}",
        box_shadow=f"0 0 28px {color}66",
    )


def zords_section():
    return rx.box(
        rx.vstack(
            rx.badge("DINOZORDS", color_scheme="yellow", variant="soft"),
            rx.heading(
                "Poderes legendarios",
                color="white",
                font_family="Permanent Marker",
                font_size=["2.5em", "4em"],
                text_align="center",
            ),
            rx.grid(
                zord_card("Tyrannosaurus", "El poder salvaje del Red Ranger.", "🦖", "#E11D48"),
                zord_card("Dragonzord", "El zord legendario del Green Ranger.", "🐉", "#16A34A"),
                zord_card("Triceratops", "Defensa, tecnología y resistencia.", "🛡️", "#2563EB"),
                zord_card("Pterodactyl", "Ataques rápidos desde el aire.", "🪽", "#EC4899"),
                columns="4",
                spacing="5",
                width="100%",
                max_width="1200px",
            ),
            spacing="8",
            align="center",
        ),
        id="zords",
        padding="6em 2em",
        background="#020617",
    )


def clip_item(clip: ClipData):
    return rx.hstack(
        rx.box(
            rx.text("▶", color="white", font_size="1.2em"),
            background="#E11D48",
            border_radius="50%",
            width="42px",
            height="42px",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        rx.vstack(
            rx.text(clip.title, color="white", font_weight="700"),
            rx.text(clip.duration, color="#9CA3AF", font_size="0.9em"),
            spacing="1",
            align="start",
        ),
        width="100%",
        class_name="glass",
        border_radius="18px",
        padding="1em",
    )


def clips_section():
    return rx.box(
        rx.vstack(
            rx.badge("CLIPS", color_scheme="red", variant="soft"),
            rx.heading(
                "Momentos destacados",
                color="white",
                font_family="Permanent Marker",
                font_size=["2.5em", "4em"],
                text_align="center",
            ),
            rx.box(
                rx.vstack(
                    rx.foreach(State.selected_ranger.clips, clip_item),
                    spacing="4",
                    width="100%",
                ),
                width="100%",
                max_width="850px",
            ),
            spacing="7",
            align="center",
        ),
        id="clips",
        padding="6em 2em",
        background="linear-gradient(135deg, #050505, #111827)",
    )


def footer():
    return rx.box(
        rx.vstack(
            rx.heading("GO GO POWER RANGERS", color="white", font_family="Permanent Marker"),
            rx.text(
                "Landing page creada con Reflex · Tema: Power Rangers Character Showcase",
                color="#9CA3AF",
                text_align="center",
            ),
            spacing="3",
            align="center",
        ),
        padding="3em 2em",
        background="#000000",
        border_top="1px solid rgba(255,255,255,0.08)",
    )


def index():
    return rx.box(
        page_style(),
        navbar(),
        hero(),
        rangers_section(),
        zords_section(),
        clips_section(),
        footer(),
        background="#050505",
        font_family="Rajdhani",
    )


app = rx.App()
app.add_page(index, route="/")