<template>
<img class="backgroundmin" src="../assets/green.jpg">
<div class="cont">
<div class="container2">
        <header>Let us know about any dietary restrictions & preferences.</header>

        <FormKit  message-class="message" type="form" :actions="false" @submit="createDietData()">
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
                            'Vegan Diet (No meat or dairy)', 'Carnivore Diet (Strictly animal based)', 'Pescatarian (Vegetarian but can consume fish)'
                            ,'Paleo Diet (No processed foods)']"></FormKit>
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
    name: 'DietPage',
    data() {
        return{
            formData: {
            diet: '',
            allergy: '',
            }
        }
    },
    methods: {
        async createDietData(){
         axios.post('http://127.0.0.1:5000/exerciseOPT', this.formData)
          .then(response => console.log(response))
          .catch(error => console.log(error))
          await new Promise((r) => setTimeout(r, 1500))

        }
     }
}
</script>

<style scoped>

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



.containerd{
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