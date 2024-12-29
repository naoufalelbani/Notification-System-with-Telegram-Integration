from typing import List
from abc import ABC,abstractmethod
from utils import get_logger

logger = get_logger(__name__)

class Observer(ABC):
  """Abstract Observer interface for all notifiers."""
  def update(self, message: str):
    pass
  
class Notifier:
  def __init__(self):
    self.observers: List[Observer] = []
  
  def add_observer(self, observer: Observer):
    self.observers.append(observer)
    logger.info(f"Observer added: {observer.__class__.__name__}")
    
  def remove_observer(self, observer: Observer):
    self.observers.remove(observer)
    logger.info(f"Observer removed: {observer.__class__.__name__}")
    
  def notify_observers(self, message: str):
    for observer in self.observers:
      observer.update(message)