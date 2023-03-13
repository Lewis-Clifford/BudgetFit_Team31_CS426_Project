<template >
    <section class="pt-5 pb-5">
  <div class="container p-5">
    <div class="row w-100">
        <div class="col-lg-12 col-md-12 col-12">
            <h3 class="display-5 mb-2 text-center">"Grocery List Name"</h3>
            <p v-if="cart.length === 0" class="mb-5 text-center">
            You have no products in your list
          </p>
          <p v-else-if="cart.length==1" class="mb-5 text-center">
            You have <i class="text-success">1</i> products in your list
          </p>
          <p v-else class="mb-5 text-center">
             You have <i class=" text-success ">{{ cart.length }}</i> products in your list
          </p>
            <table id="shoppingCart" class="table table-condensed table-responsive">
                <thead>
                    <tr>
                        <th style="width:60%">Product</th>
                        <th style="width:12%">Price</th>
                        <th style="width:10%">Quantity</th>
                        <th style="width:16%"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="product in cart" :key="product.item_name">
                        <td data-th="Product">
                            <div class="row">
                                <div class="col-md-3 text-start">
                                    <img :src="product.images_front_full_url" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow ">
                                </div>
                                <div class="col-md-9 text-start mt-sm-2">
                                    <h4>{{product.item_name}}</h4>
                                    <p class="font-weight-light">{{product.brand_name}}</p>
                                    <!-- <p class="alert alert-danger" role="alert">Hazard: Remove item, contains ingredient(s) that will cause you an allergic reaction.</p> -->
                                </div>
                            </div>
                        </td>
                        <td data-th="Price">{{product.item_price}}</td>
                        <td data-th="Quantity">
                        <input type="number" min="1" max="16" class="form-control form-control-lg text-center" v-model="product.quantity" @change="updateQuantity(product, product.quantity); updateSubtotal()">
                    </td>
                        <td class="actions" data-th="">
                            <div class="text-end">
                                <button @click="removeItem(product)" class="btn btn-lg btn-light hvr-shrink">
                                    <font-awesome-icon icon="fa-solid fa-trash"></font-awesome-icon>
                                </button>

                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="float-end text-end">
                <h4>Subtotal:</h4>
                <h1>${{ $store.getters.subtotal }}</h1>
            </div>
        </div>
    </div>
    <div class="row mt-4 d-flex align-items-center">
        <div class="col-sm-6 order-md-2 text-end">
          <router-link to="finallist">
            <button  class="btn btn-primary btn-block custom-button mb-4 btn-lg px-5">Finalize List</button>
          </router-link>
          </div>
        <div class="col-sm-6 mb-3 mb-m-1 order-md-1 text-md-start">
            <a class="btn btn-light hvr-shrink" @click="goBack">
                <font-awesome-icon icon="fa-solid fa-arrow-left mr-2"></font-awesome-icon> Continue Browsing
            </a>
        </div>
    </div>
</div>
</section>
</template>
<script>
import router from '@/router';
import { mapGetters} from 'vuex';
import FinalList from './FinalList.vue';
export default {
    name: 'Cart',
    components:{
      FinalList
    },
    methods: {
    goBack() {
      this.$router.back()
    },
    emptyCart() {
      this.$store.commit('clearCart');
      this.cart = [];
    },
    updateQuantity(product, quantity) {
    product.quantity = parseInt(quantity);
    product.price = product.item_price * product.quantity;
  },
    updateSubtotal() {
    let subtotal = 0;
    this.cartItems.forEach(product => {
    if (product.quantity > 1) {
      subtotal += product.price * product.quantity;
    } else {
      subtotal += product.price;
    }
  });
    this.$store.commit('setSubtotal', subtotal);
},
        removeItem(product) {
  this.$store.commit('removeFromCart', product);
  this.updateSubtotal();
}
  }, 
        
  mutations: {
  addToCart(state, product) {
    const existingItem = state.cart.find(item => item.id === product.id);
    if (existingItem) {
      existingItem.quantity++;
    } else {
      state.cart.push({ ...product, quantity: 1 });
    }
  },

},
computed: {
  ...mapGetters(['cart', 'subtotal']),
  cartItems() {
    return this.cart.map(item => ({
      ...item,
      name: item.item_name,
      price: item.item_price,
      quantity: item.quantity
    }));
  }
},
    
}
</script>
<style>
    
</style>
