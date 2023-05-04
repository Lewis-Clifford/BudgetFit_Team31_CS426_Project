<template>
    
<div class="cont" >
    <template v-if="dietFilledout === 0">
<div class="container2" >
    
        <header>Let us know about any dietary restrictions & preferences.</header>

        <FormKit message-class="message" type="form" :actions="false" @submit="onFormSubmit(formData)">

            <div class="form first">
                
              <span class="title">This form is required to assure proper shopping and diet information.
   
                      </span>
                <div class="detailspersonal">
                    
                   <br>
                    <span class="dietTitleReq">
                    Diet Information
                    </span>
                    
                    
                    <div class="fieldsReq">
                        <div class="input-fieldReq">
                            <FormKit type="checkbox"  label="Diet" v-model="formData.diet"
                            help="Based on your selection, we will warn or indicate if you have chosen an item that contains
                            food products that your diet prohibits" validation="required"
                            :options="['Keto Diet (Low-no carbohydrates)', 'Vegetarian Diet (No meat)', 
                            'Vegan Diet (No meat or dairy)', 'Pescatarian (Vegetarian but can consume fish)'
                            ,'Low-Sodium Diet']"></FormKit>
                        </div>
                      </div>
                      <span class="dietTitleReq">
                    Allergy Information 
                    </span>
                      <div class="fieldsReq">
                        <div class="input-fieldReq">
                            <FormKit type="checkbox" label="Allergy" placeholder="Dietary Allergies"
                            v-model="formData.allergy" validation="required"
                            help="Based on your selection, indicate from a scale of 1-5 how serious your allergy is, 1 being very mild and 5 being deadly.
                            We will provide hazard warnings if food contain an allergy item."
                            :options="['Peanut', 'Dairy', 'Gluten', 'Eggs', 'Crustaceans', 'Soy', 'Fish' ]"></FormKit>
                            <div class="form-group">
                              <help>Custom allergy:</help>
                              <input type="text" class="form-control" v-model="formData.customAllergy" name="customAllergy">
                          </div>
                         </div>
                      </div>
                </div>

                <div class="ButtonGroup" >
                    
                    <button type="submit" class="nextBtn">
                    <span class="nes">Finish</span>
                    </button>
                </div> 
                
            </div>
        </FormKit>
        
    
    
    </div>
</template>
<template v-else>
            <div class="completed-form">
                <span>Diet form completed, click below to edit.</span>
                <button class="nextBtn" @click="onEditClick()">Edit</button>
            </div>
        </template>
</div>

</template>

<script>
import axios from 'axios'
import store from '../store';
export default{
    name: 'DietPage',
    data() {
        return{
            formData: {
            diet: '',
            allergy: '',
            customAllergy: ''
            },
            dietFilledout: 0,
            profileImage: null
            
        }
    },
    methods: {
        async createDietData(){
            const data = {
                userID: localStorage.getItem('userID'),
                diet: this.formData.diet.join(","),
                allergy: this.formData.allergy.join(","),
                customAllergy: this.formData.customAllergy
            }
         axios.post('http://127.0.0.1:5000/diet', data)
          .then(response => console.log(response))
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
        onEditClick(){
        this.dietFilledout = 0;

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
                this.dietFilledout = data.dietFilledout;
                console.log(this.dietFilledout)

                })
                .catch(error => {
                console.log(error);
                });
            await new Promise((r) => setTimeout(r, 1500));
            },
        async onFormSubmit(formData) {
            this.createDietData();
            this.updateFormStatus(localStorage.getItem('userID'));
            this.$router.push({ name: "home" });
            formData.customAllergy = this.formData.customAllergy;
            console.log(formData);
            await new Promise((r) => setTimeout(r, 1500));
        },
     },
     created(){
        this.getFormStatus(localStorage.getItem('userID'));
        this.getUserProfile(localStorage.getItem('userID'));
     }

}
</script>

<style scoped>



.searchA {
    width: 60%;
    box-sizing: border-box;
    padding: 6px 11px;
    border: 1px solid #ccc;
    border-radius: 3px;
    font-size: 12px;
    background-color: white;
    resize: vertical;
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
.ButtonGroup{
    margin-top: -45px;
}
.title{

margin-bottom: -40px !important;

}
.fieldsReq {
  display: flex;
  flex-direction: column; /* Add this to stack the checkboxes vertically */
  margin-left: 0px !important;
  align-items: flex-start; /* Add this to align the checkboxes to the left */
  justify-content: flex-start; /* Add this to align the checkboxes to the top */
  margin-top: 20px;


}

.fieldsReq .input-fieldReq {
  width: 48% !important;
}

.dietTitleReq{
    display: block;
    margin-bottom: 15px !important;
    font-size: 18px;
    font-weight: 500;
    margin: 0;
    color: black;
    border-bottom: 3px solid #474b4f;
    padding-bottom: 4px;
}



.container{
    position: relative;
    min-width: 900px;
    border-radius: 10px;
    padding: 30px;
    margin: auto;
    background-color: #fff;
    box-shadow: 0 5px 10px rgba(0,0,0,0.1);
    top: 50%;
    transform: translateY(10%);

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