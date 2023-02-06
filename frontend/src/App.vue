<template>
  <nav class="navbar">
    <router-link class="iconlink" to="/"><img class="icon" src="./assets/BF.png"></router-link> 
    <div class="menu">
    <router-link class="pages" to="/shop">Shop</router-link> 
    <router-link class="pages" to="/diet">Diet</router-link> 
    <router-link class="pages" to="exercise">Exercise</router-link> 
    <router-link class="pages" to="/about">About</router-link> 
    <nav class="buttonnav">
    <router-link class="button" to="/login">Login
    </router-link>
    </nav>
  </div>
    
  </nav>
  <router-view/>

</template>

<style scoped>

.navbar{
  background: #474b4f	;
  height: 100px;
  display: flex;
  justify-content: space-between;
  padding: 0.5rem calc((50vw - 850px) / 2);
  z-index: 10;
  font-family: Georgia;
}

@media screen and (max-width: 820px) {
  .navbar{

    transition: 0.8s all ease;

  }

  .pages{
    display: none;
  }
  }


.icon{
width: 80px;
height: 80px;
background-size: cover;
background-position: center;
margin: left;
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
padding: 0 1rem;
height: 100%;
cursor: pointer;
font-size: 28px;
margin-right: 24px;
}

.pages:hover {
  border-bottom: 3px solid #778899;
  border-bottom-right-radius: 15px;
  border-bottom-left-radius: 15px;
}

.pages:active {
  color: green;
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
