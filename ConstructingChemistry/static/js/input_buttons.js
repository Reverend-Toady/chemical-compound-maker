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
document.addEventListener("DOMContentLoaded", function () {
    var adding_buttons = {
        reactant: document.getElementById("reactant-button-add"),
        reagent: document.getElementById("reagent-button-add"),
        product: document.getElementById("product-button-add"),
    };
    var removing_buttons = {
        reactant: document.getElementById("reactant-button-remove"),
        reagent: document.getElementById("reagent-button-remove"),
        product: document.getElementById("product-button-remove"),
    };
    var _loop_1 = function (adding_key) {
        adding_buttons[adding_key].addEventListener("click", function () {
            add_input_field(adding_key);
        });
    };
    for (var adding_key in adding_buttons) {
        _loop_1(adding_key);
    }
    var _loop_2 = function (removing_key) {
        removing_buttons[removing_key].addEventListener("click", function () {
            remove_input_field(removing_key);
        });
    };
    for (var removing_key in removing_buttons) {
        _loop_2(removing_key);
    }
});
//# sourceMappingURL=input_buttons.js.map