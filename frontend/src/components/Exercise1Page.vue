<template>
    <div class="styledform">
    <h1 class="titleE">Exercise and Weight Goal</h1>
    <h3 style="border-bottom: 2px solid #000; padding-bottom: 30px; color: #474b4f">Select one exercise and one weight goal below</h3>
    <FormKit type="select"  placeholder="Exercise Goal" 
    :options="['Powerlifting', 'Hypertrophy Training', 'Athlete Training', 'Cardio']"></FormKit>
    <FormKit type="select" placeholder="Weight Goal" :options="['Weight Loss', 'Weight Gain', 'Maintain Weight']"></FormKit>
    
    <div class="ButtonGroup">
            <button class="LogButton">Finish</button>
        </div>
    
    </div>
    
    
    </template>
    
    
    <script>
    export default{
        name: 'Exercise1Page',
    }
    
    </script>
     
    
    
    <style scoped>

  
    
    .titleE{
    
        font-size: 45px;
        color:#474b4f
    
    }
    
    .LogButton{
    padding: 10px;
    width: 430px;
    background-color: #4d4f47;
    font-size: 16px;
    border: 4px solid #474b4f;
    color: #fff;
    transition: ease-in-out 0.2s;
    }
    
    .LogButton:hover{
      background-color: #72b264;
      border: 4px solid #72b264;
      color: #fff;
      cursor: pointer;
    }
    
    .LogButton:active {
      background-color: #474b4f;
      border: 4px solid #474b4f;
      color: #474b4f
    }
    
    
    </style>