const buttonElement = document.querySelector('.btn-danger');
const modalElement = document.querySelector('.token-modal');

modalElement.style.cssText = `
    display: flex;
    visibility: hidden;
    opacity: 0;
    z-index: 9999;
    transition: opacity 300ms easy-in-out;
`;

const closeModal = event => {
    const target = event.target;

    if(target == modalElement || target.closest(".btn-secondary")){
        modalElement.style.opacity = 0;
        setTimeout(() => {
            modalElement.style.visibility = 'hidden';
        }, 300)
    }
}

const openModal = () => {
    modalElement.style.visibility = 'visible';
    modalElement.style.opacity = 1;
}

buttonElement.addEventListener('click', openModal);
modalElement.addEventListener('click', closeModal);
