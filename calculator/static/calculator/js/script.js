document.addEventListener('DOMContentLoaded', () => {

    console.log('DOM Loaded');


    const form = document.querySelectorAll('form');
    const input = document.querySelectorAll('input');

    form.classList.add('form-group');
    input.classList.add('form-control');
});