<!-- Author: Kaden Nesch -->
<!-- This template will display the nav menu that users will see on the top of every webpage in the website -->
<!-- The nav menu will contain options of going to the home, diet, exercise, shop, login/dropdown pages  -->
<!-- Once a user is logged in, the login button will be replaced with the user's profile picture that will allow a dropdown menu -->
<!-- The dropdown menu will allow users to go to the editprofile page or they can logout -->


<template>
    <nav class="navbar">
      <router-link class="iconlink" to="/">
        <img class="icon" src="../assets/BF.png">
      </router-link>
      <div class="menu">
        <router-link active-class="underline" class="pages" to="/shop">Shop</router-link>
        <router-link active-class="underline" class="pages" to="/diet">Diet</router-link>
        <router-link active-class="underline" class="pages" to="exercise">Exercise</router-link>
        <router-link active-class="underline" class="pages" to="/about">About</router-link>
        <nav class="buttonnav">
          <router-link v-if="!isLoggedIn"  class="button" to="/login">Login</router-link>
          <img class="profile" :class="{'highlight': isMenuOpen }" v-else :src="profileImage || defaultprofileImage" @click="toggleMenu">
          <div class="sub-menu-wrap" :class="{'open-menu': isMenuOpen}" id="subMenu">
            <div class="sub-menu" v-if="isLoggedIn">
              <div class="user-info">
                <img class="profiled" :src="profileImage || defaultprofileImage">
                <h2>{{ username }}</h2>
              </div>
              <hr>
              <router-link to="/edit" class="sub-menu-link" @click="toggleMenu">
                <img src="../assets/profile.png">
                <p>Edit Profile</p>
                <span>></span>
              </router-link>
              <a class="sub-menu-link" @click="handleLogout">
                <img src="../assets/logout.png">
                <p>Logout</p>
                <span>></span>
              </a>
            </div>
          </div>
        </nav>
      </div>
    </nav>
    <router-view/>
  </template>

  // This script will send post requests to the backend when a user presses logout, destroying their session token and logging them out of their accounts
  // Contains code to obtain the user's profile picture opon arrival on webpage


  <script>
  import profileImage from '../assets/icon.jpg';
  import axios from 'axios';
  import { mapState } from 'vuex';
  export default {
    name: "Navbar",
    data() {
      return {
        isMenuOpen: false,
        defaultprofileImage: profileImage,
        
      };
    },
    computed: {
      ...mapState(['profileImage']),
      isLoggedIn() {
        return this.$store.state.isLoggedIn;
      },
      username() {
        return this.$store.state.username;
      },
    },
    methods: {
      toggleMenu() {
        this.isMenuOpen = !this.isMenuOpen;
      },
      
      emptyCart() {
      this.$store.commit('clearCart');
      this.cart = [];
    },

      async handleLogout() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:5000/logout",
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
        );
        console.log(response);
        localStorage.removeItem("access_token");
        localStorage.removeItem("phone");
        localStorage.removeItem('userID');
        localStorage.removeItem('activeList')
        localStorage.removeItem('name')
        this.emptyCart();
        this.$store.commit("setLoggedIn", false);
        this.$router.push({ name: "login" });
        this.isMenuOpen = !this.isMenuOpen;
      } catch (error) {
        console.log(error);
      }
    },

    },
  };
  </script>

<style scoped>

.highlight{
border: 8px solid #72b264;


}

.underline{
    border-bottom: 3px solid #778899;

}

.sub-menu-link{
    display: flex;
    align-items: center;
    text-decoration: none;
    color: #474b4f;
    margin: 12px 0;
    cursor: pointer !important;
}

.sub-menu-link p{
width: 100%;
color: white;
}

.sub-menu-link img{
    width: 40px;
    max-width: 40px;
    background: #e5e5e5;
    border-radius: 50%;
    padding: 8px;
    margin-right: 15px;


}
.sub-menu-link span{
    font-size: 22px;
    transition: transform 0.5s;
    color: white;
}

.sub-menu-link:hover span{
    transform: translateX(5px);
}

.sub-menu-link:hover p{

font-weight:600;
}

.sub-menu hr{
    border: 0;
    height: 1px;
    width: 100%;
    background: #ccc;
    margin: 15px 0 10px;
}

.user-info{
    display: flex;
    align-items: center;
}

.user-info h2{
    font-weight: 500;
    color: white;;
}

.user-info img{
    width: 60px;
    border-radius: 50%;
    margin-right: 15px;
}
.sub-menu{
    background: #474b4f;
    padding: 20px;
    margin: 10px;
    position: relative;
    z-index: 5;

}
.sub-menu-wrap{
    position: absolute;
    top: 100%;
    right: 2%;
    width: 320px;
    max-height: 0px;
    overflow: hidden;
    transition: max-height 0.5s;

}

.sub-menu-wrap.open-menu{
    max-height: 400px;
}

.navbar{
    background: #343836;
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
}

.icon{
width: 80px;
height: 80px;
background-size: cover;
background-position: center;
margin: left;
border-radius: 10px;
}

.profile{
width: 60px;
height: 60px;
background-size: cover;
background-position: center;
border-radius: 50%;
cursor: pointer;
box-sizing:border-box !important;
}

.profiled{
width: 60px;
height: 60px;
background-size: cover;
background-position: center;
border-radius: 50%;
}

.menu{
display: flex;
align-items: center;
}

.iconlink{
color: #000;
display: flex;
align-items: center;
text-decoration: none;
padding: 0 1rem;
height: 100%;
cursor: pointer;
font-size: 28px;
margin-right: 24px;
}

.pages{
color: white;
display: flex;
align-items: center;
text-decoration: none;
padding: 0 1.5rem;
height: 100%;
cursor: pointer;
font-size: 28px;
margin-right: 24px;
padding-bottom: 5px;
}

.pages:hover{
    border-bottom: 3px solid #778899;
}

.pages:active {
  color: #72b264;
}


.buttonnav{
display: flex;
align-items: center;
margin-right: 24px;
}

.button{
border-radius: 50px;
background: #72b264;
white-space: nowrap;
padding: 16px 40px;
color: white;
font-size: 28px;
cursor: pointer;
transition: all 0.2s ease-in-out;
text-decoration: none;
}

.button:hover {
  transition: all 0.5 ease-in-out;
  background: white;
  color: #474b4f;
}
</style>