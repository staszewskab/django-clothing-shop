document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById("product-form");
    if (!form)
        return

    const saveBtn = document.getElementById("save-button");
    const requiredFields = form.querySelectorAll("input, textarea, select")

    function validateField(field){
        let valid = true;

        if (field.type === "file") {
            valid = field.files.length > 0  || field.dataset.hasFile === "true";
        }
        else if (field.type === "checkbox") {
            valid = true;
        }
        else {
            valid = field.value.trim() !== "";
        }

        if (field.name === "price" && parseFloat(field.value) <= 0) {
            valid = false;
        }

        if (field.name === "stock" && parseInt(field.value) < 0) {
            valid = false;
        }

        field.classList.toggle("error", !valid);
        return valid;
    }

    function validateForm() {
        let isValid = true;
        requiredFields.forEach(field => {
            if (!validateField(field)) {
                isValid = false;
            }
        });
        saveBtn.disabled = !isValid;
    }

    requiredFields.forEach(field => {
        field.addEventListener("change", validateForm);
    });

    validateForm();

})