<template >
<div class="popup-overlay" @click.self="$emit('close')">
<div class="popup-container">
    <div class="popup-content">
  
<img :src="product.images_front_full_url" style="max-width: 240px; max-height: 240px" alt="Placeholder image">
  <p>{{ product.item_name }}</p>
  <p>{{product.brand_name}}</p>
  <p>${{product.item_price}}</p>
  <button class="popup-close" @click="$emit('close')">
    <font-awesome-icon icon="fa-solid fa-x"/></button>
    <button class="btn btn-primary "
    :class="{active : isActive}"
    :key="itemCount"
    @click="toggle">
    <i v-if="isActive">Item added to List</i>
    <i v-if="!isActive">Add Item to List</i>
    </button>
  </div>
</div>
</div>

</template>
<script>
import { mapState, mapMutations } from 'vuex';
import FavoriteComponent from './AddFavoriteShop.vue';
export default {
    name: 'PopupComponent',
    components: {
      FavoriteComponent
    },
    props:['product'],

    computed: {
      ...mapState(['cart']),
    itemCount() {
      const product = this.cart.find(i => i.item_name === this.product.item_name);
      return product ? product.quantity : 0;
    },
    isActive() {
      return this.itemCount > 0
    }
    },
    methods: {
    ...mapMutations(['addToCart', 'removeFromCart']),
    toggle() {
      const isInCart = this.isActive;
      if (isInCart) {
        this.removeFromCart(this.product);
      } else {
        this.addToCart(this.product);
      }
    },
  }

}
</script>
<style scoped>

i {
font-style: normal;
}

.btn.btn-primary.active {
  background-color: rgb(206, 217, 82);
  border-color: rgb(206, 217, 82);
}
    .popup-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  width: 80%;
  max-width: 600px;
  height: 80%;
  max-height: 600px;
  background-color: white;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.04);

}

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.04);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 3;
}

.popup-close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 20px;
  font-weight: bold;
  background-color: transparent;
  border: none;
  cursor: pointer;
  outline: none;
}

.popup-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 25px;
}

.popup-content img {
  max-width: 100%;

}

.popup-content p {
  text-align: center;
  margin-top: 10px;
}

</style>