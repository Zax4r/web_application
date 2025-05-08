from dataclasses import dataclass

@dataclass(frozen=True)
class Mark:
    value: int
    subj: str