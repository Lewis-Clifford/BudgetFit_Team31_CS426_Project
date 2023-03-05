<template >
    <section class="pt-5 pb-5">
  <div class="container p-5">
    <div class="row w-100">
        <div class="col-lg-12 col-md-12 col-12">
            <h3 class="display-5 mb-2 text-center">"Grocery List Name"</h3>
            <p class="mb-5 text-center">
                <i class="text-info font-weight-bold">3</i> items in your list</p>
            <table id="shoppingCart" class="table table-condensed table-responsive">
                <thead>
                    <tr>
                        <th style="width:60%">Product</th>
                        <th style="width:12%">Price</th>
                        <th style="width:10%">Quantity</th>
                        <th style="width:16%"></th>
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
                                    <p class="font-weight-light">Brand &amp; Name</p>
                                </div>
                            </div>
                        </td>
                        <td data-th="Price">$49.00</td>
                        <td data-th="Quantity">
                            <input type="number" min="1" max="16" class="form-control form-control-lg text-center" value="1">
                        </td>
                        <td class="actions" data-th="">
                            <div class="text-end">
                                <button class="btn btn-lg btn-light hvr-shrink">
                                    <font-awesome-icon icon="fa-solid fa-trash"></font-awesome-icon>
                                </button>

                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td data-th="Product">
                            <div class="row">
                                <div class="col-md-3 text-start">
                                    <img src="../assets/240.png" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow ">
                                </div>
                                <div class="col-md-9 text-start mt-sm-2">
                                    <h4>Product Name</h4>
                                    <p class="font-weight-light">Brand &amp; Name</p>
                                </div>
                            </div>
                        </td>
                        <td data-th="Price">$49.00</td>
                        <td data-th="Quantity">
                            <input type="number" min="1" max="16" class="form-control form-control-lg text-center" value="1">
                        </td>
                        <td class="actions" data-th="">
                            <div class="text-end">
                                <button class="btn btn-lg btn-light hvr-shrink">
                                    <font-awesome-icon icon="fa-solid fa-trash"></font-awesome-icon>
                                </button>

                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td data-th="Product">
                            <div class="row">
                                <div class="col-md-3 text-start">
                                    <img src="../assets/240.png" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow ">
                                </div>
                                <div class="col-md-9 text-start mt-sm-2">
                                    <h4>Product Name</h4>
                                    <p class="font-weight-light">Brand &amp; Name</p>
                                </div>
                            </div>
                        </td>
                        <td data-th="Price">$49.00</td>
                        <td data-th="Quantity">
                            <input type="number" min="1" max="16" class="form-control form-control-lg text-center" value="1">
                        </td>
                        <td class="actions" data-th="">
                            <div class="text-end">
                                <button class="btn btn-lg btn-light hvr-shrink">
                                    <font-awesome-icon icon="fa-solid fa-trash "></font-awesome-icon>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="float-end text-end">
                <h4>Subtotal:</h4>
                <h1>$99.00</h1>
            </div>
        </div>
    </div>
    <div class="row mt-4 d-flex align-items-center">
        <div class="col-sm-6 order-md-2 text-end">
            <a @click="nextPage()" class="btn btn-primary btn-block custom-button mb-4 btn-lg px-5">Finalize List</a>
        </div>
        <div class="col-sm-6 mb-3 mb-m-1 order-md-1 text-md-start">
            <a class="btn btn-light hvr-shrink" @click="goBack">
                <font-awesome-icon icon="fa-solid fa-arrow-left mr-2"></font-awesome-icon> Continue Browsing
            </a>
        </div>
    </div>
</div>
</section>
</template>
<script>
import router from '@/router';

export default {
    name: 'Cart',
    methods: {
    goBack() {
      this.$router.back()
    },
    nextPage(){
         router.push('/finallist')

        }
  },
    
}
</script>
<style>
    
</style>
