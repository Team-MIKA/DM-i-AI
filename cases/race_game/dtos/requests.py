from typing import Any
from pydantic import BaseModel


class RaceGamePredictRequest(BaseModel):
    state: Any
