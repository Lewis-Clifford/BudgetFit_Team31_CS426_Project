<template>

<div class="styledform">
<h1 class="titleE">Select Diet Plan</h1>
<h3 style="border-bottom: 2px solid #000; padding-bottom: 30px; color: #474b4f">Select a diet if applicable, otherwise skip to next page</h3>
<FormKit type="select"  placeholder="Diet Plan" 
:options="['Keto Diet (Low-no carbohydrates)', 'Vegetarian Diet (No meat)', 
'Vegan Diet (No meat or dairy)', 'Carnivore Diet (Strictly animal based)', 'Pescatarian (Vegetarian but can consume fish)'
, 'Paleo Diet (No processed foods)']"></FormKit>


<div class="ButtonGroup">
        <button class="Skipbutton">Skip</button>
        <button class="LogButton">Finish</button>
    </div>

</div>
</template>

<script>

export default{
    name: 'DietPage'
}
</script>

<style scoped>
.titleE{

font-size: 45px;
color:#474b4f

}

.Skipbutton{
padding: 10px;
width: 150px;
background-color: #4d4f47;
font-size: 16px;
border: 4px solid #474b4f;
color: #fff;
transition: ease-in-out 0.2s;
margin-right: 15px;
}

.Skipbutton:hover{
background-color: #72b264;
border: 4px solid #72b264;
color: #fff;
cursor: pointer;
}

.Skipbutton:active {
background-color: #474b4f;
border: 4px solid #474b4f;
color: #474b4f
}




</style>