<template>
   <section  class="pt-5 pb-5">
  <div class="container p-5">
    <div class="row w-100">
        <div id="pdf-content" class="col-lg-12 col-md-12 col-12">
            <h3 class="display-5 mb-2 text-center">"Grocery List Name"</h3>
            <h5 class="mb-5 text-center">
                You have <i class="text-info font-weight-bold">{{ cart.length }}</i> products in your list
            </h5>
            <div class="d-flex justify-content-center">
          <button @click="createPdf()" class="btn btn-light"> 
            <font-awesome-icon icon="fa-solid fa-file-pdf"></font-awesome-icon>
             Generate PDF
           
          </button>
        </div>
            <table  id="shoppingCart" class="table table-condensed table-responsive">
                <thead>
                    <tr>
                        <th style="width:60%">Product</th>
                        <th style="width:10%">Price</th>
                        <th style="width:10%">Quantity</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="product in cart" :key="product.item_name">
                        <td data-th="Product">
                            <div class="row">
                                <div class="col-md-3 text-start">
                                    <img :src="product.images_front_full_url" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow ">
                                </div>
                                <div class="col-md-9 text-start mt-sm-2">
                                    <h4>{{ product.item_name }}</h4>
                                    <p class="font-weight-light">{{product.brand_name}}</p>
                                </div>
                            </div>
                        </td>
                        <td data-th="Price">{{product.item_price}}</td>
                        <td data-th="Quantity" class="text-center">{{ product.quantity }}</td>

                    </tr>
                </tbody>
            </table>
            <div class="d-flex justify-content-center">
  <div class="text-end mx-auto">
    <h4>Subtotal:</h4>
    <h1>${{subtotal}}</h1>
  </div>
</div>
        </div>
    </div>
    <div class="row d-flex align-items-center">
        <div class="col-sm-6 mb-3 mb-m-1 order-md-1 text-md-start">
            <a class="btn btn-lg btn-light hvr-shrink" @click="goBack">
                <font-awesome-icon icon="fa-solid fa-pen-to-square"></font-awesome-icon> Edit List
            </a>
        </div>
    </div>
</div>
</section>
</template>
<script>
import html2pdf from 'html2pdf.js'
import { mapGetters } from 'vuex'
export default {
    name: 'FinalList',
    props: ['cartItems'],
    methods: {
    goBack() {
      this.$router.back()
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
    ...mapGetters(['cart', 'subtotal']),
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