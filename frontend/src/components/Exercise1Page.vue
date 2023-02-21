<template>
    <img class="backgroundmin" src="../assets/green.jpg">
<div class="cont">
<div class="container" style="max-width: 540px">
        <header>Let us know your goals!</header>

        <FormKit type="form" :actions="false" style="min-height: 550px;" @submit="createExerciseData()" >
            <div class="form first">
                <div class="details personal">
                    <span class="title">This form is required to move forward towards your specialized workout plans.
                        
                    </span>
                   <br>
                    <span class="secondtitleReq">
                    Exercise Goals 
                    </span>
                    
                    
                    <div class="fieldsReq">
                        <div class="input-fieldReq">
                          <FormKit validation="required"  v-model="formData.exercisepreference" inner-class="select" 
                            type="select" label="Exercise Preference:" validation-label="Exercise Preference" placeholder="Enter Preference" 
                            :options="['Free Weight (Barbell/Dumbbell)', 'Body Weight (Calisthenics)', 'Combination Of Both', ]" ></FormKit>
                        </div>

                        <div class="input-fieldReq">
                            <FormKit validation="required"  v-model="formData.exercisetype" inner-class="select" 
                            type="select" label="Exercise Type:" validation-label="Exercise Type" placeholder="Enter Type" 
                            :options="['Powerlifting', 'Bodybuilding','Powerbuilding', 'Athlete', 'Cardio']" ></FormKit>
                        </div>

                      </div>
                      <span class="secondtitleReq">
                    Weight Goals 
                    </span>
                      <div class="fieldsReq">
                        <div class="input-fieldReq">
                          <FormKit validation="required"  v-model="formData.weightgoal" inner-class="select" 
                            type="select" label="Weight Goal:" validation-label="Weight Goal" placeholder="Enter Goal" 
                            :options="['Gain Weight', 'Lose Weight','Maintain Weight', 'Unsure']" ></FormKit>
                        </div>

                        <div class="input-fieldReq">
                            <FormKit validation="required"  v-model="formData.weightplan" inner-class="select" 
                            type="select" label="Weight Plan: (If Lose or Gain)" validation-label="Weight Type" placeholder="Enter Plan" 
                            :options="['Fast Weight Change (1 month)', 'Medium Weight Change (3 months)', 
                            'Slow Weight Change (6 months)', 'Very Slow Weight Change (1 year)', 'I Selected Maintain']" ></FormKit>
                        </div>

                      </div>

                        
                    
                    
                    
                </div>

                
                <div class="ButtonGroup" >
                    
                    <button type="submit" class="nextBtn">
                    <span class="btnText">Finish</span>
                    </button>
                </div> 
            </div>
        </FormKit>
        
        
    
    </div>
</div>
    
    </template>
    
    
    <script>
import axios from 'axios'


export default{
    name: 'Exercise1Page',
    data (){
        return{

          formData: {
            exercisepreference: '',
            exercisetype: '',
            weightgoal: '',
            weightplan: '',
          
          }

        }
      },
      methods: {
        async createExerciseData(){
         axios.post('http://127.0.0.1:5000/exerciseOPT', this.formData)
          .then(response => console.log(response))
          .catch(error => console.log(error))
          await new Promise((r) => setTimeout(r, 1500))

        }, 


      }
}
    
    </script>
     
    
    
    <style >

.container form .secondtitleReq{
    display: block;
    margin-bottom: 15px !important;
    font-size: 18px;
    font-weight: 500;
    margin-top: 10px !important;
    margin: 0;
    color: black;
    border-bottom: 3px solid #474b4f;
    padding-bottom: 4px;
}

.container form .fieldsReq{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;

   
}

form .fieldsReq .input-fieldReq{
    display: flex;
    width: calc(100% / 2 - 70px);
    flex-direction: column;
    margin: -5px 0;
    margin-bottom: 15px;
}

    
   
    
    </style>