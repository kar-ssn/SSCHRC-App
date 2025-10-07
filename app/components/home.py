import reflex as rx


def hero_section() -> rx.Component:
    """The hero section of the home page."""
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "World-Class Cancer Care, Centered On You",
                class_name="text-4xl md:text-6xl font-bold text-[#1B365D] tracking-tight font-['Inter']",
            ),
            rx.el.p(
                "Compassionate, state-of-the-art treatment from a team that's dedicated to your healing journey.",
                class_name="mt-4 text-lg md:text-xl text-[#757575] max-w-3xl",
            ),
            rx.el.div(
                rx.el.a(
                    "Book an Appointment",
                    href="#",
                    class_name="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-xl text-white bg-[#FF7043] hover:bg-orange-600 shadow-md transition-transform transform hover:scale-105",
                ),
                rx.el.a(
                    "Find a Doctor",
                    href="#",
                    class_name="inline-flex items-center justify-center px-6 py-3 border border-gray-300 text-base font-medium rounded-xl text-[#1B365D] bg-white hover:bg-gray-50 shadow-md transition-transform transform hover:scale-105",
                ),
                class_name="mt-8 flex flex-col sm:flex-row gap-4",
            ),
            class_name="container mx-auto text-center py-20 md:py-32 px-6",
        ),
        class_name="w-full bg-[#F7F9FB]",
    )


def quick_access_cards() -> rx.Component:
    """The quick access cards section of the home page."""
    cards = [
        {
            "icon": "user",
            "title": "Patient Portal",
            "description": "Access your records, appointments, and results.",
            "href": "#",
            "color": "text-[#0077B6]",
        },
        {
            "icon": "flask-round",
            "title": "Lab Reports",
            "description": "View and download your latest lab reports securely.",
            "href": "#",
            "color": "text-[#2E8B57]",
        },
        {
            "icon": "receipt",
            "title": "Billing & Payments",
            "description": "Manage your bills and make secure online payments.",
            "href": "#",
            "color": "text-[#FF7043]",
        },
    ]
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Your Health at Your Fingertips",
                class_name="text-3xl font-bold text-center text-[#1B365D] font-['Inter']",
            ),
            rx.el.p(
                "Quickly access essential services and information.",
                class_name="mt-2 text-lg text-center text-[#757575]",
            ),
            rx.el.div(
                rx.foreach(cards, lambda card: access_card(card)),
                class_name="mt-12 grid grid-cols-1 md:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto py-16 px-6",
        ),
        class_name="w-full bg-white",
    )


def access_card(card: dict) -> rx.Component:
    """A single access card component."""
    return rx.el.a(
        rx.el.div(
            rx.icon(card["icon"], size=32, class_name=f"{card['color']} mb-4"),
            rx.el.h3(
                card["title"],
                class_name="text-xl font-semibold text-[#212121] font-['Inter']",
            ),
            rx.el.p(card["description"], class_name="mt-2 text-[#757575]"),
            rx.el.div(
                "Learn More",
                rx.icon("arrow-right", class_name="ml-2 h-4 w-4"),
                class_name=f"mt-6 flex items-center font-semibold {card['color']}",
            ),
            class_name="p-8",
        ),
        href=card["href"],
        class_name="block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg transition-shadow duration-300",
    )