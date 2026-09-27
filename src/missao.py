from dataclasses import dataclass

@dataclass
class Missao:
    codigo: int
    titulo: str
    grau_dificuldade: int
    recompensa_ouro: int
    urgencia: int

    def __str__(self):
        return f"[Cod: {self.codigo:03d}] {self.titulo:22} | Dificuldade: {self.grau_dificuldade:2} | Urgência: {self.urgencia:2} | Ouro: {self.recompensa_ouro}"