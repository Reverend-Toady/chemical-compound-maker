from __future__ import annotations
from typing import Union, List
from dataclasses import dataclass
from PIL.Image import Image
from rdkit.Chem.rdchem import Atom, Bond


@dataclass
class Compound:
    name: str
    formula: str
    weight: float
    atoms: List[Atom]
    bonds: List[Bond]
    image: Image

    def __repr__(self) -> str:
        return f"{self.name} {self.formula}"


class Reaction:
    def __init__(
        self,
        reactants: Union[Compound, List[Compound]],
        reagents: Union[Compound, List[Compound]],
        products: Union[Compound, List[Compound]],
    ) -> None:
        self.reactants = reactants
        self.reagents = reagents
        self.products = products

    def __repr__(self) -> str:
        return f"""
            Reactant{"s" if isinstance(self.reactants, list) > 1 else ""}: {", ".join(str(reactant) for reactant in self.reactants) if isinstance(self.reactants, list) else str(self.reactants)}
            Reagent{"s" if isinstance(self.reagents, list) > 1 else ""}: {", ".join(str(reagent) for reagent in self.reagents) if isinstance(self.reagents, list) else str(self.reagents)}
            Product{"s" if isinstance(self.products, list) > 1 else ""}: {", ".join(str(product) for product in self.products) if isinstance(self.products, list) else str(self.products)}
        """
