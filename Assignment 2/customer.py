from dataclasses import dataclass

@dataclass
class Customer:
    id: int
    name: str
    email: str
    active: bool

    def __repr__(self) -> str:
        return f"Customer(id={self.id}, name='{self.name}', email='{self.email}', active={self.active})"