from dataclasses import dataclass

@dataclass(frozen=True)
class Mark:
    value: int
    subj: str
    
@dataclass(frozen=True)
class Test_Results:
    gained: int
    max_possible: int
    subj: str
    
    def __repr__(self):
        return f"Предмет: {self.subj}.Результат:{self.gained}/{self.max_possible}."