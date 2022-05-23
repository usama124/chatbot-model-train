from pydantic import BaseModel


class TrainModel(BaseModel):
    filepath: str
