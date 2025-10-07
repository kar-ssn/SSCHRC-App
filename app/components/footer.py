import reflex as rx


def footer() -> rx.Component:
    """The footer component for the app."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Shankara Cancer Hospital & Research Centre",
                    class_name="text-lg font-semibold text-white",
                ),
                rx.el.p(
                    "Providing hope, healing, and world-class care.",
                    class_name="text-gray-400 mt-2",
                ),
            ),
            rx.el.div(
                rx.el.h4("Quick Links", class_name="font-semibold text-white"),
                rx.el.div(
                    rx.el.a(
                        "Home", href="/", class_name="text-gray-400 hover:text-white"
                    ),
                    rx.el.a(
                        "Departments",
                        href="#",
                        class_name="text-gray-400 hover:text-white",
                    ),
                    rx.el.a(
                        "Appointments",
                        href="#",
                        class_name="text-gray-400 hover:text-white",
                    ),
                    rx.el.a(
                        "Contact Us",
                        href="#",
                        class_name="text-gray-400 hover:text-white",
                    ),
                    class_name="flex flex-col gap-2 mt-2",
                ),
                class_name="mt-4 md:mt-0",
            ),
            rx.el.div(
                rx.el.h4("Follow Us", class_name="font-semibold text-white"),
                rx.el.div(
                    rx.el.a(rx.icon("twitter", class_name="h-6 w-6"), href="#"),
                    rx.el.a(rx.icon("facebook", class_name="h-6 w-6"), href="#"),
                    rx.el.a(rx.icon("linkedin", class_name="h-6 w-6"), href="#"),
                    class_name="flex gap-4 mt-2 text-gray-400",
                ),
                class_name="mt-4 md:mt-0",
            ),
            class_name="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 p-8 md:p-12",
        ),
        rx.el.div(
            rx.el.p(
                "© 2024 Shankara Cancer Hospital. All Rights Reserved.",
                class_name="text-center text-gray-500 text-sm",
            ),
            class_name="border-t border-gray-700 py-4",
        ),
        class_name="bg-[#1B365D] font-['Lato']",
    )