from pydantic import BaseModel


class Client(BaseModel):
    id: int
    name: str
    second_name: str
    number_tel: int

    def add_client(self):  # добавить клиента
        pass

    def delete(self):  # удалить клиента
        pass

    def change(self):  # изменить данные клиента
        pass

    def get(self):  # найти клиента
        pass
