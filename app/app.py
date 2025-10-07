import reflex as rx
from app.components.layout import layout
from app.components.home import hero_section, quick_access_cards


def index() -> rx.Component:
    """The home page of the app."""
    return layout(
        rx.el.div(
            hero_section(),
            quick_access_cards(),
            class_name="flex flex-col items-center",
        )
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Lato:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="SSCHRC - Home")