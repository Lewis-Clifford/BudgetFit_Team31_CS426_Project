<template>
    <button class="btn btn-primary btn-circle position-absolute top-100 start-50 translate-middle"
            :class="{ active : isActive }"
            @click="toggle"
            type="button">
      <font-awesome-icon :icon="isActive ? 'fa-solid fa-check' : 'fa-solid fa-plus'" />
    </button>
  </template>
  
  <script>
  export default {
    name: 'ButtonComponent',
    props: ['item', 'cartItems'],
    data() {
      return {
        isActive: false
      }
    },
    methods: {
      toggle() {
  this.isActive = !this.isActive;
  if (this.isActive) {
    this.cartItems.push(this.item);
  } else {
    const index = this.cartItems.indexOf(this.item);
    this.cartItems.splice(index, 1);
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