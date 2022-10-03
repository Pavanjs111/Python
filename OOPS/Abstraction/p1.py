from abc import ABC,abstractmethod
from site import abs_paths
class calculate(ABC):
    @abstractmethod
    def add(self,*arg):
        pass
    @abstractmethod
    def mul(self,*arg):
        pass

    