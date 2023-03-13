import { createStore } from 'vuex'

const store = createStore({
  state: {
    cart: [],
    cartInitialized: false,
    subtotal: 0,
  },
  mutations: {
    addToCart(state, product) {
      const existingItem = state.cart.find(item => item.item_name === product.item_name);
      if (existingItem) {
        existingItem.quantity = 1; // set the quantity to 1
      } else {
        state.cart.push({ ...product, quantity: 1 });
      }
      localStorage.setItem('cartItems', JSON.stringify(state.cart));
    },
    removeFromCart(state, product) {
      const existingItem = state.cart.find(item => item.item_name === product.item_name);
      if (existingItem) {
        if (existingItem.quantity > 1) {
          existingItem.quantity--;
        } else {
          const index = state.cart.indexOf(existingItem);
          state.cart.splice(index, 1);
        }
        existingItem.isInCart = false;
        localStorage.setItem('cartItems', JSON.stringify(state.cart));
      }
    },
    initializeCartFromStorage(state) {
      const cartItems = JSON.parse(localStorage.getItem('cartItems'));
      if (cartItems) {
        state.cart = cartItems.map(item => {
          const product = {...item};
          product.isInCart = true;
          return product;
        }).map(item => {
          const existingItem = state.cart.find(i => i.item_name === item.item_name);
          item.quantity = existingItem ? existingItem.quantity : item.quantity;
          return item;
        });
      }
    },
    clearCart(state) {
        state.cart = [];
        localStorage.removeItem('cartItems');
      },
  },
  getters: {
    cart: (state) => state.cart,
    totalItems: (state) => {
      return state.cart.reduce((total, item) => {
        return total + item.quantity;
      }, 0);
    },
    subtotal: (state) => {
        let sum = 0;
        for (const item of state.cart) {
          sum += item.item_price * item.quantity;
        }
        return sum.toFixed(2);
      }
  },
});

export default store



