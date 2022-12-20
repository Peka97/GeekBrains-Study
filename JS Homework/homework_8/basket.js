const rightHeaderEl = document.querySelector('.rightHeader');
const cartIconEl = document.querySelector('.cartIcon');
const basketEl = document.querySelector('.basket');
const cartCounterEl = document.querySelector('.cartCounter');
const basketTotalEl = document.querySelector('.basketTotal');
rightHeaderEl.addEventListener('click', event => {
    if (event.target !== cartIconEl) {
        return;
    } else {
        basketEl.classList.toggle('hidden');
    }
});

class BasketObj {
    constructor() {
        this.content = Array();
    }

    addItem(obj) {
        for (let el of this.content) {
            if (el.id === obj.id) {
                el.count++;
                return;
            }
        }
        this.content.push(obj);
    }

    getTotalPrice() {
        let result = 0
        for (let el of this.content) {
            result += el.price * el.count
        }
        return result;
    }

    updateCart() {
        const basketTotalValueEl = document.querySelector('.basketTotalValue');
        for (let el of this.content) {
            const rowFromIdEl = document.querySelector(`.basketRow[data-id="${el.id}"]`)
            if (rowFromIdEl === null) {
                const productRow = `
                <div class="basketRow" data-id="${el.id}">
                <div class="productName">${el.name}</div>
                <div>
                    <span class="productCount">${el.count} шт.</span> 
                </div>
                <div class="productPrice">$${el.price}</div>
                <div>
                    <span class="productTotalRow">$${(el.price * el.count).toFixed(2)}</span>
                </div>
                </div>
            `;
                basketTotalEl.insertAdjacentHTML("beforebegin", productRow);
            } else {
                rowFromIdEl.childNodes[3].childNodes[1].textContent = `${el.count} шт.`;
                rowFromIdEl.childNodes[7].childNodes[1].textContent = `$${(el.price * el.count).toFixed(2)}`;
            }
        }
        basketTotalValueEl.textContent = this.getTotalPrice();
    }

}


const Basket = new BasketObj();
document.querySelector('.featuredItems').addEventListener('click', event => {
    if (!event.target.tagName === 'BUTTON') {
        return;
    } else {
        const featuredItemEl = event.target.closest('.featuredItem');
        const id = +featuredItemEl.dataset.id;
        const name = featuredItemEl.dataset.name;
        const price = +featuredItemEl.dataset.price;
        const data = {
            id: id,
            name: name,
            price: price,
            count: 1,
        }

        Basket.addItem(data);
        Basket.updateCart();

        cartCounterEl.textContent++;
    }
})