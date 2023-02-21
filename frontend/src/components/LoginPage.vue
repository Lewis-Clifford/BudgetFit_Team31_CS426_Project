<script setup>

const handleIconClick = (node, e) => {
  node.props.suffixIcon = node.props.suffixIcon === 'eye' ? 'eyeClosed' : 'eye'
  node.props.type = node.props.type === 'password' ? 'text' : 'password'
}
</script>


<template>

<div class="styledform">
    <div class="img"></div>
    <h2 class="Title">Login</h2>
    <FormKit type="form" submit-label="Login" :submit-attrs="{wrapperClass: 'buttonWrap', inputClass:'RegButtonP'}" @submit="accountLogin()">
    <p class="enterDetails">Enter your details below to sign into your account</p>

    <FormKit prefix-icon="people" message-class="textlab" v-model="formData.username" type="text"  name="username" placeholder="Username"  
    validation="required|alphanumeric|length:4,14" />

    <p class="Forgot">Forgot Password?</p>
    <FormKit prefix-icon="password" message-class="textlab" v-model="formData.password" suffix-icon="eyeClosed" @suffix-icon-click="handleIconClick" type="password" name="password" placeholder="Password" 
    validation="required|matches:/^[a-zA-Z0-9\$@]+$/|length:6,20" 
    :validation-messages="{matches: 'Password can only contain the special characters $ and @'}"/>

  

  </FormKit>

    <p class="DontHave">Don't have an account? Register Below</p>
    <div class="ButtonGroup">
      <router-link to="/signup">
        <button class="RegButton">Register</button>
      </router-link>
    </div> 
    

  

</div>
</template>

<script>
import axios from 'axios'
export default {
  
  name: 'LoginPage',
  data (){
        return{

          formData: {
            username: '',
            password: '',

          }

        }
      },
      methods: {
        async accountLogin(){
         axios.post('http://127.0.0.1:5000/login', this.formData)
          .then(response => console.log(response))
          .catch(error => console.log(error))
          await new Promise((r) => setTimeout(r, 1000))

        }, 

      }

}
</script>




<style>

.textlab{
  position: relative !important;
  right: -185px !important;

}

.textlabcon{
  position: relative !important;
  right: -150px !important;

}

.Forgot{
font-size: 15px;
text-align: right;
color: #474b4f;
margin: -10px 40px -20px;
cursor: pointer;
}

[data-type=password] .formkit-inner{
width: 430px;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
}

[data-type=text] .formkit-inner{
width: 430px;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
}

[data-type="email"] .formkit-inner{
width: 430px;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
}

[data-type="text"] .formkit-input{
  line-height: 25px;

}

[data-type="password"] .formkit-input{
  line-height: 25px;

}

[data-type="email"] .formkit-input{
  line-height: 25px;

}


[data-invalid] .formkit-inner {
  border-color: red;
  box-shadow: 0 0 0 2px red;
}

[data-complete] .formkit-inner {
  border-color: #72b264;
  box-shadow: 0 0 0 2px #72b264;
}

.RegButton{
padding: 10px;
width: 395px;
border-radius: var(--fk-border-radius);
background-color: #72b264 ;
font-size: 16px;
border: 4px solid #72b264 ;
color: #fff;
transition: ease-in-out 0.2s;
text-decoration: none;
}

.RegButton:hover{
  background-color: #474b4f;
  border: 4px solid #474b4f;
  color: #fff;
  cursor: pointer;
}

.RegButton:active {
  background-color: #72b264;
  border: 4px solid #72b264;
  color: #474b4f
}

.LogButton{
padding: 10px;
width: 395px;
border-radius: var(--fk-border-radius);
background-color: #72b264;
font-size: 16px;
border: 4px solid #72b264;
color: #fff;
transition: ease-in-out 0.2s;
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
}

.DontHave{
font-size: 20px;
text-align: center;
color: #474b4f;
margin: -10px 80px -20px;
}

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
}

.img{
width: 80px;
height: 80px;
background-image: url('../assets/BF.png');
background-size: cover;
background-position: center;
margin: left;
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
margin: -25px 145px 20px;
}

.ForgotPass{
display: flex;
justify-content: space-around;
flex-direction: row;
margin-top: 40px;
margin-bottom: 25px;
}




</style>