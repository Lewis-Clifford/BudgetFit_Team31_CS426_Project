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
