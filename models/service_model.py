from pydantic import BaseModel


class Servise(BaseModel):
    id: int
    title: str
    description: str
    type: str
    lock: str

    def add(self):  # добавить услугу
        pass

    def delete(self):  # удалить услугу
        pass

    def change(self):  # изменить услугу
        pass

    def get(self):  # найти услугу
        pass

    def lock(self):  # заблокировать запись на услугу
        pass
