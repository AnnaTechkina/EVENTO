from pydantic import BaseModel


class Write(BaseModel):
    id: int
    client_id: int  # получить id из класса Client
    service_id: int  # получить id из класса Servis
    data: str
    time: str
    price: float

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def get(self):
        pass
