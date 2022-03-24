let burger = document.querySelector('.burger');
let burgerLine1 = document.querySelector('.burger-line-1');
let burgerLine2 = document.querySelector('.burger-line-2');
let burgerLine3 = document.querySelector('.burger-line-3');
let navBar = document.querySelector('.nav-bar');
let loginBtn = document.querySelector('.login-btn')
burger.addEventListener('click', () => {
    console.log('clicked');

    navBar.classList.toggle('active');
    loginBtn.classList.toggle('active');

    burgerLine1.classList.toggle('toggle');
    burgerLine2.classList.toggle('toggle');
    burgerLine3.classList.toggle('toggle');
});
