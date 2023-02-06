<template>
    <nav>
      <router-link to="/"></router-link> |
      <router-link to="/shop">Shop</router-link> |
      <router-link to="/diet">Diet</router-link> |
      <router-link to="exercise">Exercise</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/login">
      <button>Login</button>
      </router-link>
      
    </nav>
    <router-view/>
  </template>


<script>
export default {
  name: 'Nav',

}
</script>