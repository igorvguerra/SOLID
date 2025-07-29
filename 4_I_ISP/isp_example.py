from abc import ABC, abstractmethod

class DocumentPdf(ABC): 

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass



class DocumentTxt(ABC):

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def fornat(self): pass

    
    
class DocumentExcel(ABC):

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass