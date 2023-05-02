<template >
<div class="popup-overlay" @click.self="$emit('close')">
<div class="popup-container">
    <div class="popup-content">
  
<img :src="product.images_front_full_url" style="max-width: 240px; max-height: 240px" alt="Placeholder image">
  <p>{{product.brand_name}} | {{ product.item_name }} </p>
  <p style="font-size: 25px;">${{product.item_price}}</p>
  <br>
  <button class="btn btn-primary "
    :class="{active : isActive}"
    :key="itemCount"
    @click="toggle">
    <i v-if="isActive">Item added to List</i>
    <i v-if="!isActive">Add Item to List</i>
    </button>
    <br>
  <p><b>Calories:</b> {{product.nf_calories }}

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
  <p v-if="product.nf_ingredient_statement !== null"><b>Ingredients:</b> {{ product.nf_ingredient_statement }}</p>
</p>

  <button class="popup-close" @click="$emit('close')">
    <font-awesome-icon icon="fa-solid fa-x"/></button>
    <br>

  </div>
</div>
</div>

</template>
<script>
import { mapState, mapMutations } from 'vuex';
import FavoriteComponent from './AddFavoriteShop.vue';
export default {
    name: 'PopupComponent',
    components: {
      FavoriteComponent
    },
    props:['product'],

    computed: {
      ...mapState(['cart']),
    itemCount() {
      const product = this.cart.find(i => i.item_name === this.product.item_name);
      return product ? product.quantity : 0;
    },
    isActive() {
      return this.itemCount > 0
    }
    },
    methods: {
    ...mapMutations(['addToCart', 'removeFromCart']),
    toggle() {
      const isInCart = this.isActive;
      if (isInCart) {
        this.removeFromCart(this.product);
      } else {
        this.addToCart(this.product);
      }
    },
  }

}
</script>
<style scoped>

i {
font-style: normal;
}

.btn.btn-primary.active {
  background-color: rgb(206, 217, 82);
  border-color: rgb(206, 217, 82);
}
.popup-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 3;
  width: 80%;
  max-width: 600px;
  height: 80%;
  max-height: 600px;
  background-color: white;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.04);
  overflow-y: auto;
}

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.04);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 3;
}

.popup-close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 20px;
  font-weight: bold;
  background-color: transparent;
  border: none;
  cursor: pointer;
  outline: none;
}

.popup-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 25px;
}

.popup-content img {
  max-width: 100%;

}

.popup-content p {
  text-align: center;
  margin-top: 10px;
  line-height: 1.3;
  margin-bottom: 3px;
}

</style>