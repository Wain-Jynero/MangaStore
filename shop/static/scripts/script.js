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
const footerBtnCom = document.querySelector('.footer-btn-con');
const footerElemCom = document.querySelector('.footer__company-nav');
let footerElemComCount = 0;
const footerBtnUse = document.querySelector('.footer-btn-use');
const footerElemUse = document.querySelector('.footer__useful-nav');
let footerElemUseCount = 0;
const footerBtnBuy = document.querySelector('.footer-btn-buy');
const footerElemBuy = document.querySelector('.footer__buyer-nav');
let footerElemBuyCount = 0;
const footerBtnCon = document.querySelector('.footer-btn-nav');
const footerElemCon = document.querySelector('.footer__contacts-nav');
const footerElemCon2 = document.querySelector('.contacts-nav');
let footerElemConCount = 0;
let searchCount = 0;
const searchBtn = document.querySelector('.search-img');
const searchElem = document.querySelector('.search-img');
const blockElemHistory = document.querySelector('.order-history-btn');
const buttonElemHistory = document.querySelector('.order-btn');
const elemHistory = document.querySelector('.order-history-pie');
const buttonElemData = document.querySelector('.data-btn');
const blockElemData = document.querySelector('.personal-data-btn');
const elemData = document.querySelector('.personal__data');

let darkLayer = document.createElement('div');

buttonElemReg.addEventListener('click', openModalReg);
buttonElemRegMob.addEventListener('click', openModalReg);
buttonElemAut.addEventListener('click', openModalAut);
buttonElemAutReg.addEventListener('click', openModalReg);
closeElem1.addEventListener('click', closeModal);
closeElem2.addEventListener('click', closeModal);
window.addEventListener('click', closeModalWindow);
searchElem.addEventListener('click', openSearch);
menuElem.addEventListener('click', openMenu);
menuElemClose.addEventListener('click', closeMenu)
footerBtnCom.addEventListener('click', openCom);
footerBtnUse.addEventListener('click', openUse);
footerBtnBuy.addEventListener('click', openBuy);
footerBtnCon.addEventListener('click', openCon);
buttonElemHistory.addEventListener('click', openHistory);
buttonElemData.addEventListener('click', openData);

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
   footerElemComCount++;
   if (footerElemComCount % 2 !==0) {
      footerElemCom.style.display = 'block';
      footerBtnCom.style.rotate = '180deg';
   } else {
      footerElemCom.style.display = 'none';
      footerBtnCom.style.rotate = '360deg';
   }
}

function openBuy() {
   footerElemBuyCount++;
   if (footerElemBuyCount % 2 !==0) {
      footerElemBuy.style.display = 'block';
      footerBtnBuy.style.rotate = '180deg';
   } else {
      footerElemBuy.style.display = 'none';
      footerBtnBuy.style.rotate = '360deg';  
   }
}

function openUse() {
   footerElemUseCount++;
   if (footerElemUseCount % 2 !==0) {
      footerElemUse.style.display = 'block';
      footerBtnUse.style.rotate = '180deg';
   } else {
      footerElemUse.style.display = 'none';
      footerBtnUse.style.rotate = '360deg';
   }
}

function openCon() {
   footerElemConCount++;
   if (footerElemConCount % 2 !==0) {
      footerBtnCon.style.rotate = '180deg';
      footerElemCon.style.display = 'block';
      footerElemCon.style.padding = '2em';
      footerElemCon2.style.display = 'block';
   } else {
      footerBtnCon.style.rotate = '360deg';
      footerElemCon.style.display = 'none';
      footerElemCon.style.padding = '0';
      footerElemCon2.style.display = 'none';
   }
}

function openSearch() {
   searchCount++;
   if (searchCount % 2 !==0) {
      var input = document.createElement('input');
      input.type = 'text';
      input.classList.add('search_input');  
      document.body.appendChild(input);

      input.addEventListener('keydown', function(event) {
         if (event.keyCode === 13) {
            window.location = '/search/?q=' + input.value;
         }
      });
   } else {
      searchInput = document.querySelector('.search_input');
      searchInput.style.display = 'none';
   }
}

function openHistory() {
   buttonElemHistory.style.backgroundColor = '#f3eeee';
   blockElemHistory.style.backgroundColor = '#f3eeee';
   buttonElemData.style.backgroundColor = '#fff';
   blockElemData.style.backgroundColor = '#fff';
   elemData.style.display = 'none';
   elemHistory.style.display = 'block';
}

function openData() {
   buttonElemHistory.style.backgroundColor = '#fff';
   blockElemHistory.style.backgroundColor = '#fff';
   buttonElemData.style.backgroundColor = '#f3eeee';
   blockElemData.style.backgroundColor = '#f3eeee';
   elemData.style.display = 'block';
   elemHistory.style.display = 'none';
}