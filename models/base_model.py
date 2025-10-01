from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(self, name, category):
        self._model_name = name
        self._category = category

    @abstractmethod
    def run(self, input_data):
        pass

    def get_info(self):
        return f"Model: {self._model_name}\nCategory: {self._category}\n"
