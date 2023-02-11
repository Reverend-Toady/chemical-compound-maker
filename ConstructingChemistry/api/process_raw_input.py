from .dataclasses import Compound, Reaction
from typing import Optional

from werkzeug.datastructures import ImmutableMultiDict
from flask import flash

from rdkit.Chem import MolFromSmiles  # type: ignore
from rdkit.Chem.Draw import MolToImage

import pubchempy
from pubchempy import Compound as pcpCompound


def process_raw_input(forms: ImmutableMultiDict) -> Optional[Reaction]:
    def get_compound_data(molecule, compound: pcpCompound) -> Compound:
        new_compound = Compound(
            compound.cid,  # type: ignore
            compound.iupac_name,  # type: ignore
            compound.molecular_formula,  # type: ignore
            compound.molecular_weight,  # type: ignore
            compound.atoms,  # type: ignore
            compound.bonds,  # type: ignore
            MolToImage(molecule),  # type: ignore
        )
        return new_compound

    reactants = []
    reagents = []
    products = []

    for key in forms:
        if key.startswith("reactant"):
            molecule = MolFromSmiles(forms.get(key))
            if molecule is None:
                flash(
                    "Please input a valid reactant in SMILES notation", category="error"
                )
                return
            compound = pubchempy.get_compounds(forms.get(key), namespace="smiles")[0]
            reactants.append(get_compound_data(molecule, compound))  # type: ignore

        elif key.startswith("reagent"):
            molecule = MolFromSmiles(forms.get(key))
            if molecule is None:
                flash(
                    "Please input a valid reagent in SMILES notation", category="error"
                )
                return
            compound = pubchempy.get_compounds(forms.get(key), namespace="smiles")[0]
            reagents.append(get_compound_data(molecule, compound))  # type: ignore

        elif key.startswith("product"):
            molecule = MolFromSmiles(forms.get(key))
            if molecule is None:
                flash(
                    "Please input a valid product in SMILES notation", category="error"
                )
                return
            compound = pubchempy.get_compounds(forms.get(key), namespace="smiles")[0]
            products.append(get_compound_data(molecule, compound))  # type: ignore

    return Reaction(reactants, reagents, products)
