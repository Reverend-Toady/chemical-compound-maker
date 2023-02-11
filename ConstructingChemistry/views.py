from flask import Blueprint, render_template, request, flash, redirect, url_for

import io
from pickle import dumps as pickle_dumps
from .models import Compound
from .app import db
from .api.process_raw_input import process_raw_input

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        reaction = process_raw_input(request.form)
        print(reaction)

        #     new_compound = Compound(
        #         cid=compound_cid,
        #         name=compound_name,
        #         formula=compound_formula,
        #         weight=compound_weight,
        #         atoms=compound_atoms,
        #         bonds=compound_bonds,
        #         image=img_bytes,
        #     )
        #     db.session.add(new_compound)
        #     db.session.commit()

        #     return redirect(url_for("views.home"))

    return render_template("home.html")
