import time
import requests

class HumanState():
    def __init__(self, count):
        super().__init__()
        self.count = count
        if(count>0):
            self.value = 1
        else:
            self.value = 0

    def enable_decrease(self):
        if self.value == 1:
            return 1
        else:
            return 0

    def enable_increase(self):
        if self.value == 0:
            return 1
        else:
            return 0
        
    def ext_action_decrease(self):
        if self.count > 0:
            self.count = self.count - 1            
        if self.enable_decrease(self) and self.count == 0:
            self.value = self.value - 1
            
    def ext_action_increase(self):
        self.count = self.count + 1
        if self.enable_increase(self) and self.count == 1:
            self.value = self.value + 1
            
    def get(self):
        return int(self.value)
