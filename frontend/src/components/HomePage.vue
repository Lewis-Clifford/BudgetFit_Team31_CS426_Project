<!-- Author: Kaden Nesch -->
<!-- This template will display the home page that users will see when first entering the website -->
<!-- It will contain a button to continue and a navigation bar on top that can take users to other pages, such as login -->

<template>
  <div v-if="showBanner" class="banner" :style="{ display: bannerDisplay }" @click="hideBanner">
    You're in {{ username }}. Let's get to work!
  </div>
  <img class="background" src="../assets/goat.jpeg">
  <img class="backgroundmin" src="../assets/green.jpg">
  <div class="textwrap">
    <h1>Save Money.</h1>
    <h1>Eat Clean.</h1>
    <h1>Get in Shape.</h1>
    <div class="button">
  <router-link :to="loggedIn ? '/diet' : '/login'">
    <button>{{ loggedIn ? 'Continue' : 'Get Started' }}</button>
  </router-link>
</div>
  </div>
</template>

<script>

// This script will send get requests to the backend to obtain form status initially when on the website as well as the user's already created lists
// Once users have logged in, this home page will display a banner telling the person they have logged in successfully with their name
// Contains code to obtain the user's profile picture opon arrival on webpage

import axios from 'axios';
import store from '../store';
export default {
  name: "HomePage",
  data() {
    return {
      bannerDisplay: "block",
      profileImage: null,
      listNames: []
    };
  },
  computed: {
    showBanner() {
      return this.$store.state.firstLogin && this.$store.state.isLoggedIn && !this.$store.state.bannerShown; 
    },
    username() {
      return this.$store.state.username;
    },
    loggedIn() {
      return this.$store.state.isLoggedIn;
    },
  },
  methods: {
    hideBanner() {
  const banner = document.querySelector('.banner');
  banner.classList.add('fadeOut');
  setTimeout(() => {
    this.bannerDisplay = "none";
    this.$store.commit("setBannerShown", true);
    banner.classList.remove('fadeOut');
  }, 1000);
},
async getUserProfile(userID) {
  axios.get(`http://localhost:5000/profile?userID=${userID}`)
    .then(response => {
      const data = response.data[0];
      this.profileImage = data.profileImage;

      store.dispatch('updateProfileImage', data.profileImage);

    })
    .catch(error => {
      console.log(error);
    });
},
async updateFormStatus(userID) {
  axios.post(`http://localhost:5000/updateStatus?userID=${userID}`)
    .then(response => {

    })
    .catch(error => {
      console.log(error);
    });
},
async names(userID) {
        axios.get(`http://localhost:5000/newList?userID=${userID}`)
                .then(response => {
                  const data = response.data;
                  this.listNames = data.map(list => list.listName);
                  this.listPriorities = data.map(list => list.priority)
                  this.listDescriptions = data.map(list => list.description)
                  localStorage.removeItem("activeList");
                  localStorage.setItem('activeList', this.listNames[0]);
                  localStorage.setItem('activePriority', this.listPriorities[0]);
                  localStorage.setItem('activeDescription', this.listDescriptions[0]);
                })
                .catch(error => {
                console.log(error);
                });
            },
  },
  mounted() {
    setTimeout(() => {
      this.hideBanner();
    }, 8000);
  },
  created() {
    this.getUserProfile(localStorage.getItem('userID'));
    this.updateFormStatus(localStorage.getItem('userID'))
    this.names(localStorage.getItem('userID'))
  }

};
</script>

<style scoped>

.fadeOut {
  animation-name: fadeOut;
  animation-duration: 1s;
  animation-timing-function: ease-out;
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
.background{
   position: fixed;
    top: 0;
    bottom:0;
    left:0;
    max-width: 100%;
    height: 100%;
    z-index: -1;
}

.backgroundmin{
  display: none;
  position: fixed ;
    top: 0;
    bottom:0;
    left:0;
    max-width: 100%;
    height: 100%;
    z-index: -1;
}

@media screen and (max-width: 1280px){
  .background{
    display: none;
  }
  .backgroundmin{
    display: block;
  }
}

.textwrap{
  display: flex ;
  flex-direction: column ;
  align-items: center ;
  object-fit: contain ;
  color: white; 
  font-size: 30px;
  z-index: 1;
  margin: 100px;
}

.textwrap h1{
  font-size: 60px;
  margin: 50px;
}

button{
  border-radius: 25px;
  background: white;
  white-space: nowrap;
  padding: 20px 80px;
  color: #474b4f;
  font-size: 40px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  text-decoration: none;
}

button:hover {
  transition: all 0.5 ease-in-out;
  background: #474b4f;
  color: #fff;
}

.button{
  padding-top: 50px;
}

.banner {
  position: absolute;
  top: 100px;
  left: 0;
  width: 100%;
  padding: 10px;
  background-color: #2ecc71;
  color: #fff;
  font-size: 22px;
  font-weight: bold;
  text-align: center;
  cursor: pointer;
  transition: opacity 0.3s ease-in-out; 
}

.banner.hidden {
  opacity: 0; /* set opacity to 0 when hidden */
}

</style>

