<!-- Author: Kaden Nesch -->
<!-- This template will display the optional exercise form that users will have to fill out. They can skip this form if they feel like doing so -->
<!-- Here they can enter personal information such as height, weight, age, and exercise experience -->
<!-- This template will display another screen saying Form completed click to edit if the user has already completed the form, they can edit it once again -->

<template>
  <template v-if="exerciseOPTfilledout === 0">
<div class="containere" style="max-width: 540px">
        <header>In need of a personally tailored workout?</header>

        <FormKit message-class="message" type="form" :actions="false" @submit="onFormSubmit" >
            <div class="form first">
                <div class="details personal">
                    <span class="title">This is an optional form. Choosing to complete it will allow us
                        to provide you with most personal workout routine.
                        
                    </span>
                   <br>
                    <span class="secondtitle">
                    Personal Details 
                    </span>
                    
                    <div class="fields">
                        <div class="input-field">
                            <FormKit :floating-label="false" placeholder="Enter First Name"
                             inner-class="texIn" v-model="formData.firstname"
                             validation="required|alpha:latin|length:1,20" validation-label="First Name" :validation-messages="{alpha: 'Only latin alphabet letters allowed'}"
                              type="text" label="First Name:"></FormKit>
                        </div>

                        <div class="input-field">
                            <FormKit validation="required"  v-model="formData.gender" inner-class="select" 
                            type="select" label="Gender:" validation-label="Gender" placeholder="Enter Gender" 
                            :options="['Male', 'Female', 'Non-Binary', 'Prefer not to say']" ></FormKit>
                        </div>

                        <div class="input-field">
                            <FormKit type="tel" v-model="formData.phone" label="Telephone Number:" validation-label="Phone Number" placeholder="Enter Phone Number"
                            validation="required|number|length:10,10" :floating-label="false"></FormKit>
                        </div>

                        <div class="input-field">
                            <FormKit validation="required|date_before:2011-12-31 00:00:00" v-model="formData.birth"
                            :validation-messages="{date_before: 'Minimum age requirement is 12 or older'}" validation-label="Birthdate"  
                            inner-class="text" type="date"  label="Birthdate:"
                            :floating-label="false"></FormKit>
                        </div>

                        <div class="input-field">
                            <FormKit validation="required|min:50|max:1000" :validation-messages="{min: 'Minimum weight is 50 pounds',
                             max: 'Maximum weight is 1000 pounds'}"  inner-class="textW" v-model="formData.weight"
                            label-class="labelW" type="number" validation-label="Weight" label="Weight:" placeholder="Enter Weight (lbs)" 
                            :floating-label="false" oninput="this.value = !!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"></FormKit>
                        </div>

                        <div class="input-fieldMore">
                            <FormKit validation="required|min:0|max:8" inner-class="textWF" v-model="formData.heightFeet"
                            label-class="labelW" type="text" validation-label="Height"
                            :validation-messages="{min: 'Enter valid height', max: 'Enter valid height'}" label="Height" placeholder="Feet" 
                            :floating-label="false"></FormKit>

                            <FormKit validation="required|min:0|max:11" inner-class="textWI" v-model="formData.heightInch"
                            label-class="labelI" type="text" label=":" message-class="message" placeholder="Inches" 
                            :floating-label="false"></FormKit>
                            
                        </div>

                        
                    </div>
                </div>

                <div class="details ID">
                    <span class="secondtitle">Exercise Details</span>
                    <br>
                    <div class="fields">
                        <div class="input-fieldTwo">
                            <div class="range-slider-containere">
                              <div class="range-slider-value">{{ formData.experience }}</div>
                              <div class="range-slider">
                                <FormKit type="range"  label="What is your workout experience? (1-10)" :floating-label="false"
                         v-model="formData.experience" min="0" max="10" step="1" validation="required" :validation-messages="{required: 'Experience is required.'}" />
                              </div>
                            </div>

                            <div class="range-slider-container2">
                        <div class="range-slider-value">{{ formData.level }}</div>
                        <div class="range-slider">
                        <FormKit type="range"  label="What is your current fitness level? (1-10)"  :floating-label="false"
                         v-model="formData.level" min="0" max="10" step="1" validation="required" :validation-messages="{required: 'Level is required.'}" />
                        </div>
                            </div>
                            
                        </div>

                        
                        
                    </div>
                    <div class="ButtonGroup">
                    <button type="button" class="skipBtn" @click="onFormSubmit2" >
                   <span class="btnText">Skip Form</span>
                    </button>
                    <button type="submit" class="nextBtn">
                    <span class="btnText">Finish & Go Next</span>
                    </button>
                </div>
                    
                </div> 
            </div>
        </FormKit>
        
        
    
    </div>

  </template>
  <template v-else>
    <div class="completed-form" style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <span>Optional form completed, click below to edit or view your stats.</span>
    <br>
    <button class="nextBtn" @click="onEditClick()">Edit</button>
    <button class="nextBtn" @click="goToStats()" style="margin: 10px;">View Stats</button>
</div>
        </template>
</template>


<script>

// The script code will send axios requests to the backend with the user inputs to send the data to the personform table in the database.
// It will also obtain the status of the form to see if it's completed and based off of that information it will either show the form or the edit form screen.
// Contains code to obtain the user's profile picture opon arrival on webpage

import axios from 'axios'
import Exercise1Page from './Exercise1Page.vue'
import store from '../store';


export default{
    name: 'ExercisePage',

    data (){
        return{
          isHidden: false,

          formData: {
            firstname: '',
            gender: '',
            phone: '',
            weight: '',
            birth: '',
            heightFeet: '',
            heightInch: '',
            experience: '',
            level: '',

          },
          exerciseOPTfilledout: 0,
          profileImage: null,

        }
      },
      methods: {
        async createExerciseData(){
          const data = {
            userID: localStorage.getItem('userID'),
            firstname: this.formData.firstname,
            gender: this.formData.gender,
            phone: this.formData.phone,
            weight: this.formData.weight,
            birth: this.formData.birth,
            heightFeet: this.formData.heightFeet,
            heightInch: this.formData.heightInch,
            experience: this.formData.experience,
            level: this.formData.level
          }
         axios.post('http://127.0.0.1:5000/exerciseOPT', data)
          .then(response => console.log(response))
          localStorage.setItem('phone', this.formData.phone)
          localStorage.setItem('name', this.formData.firstname)
          .catch(error => console.log(error))
          await new Promise((r) => setTimeout(r, 1500))

        },
        async getUserProfile(userID) {
  axios.get(`http://localhost:5000/profile?userID=${userID}`)
    .then(response => {
      const data = response.data[0];
      this.profileImage = data.profileImage;

      store.dispatch('updateProfileImage', data.profileImage);

    })
    .catch(error => {
      console.log(error);
    });
},
        async sendText() {
            const data = {
              number: this.formData.phone,
              message: 'Thanks for filling out the optional form, ' + this.formData.firstname
            }
            axios.post('http://127.0.0.1:5000/send_sms', data)
              .then(response => console.log(response))
              .catch(error => console.log(error))
            await new Promise((r) => setTimeout(r, 1500))
          },
        async updateFormStatus(userID) {
             axios.post(`http://localhost:5000/updateStatus?userID=${userID}`)
                .then(response => {

                })
                .catch(error => {console.log(error);
                }) 
                await new Promise((r) => setTimeout(r, 1500));
        },
        async getFormStatus(userID) {
            axios.get(`http://localhost:5000/status?userID=${userID}`)
                .then(response => {
                const data = response.data[0];
                this.exerciseOPTfilledout = data.exerciseOPTfilledout;
                })
                .catch(error => {
                console.log(error);
                });
            await new Promise((r) => setTimeout(r, 1500));
            },



        async onFormSubmit() {
            this.sendText();
            this.createExerciseData();
            this.updateFormStatus(localStorage.getItem('userID'));
            this.$router.push({ name: "exercise1" });
            await new Promise((r) => setTimeout(r, 1500));
        },
        onEditClick(){
        this.exerciseOPTfilledout = 0;

        },

        goToStats(){
          this.$router.push({ name: "stats" });
        },

        async onFormSubmit2() {
            this.updateFormStatus(localStorage.getItem('userID'));
            this.$router.push({ name: "exercise1" });
            await new Promise((r) => setTimeout(r, 1500));
        },
        

      },
      created(){
        this.getFormStatus(localStorage.getItem('userID'));
        this.getUserProfile(localStorage.getItem('userID'));
     },

      components: {
        Exercise1Page,
      }
}

</script>
 


<style>

.nextBtn:hover{
    background-color: #474b4f;
}

.button-container {
  display: flex;
  justify-content: center;
}



[data-type=checkbox] .formkit-fieldset{
border: none !important;
}


.completed-form {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.16);
  padding: 20px;
  z-index: 4;
}

.completed-form span {
  display: block;
  font-size: 24px;
  margin-bottom: 10px;
}

.completed-form button {
  display: block;
  margin: 0 auto;
  background-color: #4CAF50;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.completed-form button:hover {
  background-color: #3e8e41;
}

.message{
  display: none;
  position: absolute;
}

[data-type=range] .formkit-label{
position: relative;
left: 20px;
top: -30px;

}


.range-slider-containere {
  display: flex;
  align-items: center;
  justify-content: space-between; 
  margin-top: 50px;
  
}

.range-slider-container2 {
  display: flex;    
  align-items: center;
  justify-content: center; 
  margin-top: 50px;
  margin-left: 150px;

}

.range-slider-value {
  margin-right: 10px;
  font-size: 24px;
  font-weight: bold;
  min-width: 30px;
  color: #72b264;
}

.range-slider {
  max-width: 300px;
  width: 300px;
}

input[type="range"] {
  -webkit-appearance: none !important;
  appearance: none !important;
  width: 100% !important;
  height: 10px !important;
  border-radius: 5px !important;
  outline: none !important;
  padding: 0 !important;
  margin: 0 !important;

}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none !important;
  width: 20px !important;
  height: 20px !important;
  border-radius: 50% !important;
  background-color: #2c3e50 !important;
  cursor: pointer !important;
}

input[type="range"]::-webkit-slider-runnable-track {
  height: 10px !important;
  border-radius: 5px !important;
}

input[type="range"]:focus {
  outline: none !important;
}

input[type="range"]:focus::-webkit-slider-thumb {
  box-shadow: 0 0 0 3px #fff, 0 0 0 6px #72b264 !important;
  
}

input[type="range"]::-moz-range-thumb {
  width: 20px !important;
  height: 20px !important;
  border-radius: 50% !important;
  background-color: #72b264 !important;
  cursor: pointer !important;
  
}

input[type="range"]::-moz-range-track {
  height: 10px !important;
  border-radius: 5px !important;
  background-color: #d7dcdf !important;
  border: none!important;
}

input[type="range"]:focus::-moz-range-thumb {
  box-shadow: 0 0 0 3px #fff, 0 0 0 6px #72b264 !important;
}

input[type="range"]::-ms-thumb {
  width: 20px !important;
  height: 20px !important;
  border-radius: 50% !important;
  background-color: #72b264 !important;
  cursor: pointer !important;
}

input[type="range"]::-ms-track {
  height: 10px !important;
  border-radius: 5px !important;
  background-color: #d7dcdf !important;
  border: none !important;
}

input[type="range"]:focus::-ms-thumb {
  box-shadow: 0 0 0 3px #fff, 0 0 0 6px #72b264 !important;
}

[data-type="tel"] .formkit-inner{
width: 170px !important;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 1px !important;
margin-top: 30px;
}

[data-type="tel"] .formkit-input{
  line-height: 25px;

}


.texIn{
width: 170px !important;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 1px !important;
margin-top: 30px;
height: 50px
}



[data-type] .formkit-messages{
    position: absolute;
}



.backgroundmin{

  position: fixed;
    top: 0;
    bottom:0;
    left:0;
    width: 100%;
    height: 100%;
    z-index: -1;
}




.containere{
    position: relative;
    min-width: 900px;
    border-radius: 10px;
    padding: 30px;
    margin: auto;
    background-color: #fff;
    box-shadow: 0 3px 15px rgba(0,0,0,0.2);
    top: 50%;
    transform: translateY(10%);
    min-height: 680px;

}
.containere header{
    position: relative;
    font-size: 20px;
    font-weight: 600;
    color: #333;
}
.container2 header{
    position: relative;
    font-size: 20px;
    font-weight: 600;
    color: #333;
}
.containere header::before{
    content: "";
    position: absolute;
    left: 0;
    bottom: -5px;
    height: 3px;
    width: 65px;
    border-radius: 8px;
    background-color: #72b264;
}
.containere form{
    position: relative;
    margin-top: 16px;
    min-height: 650px;
    background-color: #fff;
    overflow: hidden;
}
.containere form .form{
    position: absolute;
    background-color: #fff;
    transition: 0.3s ease;
    
}

.containere form .title{
    display: block;
    margin-bottom: 8px;
    font-size: 16px;
    font-weight: 500;
    margin: 0;
    color: #333;
}

.containere form .secondtitle{
    display: block;
    margin-bottom: 8px;
    font-size: 18px;
    font-weight: 500;
    margin: 0;
    color: black;
    border-bottom: 3px solid #474b4f;
    padding-bottom: 4px;
}


.containere form .fields{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
   
}
form .fields .input-field{
    display: flex;
    width: calc(100% / 3 - 15px);
    flex-direction: column;
    margin: -5px 0;
    margin-bottom: 15px;
}

form .fields .input-fieldMore{
    display: flex;
    width: calc(100% / 3 - 15px);
    flex-direction: row;
    margin: 4px 0;
    margin-bottom: 15px;

}

form .fields .input-fieldTwo{
    display: flex;
    width: calc(100% / 2 - 15px);
    margin: 4px 0;
    margin-bottom: 15px;
 
}



.input-field input :focus,
.input-field select:focus{
    box-shadow: 0 3px 6px rgba(0,0,0,0.13);
}
.input-field select,
.input-field input[type="date"]{
    color: #707070;
}
.input-field input[type="date"]:valid{
    color: #333;
}
.containere form button, .backBtn{
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
    transition: all 0.3s linear;
    cursor: pointer;
}

.skipBtn{
    height: 45px;
    max-width: 400px;
    width: 40%;
    border: none;
    outline: none;
    color: #fff;
    border-radius: 5px;
    background-color: #474b4f;
    transition: all 0.3s linear;
    cursor: pointer;
    
}

.nextBtn{
    height: 45px;
    max-width: 400px ;
    width: 40%;
    border: none;
    outline: none;
    color: #fff ;
    border-radius: 5px;
    background-color: #72b264 ;
    transition: all 0.3s linear;
    cursor: pointer;
    
}

.nextBtn:hover{
    background-color: #474b4f;
}

.skipBtn:hover{
    background-color: #72b264;
}



.btnText{
    font-size: 18px;
    font-weight: 500;
}




* {
  font-family: 'KoHo', sans-serif !important; 
}

.LogButtonE{
padding: 10px !important;
width: 395px !important;
border-radius: var(--fk-border-radius) !important;
background-color: #72b264 !important;
font-size: 16px !important;
border: 4px solid #72b264 !important;
color: #fff !important;
transition: ease-in-out 0.2s !important;
}

.LogButtonE:hover{
  background-color: #474b4f !important;
  border: 4px solid #474b4f !important;
  color: #fff !important;
  cursor: pointer !important;
}

.LogButtonE:active {
  background-color: #72b264 !important;
  border: 4px solid #72b264 !important;
  color: #474b4f !important;
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

[data-type=number] .formkit-inner{
width: 170px !important;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
height: 50px
}

[data-type=date] .formkit-inner{
width: 170px !important;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
height: 50px
}



[data-type=text] .formkit-label{
 padding-bottom: -30px !important;
 position: relative;
 top: 28px;
 font-weight: normal;
}

[data-type=select] .formkit-label{
 padding-bottom: -30px !important;
 position: relative;
 top: 28px;
 font-weight: normal;
 
}

[data-type=date] .formkit-label{
 padding-bottom: -30px !important;
 position: relative;
 top: 28px;
 font-weight: normal;
 
}

[data-type=tel] .formkit-label{
 padding-bottom: -30px !important;
 position: relative;
 top: 28px;
 font-weight: 50 !important;
 
}

[data-type] .formkit-label{

 font-weight: 50 !important;
 
}

.labelW{ padding-bottom: -50px !important;
 position: relative;
 top: 28px;
 margin-top: -30px;
 }

 

.labelR{
  
 display: none !important;
}



.inputs{
  display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    margin-bottom: -20px;
}

.inputsS{

    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    margin-bottom: 70px;
    margin-top: 40px;
}

.text{
 margin-left: -33px;
 width: 80px !important;
}

.textW{
 margin-left: -33px;

 width: 170px !important;
}

.textWH{
 margin-left: -33px;

 width: 170px !important;
}

.textWF{
 margin-left: -33px;
 width: 70px !important;
}

.textWI{
 margin-left: 20px;
 width: 70px !important;
}

.select{
 margin-left: -33px;
 width: 160px !important;
}


.styledformE{
background-color: #fff;
text-align: left;
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

.ETitle{

    font-size: 45px;
    color:#474b4f;
    text-align: left;
    margin-top: -30px;
    margin-left: -10px;

}

.ETitle2{

font-size: 18px;
color:#97a0ab;
text-align: left;
margin-bottom: -10px;

border-bottom:4px solid black;
padding-bottom: 15px;


}

[data-type="select"] .formkit-inner{
width: 170px !important;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
}

[data-type="select"] .formkit-input{
  line-height: 25px;

}

.LogButtonE{
padding: 10px;
width: 430px;
background-color: #4d4f47;
font-size: 16px;
border: 4px solid #474b4f;
color: #fff;
transition: ease-in-out 0.2s;
}

.LogButtonE:hover{
  background-color: #72b264;
  border: 4px solid #72b264;
  color: #fff;
  cursor: pointer;
}

.LogButtonE:active {
  background-color: #474b4f;
  border: 4px solid #474b4f;
  color: #474b4f
}


</style>