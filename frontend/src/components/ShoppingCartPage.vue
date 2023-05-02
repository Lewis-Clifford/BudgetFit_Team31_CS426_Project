<template >
    <section class="pt-5 pb-5">
  <div class="container p-5">
    <div class="row w-100">
        <div class="col-lg-12 col-md-12 col-12">
            <h3 class="display-5 mb-2 text-center">{{this.listName}}    <font-awesome-icon v-if="priority !== ''"
        :icon="['fa', 'circle']"
        :style="{
          color: priority === 'low' ? '#72b264' : priority === 'medium' ? '#ffc107' : '#f44336',
          '--fa-animation-delay': '1s',
          '--fa-animation-duration': '1.3s',
          '--fa-animation-iteration-count': '2',
        }"
        bounce></font-awesome-icon></h3>
            
            <p class="text-center mb-5">
              {{this.description ? this.description : ''}}
          </p>


            <table id="shoppingCart" class="table table-condensed table-responsive">
              <thead>
                <tr>
                  <th style="width: 45%">Product</th>
                  <th style="width: 15%">Calories</th>
                  <th style="width: 12%">Price</th>
                  <th style="width: 10%">Quantity</th>
                  <th style="width: 18%"></th>
                </tr>
              </thead>
                <tbody>
                    <tr v-for="product in cart" :key="product.item_name">
                      <td data-th="Product">
                          <div class="row">
                              <div class="col-md-3 text-start">
                                  <img :src="product.images_front_full_url" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow">
                              </div>
                              <div class="col-md-9 text-start mt-sm-1">
                                  <h4>{{product.item_name}}</h4>
                                  <p class="font-weight-light">{{product.brand_name}}</p>
                                  <p class="alert alert-danger" role="alert">Hazard: Remove item, contains ingredient(s) that will cause you an allergic reaction.</p>
                                  <button class="btn Expand"  @click="product.showInfo = !product.showInfo"><font-awesome-icon :icon="product.showInfo ? 'fa-solid fa-angles-up' : 'fa-solid fa-angles-down'"></font-awesome-icon></button>
                                  <div v-if="product.showInfo">
                                    
                                    <span v-if="product.nf_calories_from_fat !== null"><b>Calories from Fat:</b> {{ product.nf_calories_from_fat }}</span>
                                    <p v-if="product.nf_total_fat !== null"><b>Total Fat:</b> {{ product.nf_total_fat }}g </p>
                                    <span v-if="product.nf_saturated_fat !== null"><b>Saturated Fat:</b> {{ product.nf_saturated_fat }}g </span>
                                    <span v-if="product.nf_trans_fatty_acid !== null"><b>Trans Fatty Acid:</b> {{ product.nf_trans_fatty_acid }}g </span>
                                    <span v-if="product.nf_polyunsaturated_fat !== null"><b>Polyunsaturated Fat:</b> {{ product.nf_polyunsaturated_fat }}g </span>
                                    <span v-if="product.nf_monounsaturated_fat !== null"><b>Monounsaturated Fat:</b> {{ product.nf_monounsaturated_fat }}g </span>
                                    <span v-if="product.nf_cholesterol !== null"><b>Cholesterol:</b> {{ product.nf_cholesterol }}mg </span>
                                    <p v-if="product.nf_sodium !== null"><b>Sodium:</b> {{ product.nf_sodium }}mg </p>
                                    <p v-if="product.nf_total_carbohydrate !== null"><b>Total Carbohydrate:</b> {{ product.nf_total_carbohydrate }}g </p>
                                    <span v-if="product.nf_dietary_fiber !== null"><b>Dietary Fiber:</b> {{ product.nf_dietary_fiber }}g </span>
                                    <span v-if="product.nf_sugars !== null"><b>Sugars:</b> {{ product.nf_sugars }}g </span>
                                    <p v-if="product.nf_protein !== null"><b>Protein:</b> {{ product.nf_protein }}g </p>
                                    <span v-if="product.nf_vitamin_a_dv !== null"><b>Vitamin A:</b> {{ product.nf_vitamin_a_dv }}% </span>
                                    <span v-if="product.nf_vitamin_c_dv !== null"><b>Vitamin C:</b> {{ product.nf_vitamin_c_dv }}% </span>
                                    <span v-if="product.nf_calcium_dv !== null"><b>Calcium:</b> {{ product.nf_calcium_dv }}% </span>
                                    <span v-if="product.nf_iron_dv !== null"><b>Iron:</b> {{ product.nf_iron_dv }}% </span>
                                    <span v-if="product.nf_potassium !== null"><b>Potassium:</b> {{ product.nf_potassium }}mg </span>
                                    <p v-if="product.nf_servings_per_container !== null"><b>Servings Per Container:</b> {{ product.nf_servings_per_container }}</p>
                                    <span v-if="product.nf_serving_size_qty !== null && product.nf_serving_size_unit !== null"><b>Serving Size:</b> {{ product.nf_serving_size_qty }} {{ product.nf_serving_size_unit }}</span>
                                    <p  v-if="product.nf_ingredient_statement !== null"><b>Ingredients:</b> {{ product.nf_ingredient_statement }}</p>
                                  </div>
                              </div>
                          </div>
                      </td>
                        <td data-th="Calories">{{product.nf_calories}}</td>
                        <td data-th="Price">{{product.item_price}}</td>
                        <td data-th="Quantity">
                        <input type="number" min="1" max="16" class="form-control form-control-lg text-center" v-model="product.quantity" @change="updateQuantity(product, product.quantity); updateSubtotal()">
                    </td>
                        <td class="actions" data-th="">
                            <div class="text-end">
                                <button @click="removeItem(product), removeProduct(product.productsID)" class="btn btn-lg btn-light hvr-shrink">
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
          <a @click="delayRoute">
            <button class="btn btn-primary btn-block custom-button mb-4 btn-lg px-5" @click="updateCart()">Finalize List</button>
          </a>
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

import { mapGetters} from 'vuex';
import axios from 'axios';
import FinalList from './FinalList.vue';
export default {
    name: 'Cart',
    components:{
      FinalList
    },
    data() {
        return{
            listName: '',
            description: '',
            priority: '',
            ID: [],
            quantity: []
            
        }
    },
    methods: {
    goBack() {
      this.$router.back()
    },
    delayRoute() {
    setTimeout(() => {
      this.$router.push('finallist');
    }, 1500); // Delay the route navigation for 1 second (1000 milliseconds)
  },
    async removeProduct(productsID) {
            const userID = localStorage.getItem('userID');
            const listName = localStorage.getItem('activeList');
             axios.delete(`http://localhost:5000/newList?userID=${userID}&productsID=${productsID}&listName=${listName}`)
                .then(response => {

                })
                .catch(error => {console.log(error);
                }) 
                await new Promise((r) => setTimeout(r, 1500));
        },
    async updateCart() {


      let data = [];

this.cartItems.forEach(product => {
  const item = {
    userID: localStorage.getItem('userID'),
    productID: product.productsID,
    listname: localStorage.getItem('activeList'),
    priority: localStorage.getItem('activePriority'),
    description: localStorage.getItem('activeDescription'),
    quantity: product.quantity
  };
  data.push(item);
});

axios.post('http://127.0.0.1:5000/lists', data)
  .then(response => {
    console.log(response);
  })
  .catch(error => {
    console.log(error);
  });
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
created(){
  this.listName = localStorage.getItem('activeList')
  this.description = localStorage.getItem('activeDescription')
  this.priority = localStorage.getItem('activePriority')

  
}
    
}
</script>
<style scoped>
.Expand{
border: none;
outline: none;
position: relative;
left: -10px;
top: -10px;
}



</style>
