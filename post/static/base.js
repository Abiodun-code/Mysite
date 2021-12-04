const navOpen = document.querySelector('.menu')
const navMenu = document.querySelector('.base-head')

navOpen.addEventListener('click', () => {
    navMenu.classList.toggle('show_menu')
})