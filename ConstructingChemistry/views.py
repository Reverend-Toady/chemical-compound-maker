from flask import Blueprint, render_template, request, flash, redirect, url_for
from rdkit.Chem import MolFromSmiles  # type: ignore
from rdkit.Chem.Draw import MolToImage
import pubchempy

import io
from pickle import dumps as pickle_dumps
from .models import Compound
from .app import db


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        smile_compound = request.form.get("smile")
        molecule = MolFromSmiles(smile_compound)

        if molecule is None:
            flash("Please input a valid organic chemical compound", category="error")
        else:
            compound = pubchempy.get_compounds(smile_compound, namespace="smiles")[0]
            compound_cid = compound.cid
            compound_name = compound.iupac_name
            compound_formula = compound.molecular_formula
            compound_weight = compound.molecular_weight
            compound_atoms = pickle_dumps(compound.atoms)
            compound_bonds = pickle_dumps(compound.bonds)

            img = MolToImage(molecule) 
            stream = io.BytesIO() # type: ignore
            img.save(stream, format="png") # type: ignore
            img_bytes = stream.getvalue()

            new_compound = Compound(
                cid=compound_cid,
                name=compound_name,
                formula=compound_formula,
                weight=compound_weight,
                atoms=compound_atoms,
                bonds=compound_bonds,
                image=img_bytes,
            )
            db.session.add(new_compound)
            db.session.commit()

            return redirect(url_for("views.home"))

    return render_template("home.html")
