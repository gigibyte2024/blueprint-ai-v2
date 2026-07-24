from abc import ABC, abstractmethod
from app.graph.state import BlueprintState


class BaseModule(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(self, state: BlueprintState):
        pass