import reflex as rx
from typing import Optional


class Department(rx.Model, table=True):
    id: Optional[int] = None
    name: str
    description: str