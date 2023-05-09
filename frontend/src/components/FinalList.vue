<!-- Author: Kaden Nesch -->
<!-- This template will lead users to the page after they press finalize list where they can display their finished list with all the relevant data -->
<!-- Once on this page, they can create a pdf of this page or they can go back and edit their list or create a new list altogether -->

<template>
   <section  class="pt-5 pb-5">
  <div class="container p-5">
    <div class="row w-100">
        <div id="pdf-content" class="col-lg-12 col-md-12 col-12">
          <h3 class="display-5 mb-2 text-center">{{this.listName}}    <font-awesome-icon v-if="priority !== ''"
        :icon="['fa', 'circle']"
        :style="{
          color: priority === 'low' ? '#72b264' : priority === 'medium' ? '#ffc107' : '#f44336',
          '--fa-animation-delay': '1s',
          '--fa-animation-duration': '1.3s',
          '--fa-animation-iteration-count': '2',
        }"
        bounce></font-awesome-icon></h3>
            
            <p class="text-center mb-5">
              {{this.description ? this.description : ''}}
          </p>
            <div class="d-flex justify-content-center">
          <button @click="createPdf()" class="btn btn-light"> 
            <font-awesome-icon icon="fa-solid fa-file-pdf"></font-awesome-icon>
             Generate PDF
           
          </button>
        </div>
            <table  id="shoppingCart" class="table table-condensed table-responsive">
                <thead>
                    <tr>
                      <th style="width: 45%">Product</th>
                  <th style="width: 15%">Calories</th>
                  <th style="width: 12%">Price</th>
                  <th style="width: 10%">Quantity</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="product in items" :key="product.item_name">
                        <td data-th="Product">
                            <div class="row">
                                <div class="col-md-3 text-start">
                                    <img :src="product.images_front_full_url" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow ">
                                </div>
                                <div class="col-md-9 text-start mt-sm-2">
                                   
                                  <h4>{{ product.item_name }}</h4>
                                    <p class="font-weight-light">{{product.brand_name}}</p>
                                    <p v-if="product.allergy === 1" class="alert alert-danger" role="alert">
                                    Hazard: Remove item, contains ingredient(s) that will cause you an allergic reaction.
                                  </p>
                                  <p v-if="product.diet === 1" class="alert alert-warning" role="alert">
                                    Warning: Remove item, contains ingredient(s) that do not fit your current diet.
                                    
                                  </p>
                                  <button class="btn Expand"  @click="product.showInfo = !product.showInfo"><font-awesome-icon :icon="product.showInfo ? 'fa-solid fa-angles-up' : 'fa-solid fa-angles-down'"></font-awesome-icon></button>
                                  <div v-if="product.showInfo">
                                    
                                    <span v-if="product.nf_calories_from_fat !== null"><b>Calories from Fat:</b> {{ product.nf_calories_from_fat }}</span>
                                    <p v-if="product.nf_total_fat !== null"><b>Total Fat:</b> {{ product.nf_total_fat }}g </p>
                                    <span v-if="product.nf_saturated_fat !== null"><b>Saturated Fat:</b> {{ product.nf_saturated_fat }}g </span>
                                    <span v-if="product.nf_trans_fatty_acid !== null"><b>Trans Fatty Acid:</b> {{ product.nf_trans_fatty_acid }}g </span>
                                    <span v-if="product.nf_polyunsaturated_fat !== null"><b>Polyunsaturated Fat:</b> {{ product.nf_polyunsaturated_fat }}g </span>
                                    <span v-if="product.nf_monounsaturated_fat !== null"><b>Monounsaturated Fat:</b> {{ product.nf_monounsaturated_fat }}g </span>
                                    <span v-if="product.nf_cholesterol !== null"><b>Cholesterol:</b> {{ product.nf_cholesterol }}mg </span>
                                    <p v-if="product.nf_sodium !== null"><b>Sodium:</b> {{ product.nf_sodium }}mg </p>
                                    <p v-if="product.nf_total_carbohydrate !== null"><b>Total Carbohydrate:</b> {{ product.nf_total_carbohydrate }}g </p>
                                    <span v-if="product.nf_dietary_fiber !== null"><b>Dietary Fiber:</b> {{ product.nf_dietary_fiber }}g </span>
                                    <span v-if="product.nf_sugars !== null"><b>Sugars:</b> {{ product.nf_sugars }}g </span>
                                    <p v-if="product.nf_protein !== null"><b>Protein:</b> {{ product.nf_protein }}g </p>
                                    <span v-if="product.nf_vitamin_a_dv !== null"><b>Vitamin A:</b> {{ product.nf_vitamin_a_dv }}% </span>
                                    <span v-if="product.nf_vitamin_c_dv !== null"><b>Vitamin C:</b> {{ product.nf_vitamin_c_dv }}% </span>
                                    <span v-if="product.nf_calcium_dv !== null"><b>Calcium:</b> {{ product.nf_calcium_dv }}% </span>
                                    <span v-if="product.nf_iron_dv !== null"><b>Iron:</b> {{ product.nf_iron_dv }}% </span>
                                    <span v-if="product.nf_potassium !== null"><b>Potassium:</b> {{ product.nf_potassium }}mg </span>
                                    <p v-if="product.nf_servings_per_container !== null"><b>Servings Per Container:</b> {{ product.nf_servings_per_container }}</p>
                                    <span v-if="product.nf_serving_size_qty !== null && product.nf_serving_size_unit !== null"><b>Serving Size:</b> {{ product.nf_serving_size_qty }} {{ product.nf_serving_size_unit }}</span>
                                    <p  v-if="product.nf_ingredient_statement !== null"><b>Ingredients:</b> {{ product.nf_ingredient_statement }}</p>
                                  </div>
                                </div>
                            </div>
                        </td>
                        <td data-th="Calories">{{product.nf_calories}}</td>
                        <td data-th="Price">{{product.item_price}}</td>
                        <td data-th="Quantity" class="text-center">{{ product.quantity }}</td>

                    </tr>
                </tbody>
            </table>

              <div class="row">
  <div class="col-5 text-end">
    <h4>Total Price:</h4>
    <h1>${{ subtotal }}</h1>
  </div>
  <div class="col-4 text-end">
    <h4>Total Calories:</h4>
    <h1>{{ subtotalCals}}</h1>
  </div>
</div>

        </div>
    </div>
    <div class="row d-flex align-items-center">
      <div class="col-sm-6 mb-3 mb-m-1 order-md-1 text-md-start">
            <a class="btn btn-light hvr-shrink" @click="goBack">
                <font-awesome-icon icon="fa-solid fa-arrow-left mr-2"></font-awesome-icon> Continue Browsing
            </a>
        </div>
        <div class="col-sm-6 order-md-2 text-end">
            <a class="btn btn-primary btn-block custom-button mb-4 btn-lg px-5" @click="goToHome">
                Go to Home
            </a>
        </div>
    </div>
</div>
</section>
</template>
<script>

// The script will send get requests to retrieve the stored list that the user has sent to the backend and display it. 
// Contains code that allows users to generate a pdf of the page so that their entire list is visible.
// Contains code to obtain the user's profile picture opon arrival on webpage

import html2pdf from 'html2pdf.js'
import store from '../store';
import axios from 'axios';
import { mapGetters } from 'vuex'
export default {
    name: 'FinalList',
    mounted(){
      this.getList(localStorage.getItem('userID'), localStorage.getItem('activeList'));
    },
    props: ['cartItems'],

    data() {
        return{
            items: [],
            listName: '',
            description: '',
            priority: '',
            profileImage: null,
            
        }
    },
    created(){
  this.listName = localStorage.getItem('activeList')
  this.description = localStorage.getItem('activeDescription')
  this.priority = localStorage.getItem('activePriority')

  
},
    methods: {
    goBack() {
      this.$router.back()
    },
    async getList(userID, listName) {
        axios.get(`http://localhost:5000/lists?userID=${userID}&listName=${listName}`)
                .then(response => {
                  this.items = response.data;
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
goToHome(){

setTimeout(() => {
  this.$router.push('/');
}, 500); 
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
          filename: 'my_cart.pdf',
          image: { type: 'jpeg', quality: 0.98 },
          html2canvas: { dpi: 192, letterRendering: true },
          jsPDF: { unit: 'pt', format: 'letter', orientation: 'portrait' },
        })
        .from(clonedElement)
        .save()
    },
  },
  computed: {
    ...mapGetters(['cart', 'subtotal', 'subtotalCals']),
    cartItems() {
      return this.cart.map(item => ({
        ...item,
        name: item.item_name,
        price: item.item_price,
        quantity: item.quantity
      }));
    }
  }
}
</script>
<style >
    
</style>