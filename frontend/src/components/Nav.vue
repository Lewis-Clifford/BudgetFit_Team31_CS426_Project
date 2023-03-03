<template>
  <nav class="navbar">
    <router-link class="iconlink" to="/"><img class="icon" src="../assets/BF.png"></router-link> 
    <div class="menu">
    <router-link active-class="underline" class="pages" to="/shop">Shop</router-link> 
    <router-link active-class="underline" class="pages" to="/diet">Diet</router-link> 
    <router-link active-class="underline" class="pages" to="exercise">Exercise</router-link> 
    <router-link active-class="underline" class="pages" to="/about">About</router-link> 
    <nav class="buttonnav">
    
    <router-link v-if="!buttonPressed" v-on:click="changeState" class="button" to="/login">Login
    </router-link>
    <img class="profile" :class="{'highlight': isMenuOpen }"   v-else src="../assets/icon.jpg" @click="toggleMenu">
    <div class="sub-menu-wrap" :class="{'open-menu': isMenuOpen}" id="subMenu">
        <div class="sub-menu" v-if="buttonPressed">
            <div class="user-info">
                <img src="../assets/icon.jpg">
                <h2>Username</h2>
            </div>
            <hr>
            <router-link to="/edit" class="sub-menu-link">
                <img src="../assets/profile.png">
                <p>Edit Profile</p>
                <span>></span>
            </router-link>
            <a href="#" class="sub-menu-link">
                <img src="../assets/setting.png">
                <p>Profile Settings</p>
                <span>></span>
            </a>
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


<script>


export default{
    name: 'Navbar',
    data() {
        return {
        buttonPressed: false,
        isMenuOpen: false,
        loggedIn: false,
    }
    },
    methods: {
        changeState: function(){
            this.buttonPressed = true;
        },
        toggleMenu(){
            this.isMenuOpen = !this.isMenuOpen
        },
        handleLogout(){
            this.buttonPressed = false;
        }
    }
}

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
    background: #474b4f;
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