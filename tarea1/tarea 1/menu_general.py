#parecido con el lab 1

from abc import ABC, abstractmethod

# Program specific packages
from battle import * #otro nombre 



class Menu(ABC): 
   @abstractmethod
   @classmethod
   def get_menu(cls) -> str: