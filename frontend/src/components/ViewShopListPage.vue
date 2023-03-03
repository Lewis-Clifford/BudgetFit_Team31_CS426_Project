<template>
<div class="container p-5" >
              <div class="row">
                <div class="col-md-8 order-md-2 col-lg-9">
                  <div class="container-fluid">
                    <div class="row mb-5">
                      <div class="col-12">
                        <div class="dropdown text-md-start text-center float-md-start mb-3 mt-3 mt-md-0 mb-md-0">
                          <label class="me-2">Sort by:</label>
                          <button class="btn btn-lg btn-light dropdown-toggle hvr-shrink"  id="dropdownMenuButton1" data-bs-toggle="dropdown" type="button" aria-expanded="false">Relevance <span class="caret"></span></button>
                          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                            <a class="dropdown-item" href="#">Relevance</a>
                            <a class="dropdown-item" href="#">Price Descending</a>
                            <a class="dropdown-item" href="#">Price Ascending</a>
                            <a class="dropdown-item" href="#">Best Selling</a>
                          </div>
                        </div>
                        <div class="btn-group float-md-end ms-3">
                          <button type="button" class="btn btn-lg btn-light hvr-shrink"> <font-awesome-icon icon="fa-solid fa-arrow-left" /> </button>
                          <button type="button" class="btn btn-lg btn-light hvr-shrink"> <font-awesome-icon icon="fa-solid fa-arrow-right" /> </button>
                        </div>
                        <div class="dropdown float-end">
                          <button type="button" class="btn btn-lg hvr-shrink me-4 btn-light">
                            <font-awesome-icon icon="fa-solid fa-shopping-cart"></font-awesome-icon>
                            <span class="badge bg-primary rounded-pill">{{ itemCount }}</span>
                          </button>
                          <label class="me-2">View:</label>
                          <button class="btn btn-lg btn-light dropdown-toggle hvr-shrink" data-bs-toggle="dropdown" id="dropdownMenuButton2" type="button" aria-expanded="false">9 <span class="caret"></span></button>
                          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown" x-placement="bottom-end" style="will-change: transform; position: absolute; transform: translate3d(120px, 48px, 0px); top: 0px; left: 0px;">
                            <a class="dropdown-item" href="#">12</a>
                            <a class="dropdown-item" href="#">24</a>
                            <a class="dropdown-item" href="#">48</a>
                            <a class="dropdown-item" href="#">96</a>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-12 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 w-85 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block " alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems"/>
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="product.html" class=" text-decoration-none text-dark small"> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                      <div class="col-6 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block" alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems"/>
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="product.html" class=" text-decoration-none text-dark small"> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                      <div class="col-6 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block" alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems"/>
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="product.html" class=" text-decoration-none text-dark small"> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                      <div class="col-6 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block" alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems"/>
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="product.html" class=" text-decoration-none text-dark small"> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                      <div class="col-6 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block" alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems"/>
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="product.html" class=" text-decoration-none text-dark small"> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                      <div class="col-6 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block" alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems"/>
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="product.html" class=" text-decoration-none text-dark small"> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                      <div class="col-6 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block" alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems"/>
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="product.html" class=" text-decoration-none text-dark small"> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                      <div class="col-6 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block" alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems"/>
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="product.html" class=" text-decoration-none text-dark small"> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                      <div class="col-6 col-md-6 col-lg-4 mb-3">
                        <div class="card h-100 border-0 hvr-float">
                          <div class="card-img-top position-relative">
                            <img src="https://via.placeholder.com/240x240/72b264/ffffff" class="img-fluid mx-auto d-block" alt="Card image cap">
                            <ButtonComponent :item="item" :cartItems="cartItems" />
                        </div>
                          <div class="card-body text-center">
                            <h4 class="card-title">
                              <a href="#" class="text-decoration-none text-dark small  "> Product name</a>
                            </h4>
                            <h5 class="card-price small font-weight-bold mb-3">
                              <i>
                                 $99</i>
                            </h5>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row mb-5 mt-5">
                      <div class="col-12">
                        <a class="btn btn-light hvr-shrink">
                          <font-awesome-icon icon="fa-solid fa-arrow-up me-2"></font-awesome-icon> Back to top</a>
                        <div class="btn-group float-md-end ms-3">
                          <button type="button" class="btn btn-lg btn-light hvr-shrink"> <font-awesome-icon icon="fa-solid fa-arrow-left" /> </button>
                          <button type="button" class="btn btn-lg btn-light hvr-shrink"> <font-awesome-icon icon="fa-solid fa-arrow-right" /> </button>
                        </div>
                        <div class="dropdown float-md-end">
                          <label class="me-2">View:</label>
                          <a class="btn btn-light btn-lg dropdown-toggle hvr-shrink" data-bs-toggle="dropdown" role="button" aria-expanded="false">12 <span class="caret"></span></a>
                          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="#">12</a>
                            <a class="dropdown-item" href="#">24</a>
                            <a class="dropdown-item" href="#">48</a>
                            <a class="dropdown-item" href="#">96</a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div><div class="col-md-4 order-md-1 col-lg-3 sidebar-filter">
                    <div class="input-group" >
                        <input class="form-control shadow-none" type="text" placeholder="Search" aria-label="Search">
                        <button type="button" class="btn btn-primary custom-button"><font-awesome-icon icon="fa-solid fa-magnifying-glass"/></button>
                    </div>
                    <div>
                      
                    </div>
                    <br>
                  <h6 class="text-uppercase font-weight-bold mb-3">Categories</h6>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-1">
                      <label class="form-check-label" for="category-1">Breads</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-2">
                      <label class="form-check-label" for="category-2">Condiments</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-3">
                      <label class="form-check-label" for="category-3">Dairy</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-4">
                      <label class="form-check-label" for="category-4">Drinks</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-5">
                      <label class="form-check-label" for="category-5">Frozen Foods</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-6">
                      <label class="form-check-label" for="category-6">Fruits</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-6">
                      <label class="form-check-label" for="category-6">Meats</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-6">
                      <label class="form-check-label" for="category-6">Pasta &amp; Rice</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-6">
                      <label class="form-check-label" for="category-6">Snacks</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-6">
                      <label class="form-check-label" for="category-6">Vegetables</label>
                    </div>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    <div class="form-check">
                      <input type="checkbox" class="form-check-input shadow-none" id="category-6">
                      <label class="form-check-label" for="category-6">Other</label>
                    </div>
                  </div>
                  <div class="divider mt-5 mb-5 border-bottom border-secondary"></div>
                  <h6 class="text-uppercase mt-5 mb-3 font-weight-bold">Price</h6>
                  <div class="price-filter-control">
                    <input type="number" class="form-control w-50 pull-left mb-2 shadow-none" value="50" id="price-min-control">
                    <input type="number" class="form-control w-50 pull-right shadow-none" value="150" id="price-max-control">
                  </div>
                  <input id="ex2" type="text" class="slider " value="50,150" data-slider-min="10" data-slider-max="200" data-slider-step="5" data-slider-value="[50,150]" data-value="50,150" style="display: none;">
                  <div class="divider mt-5 mb-5 border-bottom border-secondary"></div>
                  <a href="#" class="btn btn-lg btn-block btn-primary mt-5 custom-button">Update Results</a>
                </div>

              </div>
            </div>

</template>

<script>
import ButtonComponent from './Buttons&Widgets/AddButtonShop.vue'
import FavoriteComponent from './Buttons&Widgets/AddFavoriteShop.vue'
export default{
    name: 'ViewShopPage',
    components: {
        ButtonComponent,
        FavoriteComponent,
        
    },
    data(){
      return{
      cartItems: [],
      }
    },

    computed: {
      itemCount() {
      if (!this.cartItems) {
        return 0;
      }
        return this.cartItems.length;
      }
    }

}

</script>

<style >


.container {
  background: #f3f3f3;
  
}


.btn.btn-primary.custom-button{
    background-color: #72b264;
    color: white;
    border: none;
}

.btn.btn-lg.custom-button-cart{
  background-color: rgb(255, 255, 255);
}



</style>