import reflex as rx

config = rx.Config(
    app_name="landing_reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)