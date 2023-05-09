
<!-- Author: Kaden Nesch -->
<!-- This template will display the add button that allows users to add products to their cart -->

<template>
  <button class="btn btn-primary btn-circle position-absolute top-100 start-50 translate-middle"
          :class="{ active : isActive }"
          :key="itemCount"
          @click="toggle"
          type="button">
    <font-awesome-icon :icon="isActive ? 'fa-solid fa-check' : 'fa-solid fa-plus'" />
  </button>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

// The script will add products to the cart if they are not already added, and based on the state of the button, remove the item from the cart if pressed again.
export default {
  name: 'ButtonComponent',
  props: ['item'],
  computed: {
    ...mapState(['cart']),
    itemCount() {
      const item = this.cart.find(i => i.item_name === this.item.item_name);
      return item ? item.quantity : 0;
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
        this.removeFromCart(this.item);
      } else {
        this.addToCart(this.item);
      }
    }
  }
}
</script>

  <style>
.btn.btn-primary.btn-circle{
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: rgb(0, 89, 255);
    border: none;

}

.btn.btn-primary.btn-circle.active {
  background-color: rgb(206, 217, 82);
}

</style>