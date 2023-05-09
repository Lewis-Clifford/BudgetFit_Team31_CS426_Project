<!-- Author: Kaden Nesch -->
<!-- This is the data that will be present on every webpage throughout the website, so the navbar is placed here -->
<!-- Intializers for the vueX and local storage are enabled here to be present on every page -->

<template>
 <Navbar></Navbar>
</template>

<script>
import Navbar from './components/Nav.vue'

export default{
  components: {
    Navbar
  },
  created() {
    this.$store.commit('initializeCartFromStorage');

    if (localStorage.getItem("access_token")) {
    this.$store.commit("setLoggedIn", true);

  }
  if (localStorage.getItem("username")) {
    this.$store.commit("setUsername", localStorage.getItem("username"));
  }
  this.$store.commit('hideBanner');
  },
}
</script>


<style scoped>



</style>
