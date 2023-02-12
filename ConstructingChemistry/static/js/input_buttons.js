var counter = 0;
function add_input_field(type) {
    var container = document.getElementById(type + "-group");
    var new_input_field = document.createElement("input");
    new_input_field.type = "text";
    new_input_field.className = "form-control";
    new_input_field.id = type;
    new_input_field.name = type + "-" + counter;
    new_input_field.placeholder =
        "Enter " + type.charAt(0).toUpperCase() + type.substring(1);
    container.appendChild(new_input_field);
    counter++;
}
function remove_input_field(type) {
    var container = document.getElementById(type + "-group");
    if (container.lastElementChild) {
        container.removeChild(container.lastElementChild);
    }
}
function set_image(input_element, img_element) {
    var timeout;
    input_element.addEventListener("input", function () {
        clearTimeout(timeout);
        timeout = setTimeout(function () {
            var reactant_iupac = input_element.value;
            fetch("/get_image", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ data: reactant_iupac }),
            })
                .then(function (response) { return response.json(); })
                .then(function (data) {
                img_element.src = "static/compound_images/" + reactant_iupac + ".png";
                img_element.style["display"] = "flex";
                input_element.style["display"] = "none";
            });
        }, 1000);
    });
}
function set_input(input_element, img_element) {
    img_element.addEventListener("click", function () {
        img_element.src = "#";
        img_element.style["display"] = "none";
        input_element.style["display"] = "flex";
    });
}
document.addEventListener("DOMContentLoaded", function () {
    // const adding_buttons: { [key: string]: HTMLButtonElement } = {
    //   reactant: document.getElementById(
    //     "reactant-button-add"
    //   ) as HTMLButtonElement,
    //   reagent: document.getElementById("reagent-button-add") as HTMLButtonElement,
    //   product: document.getElementById("product-button-add") as HTMLButtonElement,
    // };
    // const removing_buttons: { [key: string]: HTMLButtonElement } = {
    //   reactant: document.getElementById(
    //     "reactant-button-remove"
    //   ) as HTMLButtonElement,
    //   reagent: document.getElementById(
    //     "reagent-button-remove"
    //   ) as HTMLButtonElement,
    //   product: document.getElementById(
    //     "product-button-remove"
    //   ) as HTMLButtonElement,
    // };
    // for (let adding_key in adding_buttons) {
    //   console.log(adding_buttons[adding_key])
    //   adding_buttons[adding_key].addEventListener("click", () => {
    //     add_input_field(adding_key);
    //   });
    // }
    // for (let removing_key in removing_buttons) {
    //   removing_buttons[removing_key].addEventListener("click", () => {
    //     remove_input_field(removing_key);
    //   });
    // }
    var reactant_input = document.getElementById("reactant");
    var reactant_image = document.getElementById("reactant-image");
    set_image(reactant_input, reactant_image);
    set_input(reactant_input, reactant_image);
    var reagent_input = document.getElementById("reagent");
    var reagent_image = document.getElementById("reagent-image");
    set_image(reagent_input, reagent_image);
    set_input(reagent_input, reagent_image);
    var product_input = document.getElementById("product");
    var product_image = document.getElementById("product-image");
    set_image(product_input, product_image);
    set_input(product_input, product_image);
});
//# sourceMappingURL=input_buttons.js.map