<template>
   <section  class="pt-5 pb-5">
  <div class="container p-5">
    <div class="row w-100">
        <div id="pdf-content" class="col-lg-12 col-md-12 col-12">
            <h3 class="display-5 mb-2 text-center">"Grocery List Name"</h3>
            <h5 class="mb-5 text-center">
                You have <i class="text-info font-weight-bold">3</i> items in your list
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
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td data-th="Product">
                            <div class="row">
                                <div class="col-md-3 text-start">
                                    <img src="../assets/240.png" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow ">
                                </div>
                                <div class="col-md-9 text-start mt-sm-2">
                                    <h4>Product Name</h4>
                                    <p class="font-weight-light">Nutritional Information</p>
                                </div>
                            </div>
                        </td>
                        <td data-th="Price">$49.00</td>

                    </tr>
                    <tr>
                        <td data-th="Product">
                            <div class="row">
                                <div class="col-md-3 text-start">
                                    <img src="../assets/240.png" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow ">
                                </div>
                                <div class="col-md-9 text-start mt-sm-2">
                                    <h4>Product Name</h4>
                                    <p class="font-weight-light">Nutritional Information</p>
                                </div>
                            </div>
                        </td>
                        <td data-th="Price">$49.00</td>

                    </tr>
                    <tr>
                        <td data-th="Product">
                            <div class="row">
                                <div class="col-md-3 text-start">
                                    <img src="../assets/240.png" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow ">
                                </div>
                                <div class="col-md-9 text-start mt-sm-2">
                                    <h4>Product Name</h4>
                                    <p class="font-weight-light">Nutritional Information</p>
                                </div>
                            </div>
                        </td>
                        <td data-th="Price">$49.00</td>
                    </tr>
                </tbody>
            </table>
            <div class="d-flex justify-content-center">
  <div class="text-end mx-auto">
    <h4>Subtotal:</h4>
    <h1>$99.00</h1>
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

export default {
    name: 'FinalList',
    methods: {
    goBack() {
      this.$router.back()
    },
    createPdf() {
    const element = document.getElementById('pdf-content')
    html2pdf().from(element).save()
  }
  },
}
</script>
<style >
    
</style>