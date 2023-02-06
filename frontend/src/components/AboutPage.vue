<template>
<div class="Wrapper">
<div class="green">

<div class="TextWrapper">
<h1>About us</h1>
<div class="image"></div>
<p class="paragraph">We are Team 31 in Senior Software Engineering at University of Nevada, Reno.
        Our group members are Kaden Nesch, Alexander Ram, and Clifford Lewis. Our Team 31’s project consists of an application oriented toward diet, fitness, and budgeting. The aim of the application is to help the user track grocery prices, user budgets, calories consumed, and calories burned, micro/macro-nutrients needed, dietary restrictions, proximity to stores, and user progress toward set goals. 
        <br/><br/>Users should be able to create a list of items they want to purchase and receive a variety of information based on the list. This list will include preferred shopping location, similar item suggestions, tracking for a variety of diets, estimated food viability time, prices, and historical data on user progress, trends, and choices. The primary areas of focus on the usage of the features are simple GUI, ease of use, and reliability. The intention is to provide a user experience that is neither overbearing nor lacking.
        <br/><br/> A simple GUI ensures that using the application requires no extensive effort. Ease of use allows users to reduce the amount of time they spend trying to navigate the app and increase the amount of benefit they gain by using the app. The application must also provide a reliable experience so that the user is not affected by any issues that hamper the user experience. Major architecture components are the interface, which must be optimized for functionality and appearance; APIs for integrated features, which reduces the need for hard-coded features; and a robust database, to maintain and track user data most efficiently. 
        <br/><br/>The project is intended to decrease user food spending and improve user dietary practices to address growing societal, financial and health concerns. Potential technologies for the project include React Native, Google Calendar API, MyFitnessPal API, and Micro Users Service API. Challenges are expected in learning database creation, use, and management, learning user interface development, and using APIs.
        <br/><br/><br/>
        <br/></p>
</div>
</div>
</div>


</template>

<script>

export default{

    name: 'AboutPage',
}
</script>


<style scoped>

.green{
height: 30vh;
background-image: url('../assets/green.jpg');
background-size: cover;
background-position: center;
background-repeat: no-repeat;
}

.image{
width: 90vw;
height: 40vh;
background-image: url('../assets/5912.jpg');
background-size: contain;
background-position: center;
background-repeat: no-repeat;
z-index: 2;
margin-bottom: -20px;
}

.paragraph{
font-size: 20px;
color: black;
width: 70%;
text-align: left;
line-height: 40px;
}

.Wrapper{
    display: flex;

}

.TextWrapper{
display: flex;
flex-direction: column;
align-items: center;
object-fit: contain;
color: white;
font-size: 30px;
}


</style>

