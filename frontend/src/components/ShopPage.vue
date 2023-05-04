<template>
    <div class="containergrocery">
      <h1 class="groceryTitle">Grocery List</h1>
      <FormKit type="form" :actions="false" @submit="together()">
        <div class="form-group">
          <div class="input-field">
                            <FormKit :floating-label="false" placeholder="Enter Grocery List"
                             inner-class="texInGroc" v-model="listname" id="listname"
                             validation="required|length:1,30" validation-label="Grocery List Name"
                              type="text" label="Grocery List Name (Required):" 
                              label-class="labelSize"></FormKit>
                        </div>
        </div>
        <br>
        <div class="form-group">
          <label for="priority" class="labelSize">Priority (Optional):</label>
          <div class="radio-buttons">
            <br>
            <label :class="{ 'low-priority': priority === 'low' }">
              <input type="radio" name="priority" value="low" v-model="priority">
              Low
            </label>
            <label :class="{ 'medium-priority': priority === 'medium' }">
              <input type="radio" name="priority" value="medium" v-model="priority">
              Medium
            </label>
            <label :class="{ 'high-priority': priority === 'high' }">
              <input type="radio" name="priority" value="high" v-model="priority">
              High
            </label>
          </div>
        </div>
        <div class="form-group">
          <label for="description" class="labelSize">Description (Optional):</label>
          <br>
          <textarea id="description" v-model="description"></textarea>
        </div>
        <button class="nextBtn" type="submit">Save</button>
        <button class="skipBtn2" @click="nextPage">Skip</button>
    </FormKit>
    </div>
  </template>
  
  <script>
import store from '../store';
import router from '@/router'
import axios from 'axios'
  export default {
    name: 'ShopPage',

    data() {
      return {

        listname: '',
        priority: '',
        description: '',
        listNames: [],
        listPriorities: [],
        listDescriptions: [],
        profileImage: null,
        
      }
    },
    created() {
      this.getUserProfile(localStorage.getItem('userID'));
    },
    methods: {
        async createGroceryList(){
          const data = {
                userID: localStorage.getItem('userID'),
                listname: this.listname,
                priority: this.priority,
                description: this.description
            }
          axios.post('http://127.0.0.1:5000/newList', data)
          .then(response => console.log(response))
          .catch(error => console.log(error))
          await new Promise((r) => setTimeout(r, 1500))
    

        }, 
        async names(userID) {
        axios.get(`http://localhost:5000/newList?userID=${userID}`)
                .then(response => {
                  const data = response.data;
                  this.listNames = data.map(list => list.listName);
                  this.listPriorities = data.map(list => list.priority)
                  this.listDescriptions = data.map(list => list.description)
                  localStorage.removeItem("activeList");
                  localStorage.setItem('activeList', this.listNames[0]);
                  localStorage.setItem('activePriority', this.listPriorities[0]);
                  localStorage.setItem('activeDescription', this.listDescriptions[0]);
                })
                .catch(error => {
                console.log(error);
                });
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
          
            

        nextPage(){
         router.push('/viewshop')

        },

        together(){
          this.createGroceryList().then(() => {
            this.names(localStorage.getItem('userID'));
            this.nextPage();
          }).catch(error => {
            console.log(error);
          });
        }
    
      },

  }
  </script>
  
  <style >

.skipBtn2{
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
    margin-left: 40px;
    
}

.skipBtn2:hover{
    background-color: #72b264;
}

  .labelSize{
    font-size: 18px !important;
    padding-bottom: 10px;
  }

.texInGroc{
width: 250px !important;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 1px !important;
margin-top: 30px;
height: 50px
}

.containergrocery {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: sans-serif;
  margin: auto;
  position: relative;
  min-width: 900px;
  border-radius: 10px;
  padding: 30px;
  top: 50%;
  transform: translateY(10%);
  min-height: 680px;
}

.groceryTitle{
font-size: 45px;
color: #72b264;

}

  
  .form-group {
    margin-bottom: 20px;
  }
  
  .radio-buttons label {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.3s ease-in-out;
  }
  
  .radio-buttons input[type="radio"] {
    display: none;
  }
  
  .low-priority {
    background-color: #72b264;
    color: #fff;
  }
  
  .medium-priority {
    background-color: #ffc107;
    color: #fff;
  }
  
  .high-priority {
    background-color: #f44336;
    color: #fff;
  }
  
  textarea {
    width: 100%;
    padding: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
    font-family: sans-serif;
  }
  </style>