let counter = 0;

function add_input_field(type: string) {
  let container = document.getElementById(type + "-group") as HTMLDivElement;
  let new_input_field = document.createElement("input") as HTMLInputElement;
  new_input_field.type = "text";
  new_input_field.className = "form-control";
  new_input_field.id = type;
  new_input_field.name = type + "-" + counter;
  new_input_field.placeholder =
    "Enter " + type.charAt(0).toUpperCase() + type.substring(1);
  container.appendChild(new_input_field);
  counter++;
}

function remove_input_field(type: string) {
  let container = document.getElementById(type + "-group") as HTMLDivElement;
  if (container.lastElementChild) {
    container.removeChild(container.lastElementChild);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const adding_buttons: { [key: string]: HTMLButtonElement } = {
    reactant: document.getElementById(
      "reactant-button-add"
    ) as HTMLButtonElement,
    reagent: document.getElementById("reagent-button-add") as HTMLButtonElement,
    product: document.getElementById("product-button-add") as HTMLButtonElement,
  };

  const removing_buttons: { [key: string]: HTMLButtonElement } = {
    reactant: document.getElementById(
      "reactant-button-remove"
    ) as HTMLButtonElement,
    reagent: document.getElementById(
      "reagent-button-remove"
    ) as HTMLButtonElement,
    product: document.getElementById(
      "product-button-remove"
    ) as HTMLButtonElement,
  };

  for (let adding_key in adding_buttons) {
    adding_buttons[adding_key].addEventListener("click", () => {
      add_input_field(adding_key);
    });
  }

  for (let removing_key in removing_buttons) {
    removing_buttons[removing_key].addEventListener("click", () => {
      remove_input_field(removing_key);
    });
  }
});
