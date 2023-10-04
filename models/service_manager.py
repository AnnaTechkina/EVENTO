from pydantic import BaseModel


class Service_manager(BaseModel):
    id: int
    title: str

    def add(self):
        pass

    def change(self):
        pass

    def get(self):
        pass
