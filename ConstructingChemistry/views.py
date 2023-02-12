from flask import Blueprint, render_template, request, jsonify

from .models import Compound
from .api.process_raw_input import process_raw_input, save_raw_mol_image

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

@views.route("/get_image", methods= ["POST"])
def get_image():
    data = request.get_json()
    if data:
        img_name = data["data"]
        if not save_raw_mol_image(img_name):
            return {"worked?": "False"}
        return {"worked?": "True"}
    return {"worked?": "NotSure"}
