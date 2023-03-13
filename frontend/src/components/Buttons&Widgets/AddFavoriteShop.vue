<template>
  <div class="position-absolute top-0 end-0 mt-3 me-3">
    <button class="btn fav-button"
    :class="{'text-warning' : isActive, 'text-dark' : !isActive}"
    @click="toggle()">
    <font-awesome-icon :icon="isActive ? ' fa-star' : 'fa-regular fa-star'"></font-awesome-icon>

    </button>
  </div>
  </template>
  
  <script>
  export default {
    name: 'FavoriteComponent',
    data() {
      return {
        isActive: false
      }
    },
    methods: {
      toggle() {
        this.isActive = !this.isActive
      }
    }
  }
  </script>

  <style>
.btn.fav-button {
    border-radius: 50%;
    width: 32px;
    height: 32px;
    font-size: 1.7rem;
    line-height: 1.5;
    padding: 0; /* Remove default button padding */
    background-color: transparent; /* Remove default button background */
    border: none; /* Remove default button border */
  }







</style>