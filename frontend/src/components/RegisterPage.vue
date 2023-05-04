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

    <div v-else class="styledformR">
        <div class="img"></div>
        <h2 class="Title">Register</h2>
        <FormKit type="form" submit-label="Register" :submit-attrs="{wrapperClass: 'buttonWrap', inputClass:'RegButtonP'}" @submit="createAccount()">
        <p class="enterDetails">Enter your details below to register a new account </p>
        <p class="error-message">{{ errorMessage }}</p>
        <FormKit  prefix-icon="people" message-class="textlab" type="text" v-model="username" name="username" placeholder="Username"  
        validation="required|alphanumeric|length:6,18"/>
        

        <FormKit  prefix-icon="email" message-class="textlab" v-model="email" type="email" placeholder="Email" name="email" validation="required|email" 
        />

        <FormKit  type="group">

        <FormKit prefix-icon="password" message-class="textlab" suffix-icon="eyeClosed" @suffix-icon-click="handleIconClick" type="password" name="password" v-model="password" placeholder="Password" 
        validation="required|matches:/^[a-zA-Z0-9\$@]+$/|length:6,20" 
        :validation-messages="{matches: 'Password can only contain the special characters $ and @'}" />
        <p class="Forgot">Forgot Password?</p>
        <FormKit prefix-icon="password" message-class="textlab" suffix-icon="eyeClosed" @suffix-icon-click="handleIconClick" type="password" name="password_confirm" placeholder="Confirm Password"
        validation="required|confirm|" validation-label="Confirmation"/>

        
        </FormKit>

      </FormKit>
        
       <!-- Comment --> 
      
        <p class="DontHave">Already registered? Login below</p>
        <div class="ButtonGroup">
          <router-link to="/login">
            <button class="LogButton">Login</button>
          </router-link>
        </div> 
        
    
      
    
    </div>
    </template>
    
    <script>
    import store from '../store';
    import axios from 'axios'
    import sha256 from 'crypto-js/sha256';
    
    export default {
    
      name: 'RegisterPage',
      data (){
        return{

            username: '',
            email: '',
            password: '',
            errorMessage: null,
            profileImage: null,
          

        }
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
        async createAccount() {
  const hashedPassword = sha256(this.password).toString();

  try {
    const response = await axios.post('http://127.0.0.1:5000/register', {
      username: this.username,
      email: this.email,
      password: hashedPassword,
    });
    console.log(response);
    await new Promise((resolve) => setTimeout(resolve, 1500));
    this.$router.push({ name: "login" }); // redirect to login page after successful registration
  } catch (error) {
    console.log(error.response.data.error); // display error message in console
    this.errorMessage = error.response.data.error; // set error message to be displayed in frontend
  }
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
        this.$store.commit("setLoggedIn", false);
        this.$router.push({ name: "login" });
        this.isMenuOpen = !this.isMenuOpen;
      } catch (error) {
        console.log(error);
      }
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

      }}
    </script>
    
    
    
    
    <style >

    .error-message {
        color: red;
        font-size: 15px;
        position: absolute;
        bottom: 45px;
        left: 0;
        right: 0;
      }

    .styledformR{
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


    .buttonWrap{
    display: flex;
    
justify-content: space-around;
flex-direction: row;
margin-top: 40px;
margin-bottom: 25px;
margin-left: 52px;

    }

    .RegButtonP{
padding: 10px !important;
margin-top: 20px !important;
width: 430px !important;
background-color: #72b264 !important;
font-size: 16px !important;
border: 4px solid #72b264 !important;
color: #fff !important;
transition: ease-in-out 0.2s !important;
text-decoration: none !important;
;
}

.RegButtonP:hover{
  background-color: #474b4f !important;
  border: 4px solid #474b4f !important;
  color: #fff !important;
  cursor: pointer !important;
}

.RegButtonP:active {
  background-color: #72b264 !important;
  border: 4px solid #72b264 !important;
  color: #474b4f !important;

}
    
    </style>