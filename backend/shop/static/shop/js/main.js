document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById("product-form");
    if (form){

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
    }

    //AJAX
    const text = document.getElementById("ajax-message-text");

    function showMess(message, type="success"){
        text.textContent = message;
    }

    const addToCartForm = document.querySelectorAll('.add-to-cart-form');
    addToCartForm.forEach(cartform => {
        cartform.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(cartform);
            const productId = cartform.dataset.productId;

            const response = await fetch(`/cart/add/${productId}/`, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            });

            const data = await response.json();
            if (data.success) {
                showMess(data.message, "success");
            } else {
                showMess(data.message || "Error adding product", "error");
            }
        });
    });
});