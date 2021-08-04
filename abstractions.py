from abc import ABC, abstractmethod

class ModuleInterface(ABC):
    @abstractmethod
    def type_validation(self):
        pass
    
    @abstractmethod
    def file_iteration(self):
        pass
    
    @abstractmethod
    def read_full_content(self):
        pass
    @abstractmethod
    def read_first_two_lines(self):
        pass
    
    @abstractmethod
    def read_last_two_lines(self):
        pass

class ModuleInterfaceB(ABC):
    @abstractmethod
    def type_validation(self):
        pass
    
    @abstractmethod
    def file_iteration(self):
        pass

    @abstractmethod
    def file_manipulation(uself):
        pass
    
    @abstractmethod
    def read_first_two_lines(self):
        pass
    
    @abstractmethod
    def read_last_two_lines(self):
        pass