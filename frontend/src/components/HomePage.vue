<template>
<img class="background" src="../assets/goat.jpeg">
<img class="backgroundmin" src="../assets/green.jpg">
<div class="textwrap">
    <h1>Save Money.</h1>
    <h1>Eat Clean.</h1>
    <h1>Get in Shape.</h1>
    <div class="button">
      <router-link to="/login">
        <button>Begin</button>
      </router-link>
    </div>
</div>
</template>

<script>
export default {
  name: 'HomePage',

}
</script>


<style scoped>
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
  position: fixed;
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
display: flex;
flex-direction: column;
align-items: center;
object-fit: contain;
color: white;
font-size: 30px;
z-index: 1;
margin: 100px;
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

</style>
