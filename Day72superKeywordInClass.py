

class Device:
    def connect(self):
        print("Device is connecting...")


class Smartphone(Device):
    "A simple Smartphone model."
    def connect(self):
        super().connect()
        print("Smartphone is connecting to mobile network...")
    
class SmartTV(Device):
    "A simple Smart TV model."
    def connect(self):
        super().connect()
        print("Smart TV is connecting to Wi-Fi...")
    
class SmartRemote(Smartphone, SmartTV):
    "A simple Smart Remote model."
    def connect(self):
        super().connect()
        print("SmartRemote is ready to control devices!")
         


s = SmartRemote()
s.connect()