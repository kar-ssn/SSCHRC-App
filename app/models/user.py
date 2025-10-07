import reflex as rx
from typing import Optional


class User(rx.Model, table=True):
    id: Optional[int] = None
    name: str
    email: str
    password_hash: str
    role: str