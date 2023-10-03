const buttonElemReg = document.querySelector('.autorization__btn');
const buttonElemRegMob = document.querySelector('.autorization__btn-mobile');
const buttonElemAut = document.querySelector('.regisration__btn');
const buttonElemAutReg = document.querySelector('.autorization__btn-reg');
const closeElem1 = document.querySelector('.modal__close1');
const closeElem2 = document.querySelector('.modal__close2');
const regElem = document.querySelector('.modal__registration');
const autElem = document.querySelector('.modal__autorization');
const menuElem = document.querySelector('.mobile-menu-btn');
const menuLi = document.querySelector('.mobile-menu__container');
const menuElemClose = document.querySelector('.mobile-menu-close');
const footerBtnCom = document.querySelector('.footer-btn-com');
const footerElemCom = document.querySelector('.footer__company-nav');
const footerBtnUse = document.querySelector('.footer-btn-use');
const footerElemUse = document.querySelector('.footer__useful-nav');
const footerBtnBuy = document.querySelector('.footer-btn-buy');
const footerElemBuy = document.querySelector('.footer__buyer-nav');
const footerBtnCon = document.querySelector('.footer-btn-con');
const footerElemCon = document.querySelector('.footer__contacts-nav');
const footerElemCon2 = document.querySelector('.contacts-nav');
let darkLayer = document.createElement('div');

buttonElemReg.addEventListener('click', openModalReg);
buttonElemRegMob.addEventListener('click', openModalReg);
buttonElemAut.addEventListener('click', openModalAut);
buttonElemAutReg.addEventListener('click', openModalReg);
closeElem1.addEventListener('click', closeModal);
closeElem2.addEventListener('click', closeModal);
window.addEventListener('click', closeModalWindow);
menuElem.addEventListener('click', openMenu);
menuElemClose.addEventListener('click', closeMenu)
footerBtnCom.addEventListener('click', openCom);
footerBtnUse.addEventListener('click', openUse);
footerBtnBuy.addEventListener('click', openBuy);
footerBtnCon.addEventListener('click', openCon);

function openModalReg() {
   regElem.style.display = 'block';
   autElem.style.display = 'none';

   darkLayer.id = 'shadow';
   document.body.appendChild(darkLayer);
}

function openModalAut() {
   regElem.style.display = 'none';
   autElem.style.display = 'block';

   darkLayer.id = 'shadow';
   document.body.appendChild(darkLayer);
}

function closeModal() {
   regElem.style.display = 'none';
   autElem.style.display = 'none';

   darkLayer.parentNode.removeChild(darkLayer);
}

function closeModalWindow() {
   darkLayer.onclick = function () {
      darkLayer.parentNode.removeChild(darkLayer);
      regElem.style.display = 'none';
      autElem.style.display = 'none';
      return false;
   };
}

function openMenu() {
   menuLi.style.display = 'block';
   menuElem.style.display = 'none';
   menuElemClose.style.display = 'block';
}

function closeMenu() {
   menuLi.style.display = 'none';
   menuElem.style.display = 'block';
   menuElemClose.style.display = 'none';
}

function openCom() {
   footerElemCom.style.display = 'block';
}

function openBuy() {
   footerElemBuy.style.display = 'block';
}

function openUse() {
   footerElemUse.style.display = 'block';
}

function openCon() {
   footerElemCon.style.display = 'block';
   footerElemCon2.style.display = 'block';
}