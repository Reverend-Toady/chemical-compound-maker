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

function set_image(
  input_element: HTMLInputElement,
  img_element: HTMLImageElement
) {
  let timeout: number;
  input_element.addEventListener("input", () => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      let reactant_iupac = input_element.value;
      fetch("/get_image", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: reactant_iupac }),
      })
        .then((response) => response.json())
        .then((data) => {
          img_element.src = "static/compound_images/" + reactant_iupac + ".png";
          img_element.style["display"] = "flex";
          input_element.style["display"] = "none";
        });
    }, 1000);
  });
}

function set_input(
  input_element: HTMLInputElement,
  img_element: HTMLImageElement
) {
  img_element.addEventListener("click", () => {
    img_element.src = "#";
    img_element.style["display"] = "none";
    input_element.style["display"] = "flex";
  });
}

document.addEventListener("DOMContentLoaded", () => {
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

  let reactant_input = document.getElementById("reactant") as HTMLInputElement;
  let reactant_image = document.getElementById(
    "reactant-image"
  ) as HTMLImageElement;

  set_image(reactant_input, reactant_image);
  set_input(reactant_input, reactant_image);

  let reagent_input = document.getElementById("reagent") as HTMLInputElement;
  let reagent_image = document.getElementById(
    "reagent-image"
  ) as HTMLImageElement;

  set_image(reagent_input, reagent_image);
  set_input(reagent_input, reagent_image);

  let product_input = document.getElementById("product") as HTMLInputElement;
  let product_image = document.getElementById(
    "product-image"
  ) as HTMLImageElement;

  set_image(product_input, product_image);
  set_input(product_input, product_image);
});
