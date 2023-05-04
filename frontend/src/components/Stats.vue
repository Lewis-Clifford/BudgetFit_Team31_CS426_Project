<template>
    <div class="containerz"  id="pdf-content" style="max-width: 540px">
      <div class="header">
        <h2>Your Health Statistics</h2>
      </div>
        <div class="help">*BMI and Fitness level are not 100% accurate and should not be taken as a fact*
        </div>
        <br>
        <div class="d-flex justify-content-center">
          <button @click="createPdf()" class="btn btn-light"> 
            <font-awesome-icon icon="fa-solid fa-file-pdf"></font-awesome-icon>
             Generate PDF
           
          </button>
        </div>
        <br>
      <div class="content">
        <div class="info">
        <p>Body Mass Index (BMI): <span>{{ this.BMI }}</span></p>
        <p>Assessed Fitness Level: <span>{{ this.BMICategory }}</span></p>
        <p>Daily Active Metabolic Rate (Calories to maintain weight while active): <span>{{ this.AMR }} </span> calories</p>
        <p>Daily Basal Metabolic Rate (Calories to maintain weight while inactive): <span>{{ this.BMR }} </span> calories</p>
        <p>Daily Bulking Calories: <span>{{ this.bulkCalories }}</span> calories</p>
        <p>Weekly Bulking Calories: <span>{{ this.weeklyBCals }}</span> calories</p>
        <p>Daily Cutting Calories: <span>{{ this.lossCalories }}</span> calories</p>
        <p>Weekly Cutting Calories: <span>{{ this.weeklyLCals }}</span> calories</p>
        </div>
        <br>
        <button class="nextBtnz" @click="goToHome">
                    <span class="btnText">Back to Home</span>
                    </button>
      </div>
    </div>
  </template>

<script>
import store from '../store';
import html2pdf from 'html2pdf.js'
import axios from 'axios';
export default{
    name: 'Stats',
    data() {
        return{
            BMR: 0,
            AMR: 0,
            lossCalories: 0,
            weeklyLCals: 0,
            bulkCalories: 0,
            weeklyBCals: 0,
            BMI: 0.0,
            BMICategory: '',
            profileImage: null,

        }
    },
    created(){
        this.getExerciseData(localStorage.getItem('userID'))
        this.getUserProfile(localStorage.getItem('userID'));
    },
    methods: {
        getExerciseData(userID){
            axios.get(`http://localhost:5000/exerciseProfile?userID=${userID}`)
                .then(response => {
                  const data = response.data[0];
                  console.log(data)
                  this.AMR = data.AMR;
                  this.BMR = data.BMR;
                  this.lossCalories = data.lossCalories;
                  this.weeklyLCals = data.weeklyLCals;
                  this.bulkCalories = data.bulkCalories;
                  this.weeklyBCals = data.weeklyBCals;
                  this.BMI = data.BMI;
                  this.BMICategory = data.BMICategory;
                  console.log(this.AMR)
                })
                .catch(error => {
                console.log(error);
                });
        },
        async createPdf() {
      const element = document.getElementById('pdf-content')
      const clonedElement = element.cloneNode(true)
      const images = clonedElement.querySelectorAll('img')

      for (const img of images) {
        try {
          const response = await fetch(img.src)
          const blob = await response.blob()
          const dataUrl = await new Promise(resolve => {
            const reader = new FileReader()
            reader.onloadend = () => resolve(reader.result)
            reader.readAsDataURL(blob)
          })
          img.setAttribute('src', dataUrl)
        } catch (error) {
          console.error(`Failed to convert image to data URL: ${error.message}`)
        }
      }

      html2pdf()
        .set({
          margin: [20, 20, 20, 20],
          filename: 'my_stats.pdf',
          image: { type: 'jpeg', quality: 0.98 },
          html2canvas: { dpi: 192, letterRendering: true },
          jsPDF: { unit: 'pt', format: 'letter', orientation: 'portrait' },
        })
        .from(clonedElement)
        .save()
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
        goToHome(){

    setTimeout(() => {
      this.$router.push('/');
    }, 500); 
        }
    }
}
</script>

<style>

.nextBtnz{
    height: 38px;
    max-width: 200px ;
    width: 30%;
    border: none;
    outline: none;
    color: #fff ;
    border-radius: 5px;
    background-color: #72b264 ;
    transition: all 0.3s linear;
    cursor: pointer;
    position: relative;
    left: 170px;

}

.nextBtnz:hover{
    background-color: #474b4f;
}
.containerz {
  border-radius: 8px;
  box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  padding: 20px;
  margin: 20px auto;
}

.help{
    color: rgb(132, 132, 132);
    text-align: center;
    font-size: 15px;
}

.header {
  font-size: 28px;
  font-weight: bold;
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}

 h2 {
color: #72b264;
}

.info {
  font-size: 18px;
  line-height: 1.5;
  color: #333;
}

.info p span {
  font-weight: bold;
  font-size: 18px;
}
</style>