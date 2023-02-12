from .dataclasses import Compound, Reaction
from requests import get as rget
from typing import Optional
from PIL.Image import Image

from werkzeug.datastructures import ImmutableMultiDict
from flask import flash

from rdkit.Chem import MolFromSmiles, rdchem  # type: ignore
from rdkit.Chem.Draw import MolToImage
from rdkit.Chem import Descriptors

def convert_iupac_to_smiles(name: str) -> Optional[str]:
    resp = rget(f"http://cactus.nci.nih.gov/chemical/structure/{name}/smiles")
    if resp.status_code == 200:
        return resp.text
    flash("Please input a valid iupac name", category="error")
    return None

def process_raw_input(forms: ImmutableMultiDict) -> Optional[Reaction]:
    def get_compound_data(molecule: rdchem.Mol, iupac_name: str) -> Compound:
        new_compound = Compound(
            iupac_name,  # type: ignore
            Descriptors.rdMolDescriptors.CalcMolFormula(molecule),  # type: ignore
            Descriptors.MolWt(molecule),  # type: ignore
            [atom for atom in molecule.GetAtoms()],  # type: ignore
            [bond for bond in molecule.GetBonds()],  # type: ignore
            MolToImage(molecule),  # type: ignore
        )
        return new_compound

    reactants = []
    reagents = []
    products = []

    for key in forms:
        smiles = convert_iupac_to_smiles(forms.get(key))  # type: ignore
        molecule = MolFromSmiles(smiles)
        if molecule is None:
            flash("Please input a valid iupac name of compound", category="error")
            return

        if key.startswith("reactant"):
            reactants.append(get_compound_data(molecule, forms.get(key)))  # type: ignore

        elif key.startswith("reagent"):
            reagents.append(get_compound_data(molecule, forms.get(key)))  # type: ignore

        elif key.startswith("product"):
            products.append(get_compound_data(molecule, forms.get(key)))  # type: ignore

    return Reaction(reactants, reagents, products)

def save_raw_mol_image(name: str):
    smiles = convert_iupac_to_smiles(name)
    molecule = MolFromSmiles(smiles)

    if molecule is None:
        flash("Please input valid iupac name of compound", category="error")
        return False

    img = MolToImage(molecule)
    if isinstance(img, Image):
        img.save(f"ConstructingChemistry/static/compound_images/{name}.png")
        return True
    return False