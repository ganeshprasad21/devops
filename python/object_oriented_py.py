class Human:
    def __init__(self,name="default"):
        self.name = name
        print(f"human initialized with name = {self.name}")


h = Human("Ganesh Prasad R")

print(h.name)

class ConfigManager:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config = {}  # Initialize config storage
        return cls._instance

config1 = ConfigManager()
config2 = ConfigManager()
config1.config["timeout"] = 30

print(config2.config["timeout"])  # ✅ 30 (Shared instance)