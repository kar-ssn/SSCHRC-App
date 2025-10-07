import reflex as rx


def navbar() -> rx.Component:
    """The navbar component for the app."""
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("heart-pulse", class_name="text-[#2E8B57] h-8 w-8"),
                    rx.el.span(
                        "Shankara Cancer Hospital",
                        class_name="hidden md:block text-xl font-bold text-white font-['Inter']",
                    ),
                    class_name="flex items-center gap-3",
                ),
                href="/",
            ),
            rx.el.nav(
                rx.el.a(
                    "Departments",
                    href="#",
                    class_name="text-white hover:text-gray-300 transition-colors",
                ),
                rx.el.a(
                    "Research",
                    href="#",
                    class_name="text-white hover:text-gray-300 transition-colors",
                ),
                rx.el.a(
                    "Donations",
                    href="#",
                    class_name="text-white hover:text-gray-300 transition-colors",
                ),
                rx.el.a(
                    "Patient Portal",
                    href="#",
                    class_name="bg-[#FF7043] text-white px-4 py-2 rounded-lg hover:bg-orange-600 transition-colors text-sm font-semibold",
                ),
                class_name="flex items-center gap-6 text-sm font-medium font-['Lato']",
            ),
            class_name="container mx-auto flex items-center justify-between p-4",
        ),
        class_name="bg-[#1B365D] sticky top-0 z-50 shadow-md",
    )