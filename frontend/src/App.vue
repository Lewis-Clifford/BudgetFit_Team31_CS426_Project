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
  },
}
</script>


<style scoped>



</style>
