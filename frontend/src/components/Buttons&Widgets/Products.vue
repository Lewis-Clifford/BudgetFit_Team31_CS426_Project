<template>
  <div>
    <div class="row">
    <div class="col-12 col-md-6 col-lg-4 mb-3" v-for="product in list" :key="product.productsID">
      <div class="card h-100 border-0" style="max-width: 240px">
        <div class="card-img-top position-relative">
          <img :src="product.images_front_full_url" class="img-fluid mx-auto d-block" @click="showPopup(product)" style="cursor: pointer;">
          <FavoriteComponent :item="product"/>
          <ButtonComponent :disabled="isActive" @click="toggleCart(product)" :item="product" />

        </div>
        <div class="card-body text-center">
          <h4 class="card-title">
            <a @click="showPopup(product)" style="cursor: pointer;" class="text-decoration-none text-dark small">{{ product.item_name }}</a>
          </h4>
          <h5 class="card-price small font-weight-bold mb-3">
            <p>{{ product.brand_name }}</p>
            <i>${{ product.item_price }}</i>
          </h5>
        </div>
      </div>
      <PopupComponent v-if="popupProduct" :product="popupProduct" @close="closePopup"/>
    </div>
  </div>
  
  </div>
</template>

<script>
import ButtonComponent from './AddButtonShop.vue';
import FavoriteComponent from './AddFavoriteShop.vue';
import PopupComponent from './ProductPopUp.vue';
import { mapMutations, mapState } from 'vuex';

export default {
  name: 'Products',
  props: ['cartItems', 'products', 'list'],
  components: {
    ButtonComponent,
    FavoriteComponent,
    PopupComponent
  },
  computed: {
...mapState(['cart'])
  },
  methods: {
    ...mapMutations(['addToCart', 'removeFromCart']),
    toggleCart(product) {
    product.isInCart = !product.isInCart;
    if (product.isInCart) {
      this.addToCart(product);
    } else {
      this.removeFromCart(product);
    }
  },
  showPopup(product) {
      this.popupProduct = product;
    },
    closePopup() {
      this.popupProduct = null;
    }
  },
  data() {
    return {
      popupProduct: null,
    }
  },
  mounted(){
    
  }
}
</script>

<style>
</style>