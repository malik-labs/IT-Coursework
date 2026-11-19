document.addEventListener("DOMContentLoaded", function () {
    const cartIcon = document.getElementById('cart-icon');
    const cartDropdown = document.getElementById('cart-dropdown');
    const cartItemsDiv = document.getElementById('cart-items');

    // Load cart preview into dropdown
    function loadCartPreview() {
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        cartItemsDiv.innerHTML = cart.length
            ? cart.map(item => `<p>${item.quantity}× ${item.name} – £${item.price}</p>`).join('')
            : '<p>Your cart is empty.</p>';
    }

    // Toggle cart dropdown
    if (cartIcon) {
        cartIcon.addEventListener('click', function () {
            loadCartPreview();
            cartDropdown.style.display = cartDropdown.style.display === 'block' ? 'none' : 'block';
        });
    }

    // Add to cart on product page
    if (location.pathname.includes('product.html')) {
        const addToCartBtn = document.getElementById('add-to-cart-btn');
        if (addToCartBtn) {
            addToCartBtn.addEventListener('click', function (e) {
                e.preventDefault();

                const color = document.querySelector('input[name="color"]:checked')?.value || 'Default';
                const quantity = parseInt(document.getElementById('quantity')?.value) || 1;

                const cart = JSON.parse(localStorage.getItem('cart')) || [];

                cart.push({
                    name: `Smart Lunchbox (${color})`,
                    price: 25.99,
                    quantity: quantity
                });

                localStorage.setItem('cart', JSON.stringify(cart));
                alert('Item added to cart');
            });
        }
    }
});
