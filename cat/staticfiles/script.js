// Slider Auto Change
let index = 0;
function changeSlide() {
    const slides = document.querySelectorAll('.slider img');
    slides.forEach((slide, i) => {
        slide.style.display = i === index ? 'block' : 'none';
    });
    index = (index + 1) % slides.length;
}
setInterval(changeSlide, 3000);

// Change the main product image when a thumbnail is clicked
function changeImage(imageUrl) {
    document.getElementById('main-image').src = imageUrl;
}

// Add to Cart Functionality (placeholder)
function addToCart() {
    const quantity = document.getElementById('quantity').value;
    alert(`Added ${quantity} item(s) to the cart!`);
}

function changeImage(imageUrl) {
    document.getElementById("main-image").src = imageUrl;
}
function changeImage(imageUrl) {
    document.getElementById("main-image").src = imageUrl;
}

document.addEventListener("DOMContentLoaded", function () {
    let cartCount = localStorage.getItem("cartCount") || 0;
    document.getElementById("cart-count").innerText = cartCount;
});



