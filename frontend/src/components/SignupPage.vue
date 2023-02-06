<script setup>
const handleIconClick = (node, e) => {
  node.props.suffixIcon = node.props.suffixIcon === 'eye' ? 'eyeClosed' : 'eye'
  node.props.type = node.props.type === 'password' ? 'text' : 'password'
}
</script>

<template>

    <div class="styledform">
        <div class="img"></div>
        <h2 class="Title">Register</h2>
        <p class="enterDetails">Enter your details below to register a new account </p>
        <FormKit prefix-icon="people" type="text"  name="username" placeholder="Username"  
        validation="required|alphanumeric|length:6,18"/>

        <FormKit prefix-icon="email" type="email" placeholder="Email" name="Email" validation="required|email" 
        />

        <FormKit type="group">

        <FormKit prefix-icon="password" suffix-icon="eyeClosed" @suffix-icon-click="handleIconClick" type="password" name="password" placeholder="Password" 
        validation="required|matches:/^[a-zA-Z0-9\$@]+$/|length:6,20" 
        :validation-messages="{matches: 'Password can only contain the special characters $ and @'}" />

        <FormKit prefix-icon="password" suffix-icon="eyeClosed" @suffix-icon-click="handleIconClick" type="password" name="password_confirm" placeholder="Confirm Password"
        validation="required|confirm|" validation-label="Password confirmation"/>

        </FormKit>

        <p class="Forgot">Forgot Password?</p>
        <div class="ButtonGroup">
            <button class="LogButton">Register</button>
        </div>
        <p class="DontHave">Already registered? Login below</p>
        <div class="ButtonGroup">
          <router-link to="/login">
            <button class="RegButton">Login</button>
          </router-link>
        </div> 
        
    
      
    
    </div>
    </template>
    
    <script>
    
    export default {
    
      name: 'SignupPage',
    
    }
    </script>
    
    
    
    
    <style scoped>

    .styledform{
    background-color: #fff;
    text-align: center;
    padding: 45px 55px;
    width: 500px;
    height: auto;
    margin-left: auto;
    margin-right: auto;
    margin-top: 60px;
    display: block;
    border: solid;
    border-color: #72b264;
    border-width: 100px;
    border-image-slice: 1;
    border-image-source: linear-gradient(#72b264 , #474b4f);
    overflow: auto;
    }
    
    </style>