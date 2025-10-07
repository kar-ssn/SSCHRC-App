import reflex as rx
from typing import Optional
from datetime import datetime


class Message(rx.Model, table=True):
    id: Optional[int] = None
    sender_id: int
    receiver_id: int
    text: str
    timestamp: datetime