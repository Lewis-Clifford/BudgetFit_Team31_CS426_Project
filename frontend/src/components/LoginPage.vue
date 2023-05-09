<!-- Author: Kaden Nesch -->
<!-- This template will display the login page where users can enter their username and password to login -->
<!-- If users do not have an account, they can enter the button to go to the register page instead where they can create ana account, then come back to this one to login -->

<script setup>

const handleIconClick = (node, e) => {
  node.props.suffixIcon = node.props.suffixIcon === 'eye' ? 'eyeClosed' : 'eye'
  node.props.type = node.props.type === 'password' ? 'text' : 'password'
}
</script>


<template>

<div v-if="loggedIn" class="logged-in-box">
  <p>You are already logged in as <b>{{ $store.state.username }}</b>.</p>
  <button @click="handleLogout">Click here to logout</button>
</div>

<div v-else class="styledform">
    <div class="img"></div>
    <h2 class="Title">Login</h2>
    <FormKit type="form" submit-label="Login" :submit-attrs="{wrapperClass: 'buttonWrap', inputClass:'RegButtonP'}" @submit="accountLogin()">
      
    <p class="enterDetails">Enter your details below to sign into your account</p>
    <div v-if="error" class="error">{{ error }}</div>
    
    <FormKit prefix-icon="people" message-class="textlab" v-model="formData.username" type="text"  name="username" placeholder="Username"  
    validation="required|alphanumeric|length:4,14" />


    <FormKit prefix-icon="password" message-class="textlab" v-model="formData.password" suffix-icon="eyeClosed" @suffix-icon-click="handleIconClick" type="password" name="password" placeholder="Password" 
    validation="required|matches:/^[a-zA-Z0-9\$@]+$/|length:6,20" 
    :validation-messages="{matches: 'Password can only contain the special characters $ and @'}"/>



  </FormKit>

    <p class="DontHave">Don't have an account? Register Below</p>
    <div class="ButtonGroup">
      <router-link to="/register">
        <button class="RegButton">Register</button>
      </router-link>
    </div> 
    

  

</div>
</template>

<script>

// This script will send a post request to the backend once a user has filled out a correct username or password
// If that is not the case, they will be greeted with an error that either the username or password is incorrect
// Once users enter this page while logged in, a page will display that will display their name and the ability to logout
// Contains code to obtain the user's profile picture opon arrival on webpage

import store from '../store';
import axios from "axios";
export default {
  name: "LoginPage",
  data() {
    return {
      formData: {
        username: "",
        password: "",
      },
      error: null,
      profileImage: null,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.isLoggedIn;
    },
  },
  created(){
    this.getUserProfile(localStorage.getItem('userID'));
  },
  methods: {
    
    async accountLogin() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:5000/login",
          this.formData
        );
        console.log(response);
        await new Promise((r) => setTimeout(r, 1000));
        const userID = response.data.userID;
        localStorage.setItem('userID', userID);
        localStorage.setItem('access_token', response.data.access_token);
        this.$store.commit('setLoggedIn', true);
        this.$store.commit('setBannerShown', false)
        this.$store.commit('setUsername', this.formData.username);
        localStorage.setItem('username', this.formData.username);
        this.$router.push({ name: "home" });
        
      } catch (error) {
        console.log(error);
        if (error.response.status === 401) {
          this.error = "Username or password incorrect.";
        }
      }
    },
    emptyCart() {
      this.$store.commit('clearCart');
      this.cart = [];
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




<style>

.logged-in-box {
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  width: 330px;
  margin: 60px auto;
  text-align: center;
  border-radius: 10px;
  overflow: auto;
}

.logged-in-box p {
  font-size: 1.2rem;
  color: #333333;
  margin-bottom: 20px;
}

.logged-in-box button {
  background-color: #72b264;
  border: none;
  border-radius: 5px;
  color: #ffffff;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  padding: 10px 20px;
}

.logged-in-box button:hover {
  background-color: #474b4f;
}

.error {
  color: red;
  position: absolute;
  right: 0;
  font-size: 15px;
  left: 0;
  top: 246px;
}


.textlab{
  position: relative !important;
  right: -35px !important;
  box-sizing: initial !important;;

}

.textlabcon{
  position: relative !important;
  right: -150px !important;
  box-sizing: initial !important;

}

.Forgot{
font-size: 15px;
text-align: right;
color: #474b4f;
margin: -10px 40px -20px;
cursor: pointer;
box-sizing: initial !important;
}

[data-type=password] .formkit-inner{
width: 430px;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
box-sizing: initial !important;
}

[data-type=text] .formkit-inner{
width: 430px;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
box-sizing: initial !important;
}

[data-type="email"] .formkit-inner{
width: 430px;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
box-sizing: initial !important;
}

[data-type="text"] .formkit-input{
  line-height: 25px;
  box-sizing: initial !important;

}

[data-type="password"] .formkit-input{
  line-height: 25px;
  box-sizing: initial !important;

}

[data-type="email"] .formkit-input{
  line-height: 25px;
  box-sizing: initial !important;

}


[data-invalid] .formkit-inner {
  border-color: red;
  box-shadow: 0 0 0 2px red;
  box-sizing: initial !important;
}

[data-complete] .formkit-inner {
  border-color: #72b264;
  box-shadow: 0 0 0 2px #72b264;
  box-sizing: initial !important;
}

.RegButton{
padding: 8px;
width: 393px;
border-radius: var(--fk-border-radius);
background-color: #72b264 ;
font-size: 16px;
border: 4px solid #72b264 ;
color: #fff;
transition: ease-in-out 0.2s;
text-decoration: none;
box-sizing: border-box !important;
}

.RegButton:hover{
  background-color: #474b4f;
  border: 4px solid #474b4f;
  color: #fff;
  cursor: pointer;
  box-sizing: border-box !important;
}

.RegButton:active {
  background-color: #72b264;
  border: 4px solid #72b264;
  color: #474b4f;
  
}

.LogButton{
  padding: 9px;
width: 395px;
border-radius: var(--fk-border-radius);
background-color: #72b264 ;
font-size: 16px;
border: 4px solid #72b264 ;
color: #fff;
transition: ease-in-out 0.2s;
text-decoration: none;
box-sizing: border-box !important;
}

.LogButton:hover{
  background-color: #474b4f;
  border: 4px solid #474b4f;
  color: #fff;
  cursor: pointer;
}

.LogButton:active {
  background-color: #72b264;
  border: 4px solid #72b264;
  color: #474b4f
}

.ButtonGroup{
display: flex;
justify-content: space-around;
flex-direction: row;
margin-top: 40px;
margin-bottom: 25px;
box-sizing: initial !important;
}

.DontHave{
font-size: 20px;
text-align: center;
color: #474b4f;
margin: -10px 80px -20px;
box-sizing: initial !important;
}

.styledform{
background: #f3f3f3;
text-align: center;
padding: 45px 55px;
width: 500px;
height: auto;
margin-left: auto;
margin-right: auto;
margin-top: 60px;
display: block;
border-radius: 10px;
overflow: auto;
box-sizing: initial !important;
}

.img{
width: 80px;
height: 80px;
background-image: url('../assets/BF.png');
background-size: cover;
background-position: center;
margin: left;
border-radius: 10px;

}

.Title{
font-size: 45px;
text-align: center;
color: #72b264;
margin-top: -25px;
}

.enterDetails{
font-size: 20px;
text-align: center;
color: #474b4f;
margin: 15px 120px 20px;
}

.ForgotPass{
display: flex;
justify-content: space-around;
flex-direction: row;
margin-top: 40px;
margin-bottom: 25px;
}




</style>

