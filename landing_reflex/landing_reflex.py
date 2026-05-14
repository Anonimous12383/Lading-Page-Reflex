import reflex as rx


class State(rx.State):
    pass


def navbar():
    return rx.hstack(
        rx.heading(
            "NovaStudio",
            size="7",
            color="white",
            font_weight="bold",
        ),

        rx.spacer(),

        rx.hstack(
            rx.link("Inicio", href="#inicio", color="white"),
            rx.link("Servicios", href="#servicios", color="white"),
            rx.link("Proyectos", href="#proyectos", color="white"),
            rx.link("Contacto", href="#contacto", color="white"),
            spacing="7",
        ),

        rx.button(
            "Empezar",
            bg="white",
            color="black",
            border_radius="999px",
            padding_x="1.5em",
        ),

        width="100%",
        padding="1.5em 3em",
        position="fixed",
        top="0",
        z_index="999",
        background="rgba(0,0,0,0.7)",
        backdrop_filter="blur(10px)",
    )


def hero_section():
    return rx.box(
        rx.vstack(
            rx.badge(
                "AGENCIA CREATIVA",
                color_scheme="purple",
                variant="soft",
                font_size="0.9em",
                padding="0.5em 1em",
            ),

            rx.heading(
                "Creamos experiencias digitales modernas",
                size="9",
                color="white",
                text_align="center",
                max_width="900px",
            ),

            rx.text(
                "Diseñamos páginas web futuristas, branding y experiencias visuales para negocios modernos.",
                color="#D1D5DB",
                font_size="1.2em",
                text_align="center",
                max_width="700px",
            ),

            rx.hstack(
                rx.button(
                    "Ver Proyectos",
                    size="3",
                    bg="#7C3AED",
                    color="white",
                    border_radius="999px",
                ),

                rx.button(
                    "Contactar",
                    size="3",
                    variant="outline",
                    color="white",
                    border_radius="999px",
                ),

                spacing="4",
            ),

            spacing="6",
            align="center",
        ),

        id="inicio",
        min_height="100vh",
        display="flex",
        align_items="center",
        justify_content="center",
        padding="2em",
        background="""
        linear-gradient(
            135deg,
            #0F172A 0%,
            #111827 40%,
            #4C1D95 100%
        )
        """,
    )


def service_card(icon, title, description):
    return rx.box(
        rx.vstack(
            rx.text(icon, font_size="3em"),

            rx.heading(
                title,
                size="5",
                color="white",
            ),

            rx.text(
                description,
                color="#D1D5DB",
                text_align="center",
            ),

            spacing="4",
            align="center",
        ),

        background="rgba(255,255,255,0.05)",
        border="1px solid rgba(255,255,255,0.08)",
        border_radius="25px",
        padding="2em",
        width="100%",
    )


def services_section():
    return rx.box(
        rx.vstack(
            rx.badge(
                "SERVICIOS",
                color_scheme="purple",
                variant="soft",
            ),

            rx.heading(
                "Soluciones para tu negocio",
                size="8",
                color="white",
            ),

            rx.grid(
                service_card(
                    "💻",
                    "Diseño Web",
                    "Landing pages modernas y rápidas.",
                ),

                service_card(
                    "🎨",
                    "Branding",
                    "Identidad visual profesional.",
                ),

                service_card(
                    "🚀",
                    "Marketing",
                    "Estrategias digitales efectivas.",
                ),

                columns="3",
                spacing="6",
                width="100%",
                max_width="1200px",
            ),

            spacing="8",
            align="center",
        ),

        id="servicios",
        padding="6em 2em",
        background="#050505",
    )


def project_card(title):
    return rx.box(
        rx.vstack(
            rx.spacer(),

            rx.heading(
                title,
                color="white",
                size="5",
            ),

            rx.text(
                "Proyecto moderno y minimalista.",
                color="#D1D5DB",
            ),

            align="start",
            height="100%",
        ),

        height="300px",
        border_radius="30px",
        padding="2em",
        background="""
        linear-gradient(
            135deg,
            #7C3AED,
            #312E81
        )
        """,
    )


def projects_section():
    return rx.box(
        rx.vstack(
            rx.badge(
                "PORTAFOLIO",
                color_scheme="purple",
                variant="soft",
            ),

            rx.heading(
                "Proyectos destacados",
                size="8",
                color="white",
            ),

            rx.grid(
                project_card("Landing Page"),
                project_card("App Mobile"),
                project_card("Creative Studio"),

                columns="3",
                spacing="6",
                width="100%",
                max_width="1200px",
            ),

            spacing="8",
            align="center",
        ),

        id="proyectos",
        padding="6em 2em",
        background="#0A0A0A",
    )


def contact_section():
    return rx.box(
        rx.vstack(
            rx.heading(
                "¿Listo para trabajar juntos?",
                size="8",
                color="white",
                text_align="center",
            ),

            rx.text(
                "Contáctanos y crea una presencia digital increíble.",
                color="#D1D5DB",
                text_align="center",
            ),

            rx.hstack(
                rx.input(
                    placeholder="Tu correo",
                    width="320px",
                    background="white",
                    border_radius="999px",
                ),

                rx.button(
                    "Enviar",
                    bg="#7C3AED",
                    color="white",
                    border_radius="999px",
                ),

                spacing="3",
            ),

            spacing="6",
            align="center",
        ),

        id="contacto",
        padding="6em 2em",
        background="""
        linear-gradient(
            135deg,
            #111827,
            #4C1D95
        )
        """,
    )


def footer():
    return rx.box(
        rx.text(
            "© 2026 NovaStudio - Creado con Reflex",
            color="#9CA3AF",
        ),

        text_align="center",
        padding="2em",
        background="#050505",
    )


def index():
    return rx.box(
        navbar(),
        hero_section(),
        services_section(),
        projects_section(),
        contact_section(),
        footer(),

        font_family="Inter",
        background="#000000",
    )


app = rx.App()
app.add_page(index)