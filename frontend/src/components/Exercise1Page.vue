<template>
    <img class="backgroundmin" src="../assets/green.jpg">
<div class="cont">
<div class="container2">
        <header>Let us know your goals!</header>

        <FormKit  message-class="message" type="form" :actions="false" style="min-height: 550px;" @submit="createExerciseData()" >
            <div class="form first">
                
              <span class="title">This form is required to move forward towards your specialized workout plans.
   
                      </span>
                <div class="detailspersonal">
                    
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


.detailspersonal{
  top: 50px;
  position: relative;
}

.container2{
    position: relative;
    max-width: 870px;
    border-radius: 10px;
    padding: 25px;
    margin: auto;
    background-color: #fff;
    box-shadow: 0 5px 10px rgba(0,0,0,0.1);
    top: 50%;
    min-height: 690px;
    transform: translateY(10.4%);

}

.container2 form button, .backBtn{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 45px;
    max-width: 300px;
    width: 100%;
    border: none;
    outline: none;
    color: #fff;
    border-radius: 5px;
    margin: 25px 0;
    margin-top: 100px;
    transition: all 0.3s linear;
    cursor: pointer;
}

.container2 form .secondtitleReq{
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

.container2 form .fieldsReq{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    margin-left: 130px;

   
}

.container2 header{
    position: relative;
    font-size: 20px;
    font-weight: 600;
    color: #333;
}

.container2 header::before{
    content: "";
    position: absolute;
    left: 0;
    bottom: -5px;
    height: 3px;
    width: 65px;
    border-radius: 8px;
    background-color: #72b264;
}

.container2 form{
    position: relative;
    margin-top: 16px;
    min-height: 650px;
    background-color: #fff;
    overflow: hidden;
}

.container2 form .title{
    display: block;
    margin-bottom: 8px;
    font-size: 16px;
    font-weight: 500;
    margin: 0;
    color: #333;
}



form .fieldsReq .input-fieldReq{
    display: flex;
    width: calc(100% / 2 - 70px);
    flex-direction: column;
    margin: -5px 0;
    margin-bottom: 15px;
}

    
    </style>