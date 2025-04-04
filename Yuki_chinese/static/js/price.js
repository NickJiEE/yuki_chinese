document.addEventListener("DOMContentLoaded", function () {
    const tierSelect = document.getElementById("tier-select");
    const hoursInput = document.getElementById("hours-input");
    const totalPrice = document.getElementById("total-price");
    const errorMessage = document.getElementById("error-message"); // Error message display

    const prices = {
        1: 109, // Tier 1 hourly rate
        2: 86,  // Tier 2 hourly rate
        3: 74   // Tier 3 hourly rate
    };

    const discounts = {
        1: { 6: 588 },
        2: { 6: 468 },
        3: { 6: 399 }
    };

    function calculatePrice() {
        const tier = parseInt(tierSelect.value);
        const hours = parseInt(hoursInput.value);

        // Reset error message
        errorMessage.textContent = "";

        // Check for invalid input
        if (!tier || isNaN(hours) || hours < 1) {
            totalPrice.textContent = "$0";
            return;
        }

        // Check if hours exceed the limit
        if (hours >= 13) {
            errorMessage.textContent = "Error: The maximum booking time is 12 hours.";
            totalPrice.textContent = "$0";
            return;
        }

        let cost;

        if (hours === 6) {
            cost = discounts[tier][hours]; // Use discount price for 6 or 11 hours
        } else if (hours > 6) {
            const extraHours = hours - 6;
            cost = discounts[tier][6] + (extraHours * prices[tier]); // Combo + extra hours
        } else {
            cost = hours * prices[tier]; // Normal hourly rate
        }

        totalPrice.textContent = `$${cost}`;
    }

    tierSelect.addEventListener("change", calculatePrice);
    hoursInput.addEventListener("input", calculatePrice);
});