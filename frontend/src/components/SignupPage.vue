<script setup>

const handleIconClick = (node, e) => {
  node.props.suffixIcon = node.props.suffixIcon === 'eye' ? 'eyeClosed' : 'eye'
  node.props.type = node.props.type === 'password' ? 'text' : 'password'
}


</script>

<template>
<img class="backgroundmin" src="../assets/green.jpg">
    <div class="styledformR">
        <div class="img"></div>
        <h2 class="Title">Register</h2>
        <FormKit type="form" submit-label="Register" :submit-attrs="{wrapperClass: 'buttonWrap', inputClass:'RegButtonP'}" @submit="createAccount()">
        <p class="enterDetails">Enter your details below to register a new account </p>
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
    import axios from 'axios'
    import sha256 from 'crypto-js/sha256';
    
    export default {
    
      name: 'SignupPage',
      data (){
        return{

            username: '',
            email: '',
            password: '',
          

        }
      },
      methods: {
        async createAccount(){
          const hashedPassword = sha256(this.password).toString();
          axios.post('http://127.0.0.1:5000/register', {
          username: this.username,
          email: this.email,
          password: hashedPassword,
         })
          .then(response => console.log(response))
          .catch(error => console.log(error))
          await new Promise((r) => setTimeout(r, 1500))
    

        }, 

      }}
    </script>
    
    
    
    
    <style >

    .styledformR{
    background-color: #fff;
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