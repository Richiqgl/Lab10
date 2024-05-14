from dataclasses import dataclass
@dataclass
class Nazione:
    CCode:int
    StateAbb:str
    StateNme:str

    def __hash__(self):
        return hash(self.CCode)

    def __str__(self):
        return f"Codice :{self.CCode} - {self.StateAbb} - {self.StateNme}"