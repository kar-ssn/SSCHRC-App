import reflex as rx
from typing import Optional
from datetime import date


class Report(rx.Model, table=True):
    id: Optional[int] = None
    patient_id: int
    file_url: str
    type: str
    date_issued: date