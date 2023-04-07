
<template>
<div class="container p-5" >
              <div class="row">
                <div class="col-md-8 order-md-2 col-lg-9">
                  <div class="container-fluid">
                    <div class="row mb-5">
                      <div class="col-12">
                        <div class="dropdown text-md-start text-center float-md-start mb-3 mt-3 mt-md-0 mb-md-0">
                          <label class="me-2">Sort by:</label>
                          <button class="btn btn-lg btn-light dropdown-toggle hvr-shrink"  id="dropdownMenuButton1" data-bs-toggle="dropdown" type="button" aria-expanded="false" :value="selectedSort">{{ selectedSort }}</button>

                          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                            <a v-if="selectedSort !== 'Default'" class="dropdown-item" @click="setSort('def')">Default</a>
                            <a v-if="selectedSort !== 'Price Descending'" class="dropdown-item" @click="setSort('price_dec')">Price Descending</a>
                            <a v-if="selectedSort !== 'Price Ascending'" class="dropdown-item" @click="setSort('price_asc')">Price Ascending</a>
                          </div>
                        </div>
                        
                        <div class="btn-group float-md-end ms-3">
                          <button :disabled="page === 1" @click="setView(selectedView, page - 1)" type="button" class="btn btn-lg btn-light hvr-shrink"> <font-awesome-icon icon="fa-solid fa-arrow-left" /> </button>
                          <button :disabled="page === total" @click="setView(selectedView, page + 1)" type="button" class="btn btn-lg btn-light hvr-shrink"> <font-awesome-icon icon="fa-solid fa-arrow-right" /> </button>
                        </div>
                        <div class="float-md-end">
                          <label class="ms-4 mt-3">Page {{ page }} of {{ total }}</label>
                        </div>
                        
                        <div class="dropdown float-end">
                          <router-link to="/cart" >
                          <button type="button" class="btn btn-lg hvr-shrink me-4 btn-light">
                            <font-awesome-icon icon="fa-solid fa-shopping-cart"></font-awesome-icon>

                            <span class="badge bg-primary rounded-pill">{{ totalItems }}</span>
                          </button>
                          
                        </router-link>
                        <label class="me-2">View:</label>
                        <button class="btn btn-lg btn-light dropdown-toggle hvr-shrink" data-bs-toggle="dropdown" id="dropdownMenuButton2" type="button"  aria-expanded="false" :value="selectedView">{{ selectedView }}</button>
                        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown" x-placement="bottom-end" style="will-change: transform; position: absolute; transform: translate3d(120px, 48px, 0px); top: 0px; left: 0px;">
                            <a class="dropdown-item" @click="setView(9)" v-if="selectedView !== 9">9</a>
                            <a class="dropdown-item" @click="setView(18)" v-if="selectedView !== 18 && selectedView !== 'default'">18</a>
                            <a class="dropdown-item" @click="setView(27)" v-if="selectedView !== 27 && selectedView !== 'default'">27</a>
                            <a class="dropdown-item" @click="setView(36)" v-if="selectedView !== 36 && selectedView !== 'default'">36</a>
                            <a class="dropdown-item" @click="setView(45)" v-if="selectedView !== 45 && selectedView !== 'default'">45</a>
                        </div>

                        </div>
                        
                      </div>
                    </div>
                    <div class="row">
                      <Products :cartItems="cartItems" :list="list"/>
                    </div>
                    <div class="row mb-5 mt-5">
                      <div class="col-12">
                        <a class="btn btn-light hvr-shrink" @click="scrollToTop">
                          <font-awesome-icon icon="fa-solid fa-arrow-up me-2"></font-awesome-icon> Back to top</a>
                          <div class="btn-group float-md-end ms-3">
                          <button :disabled="page === 1" @click="setView(selectedView, page - 1)" type="button" class="btn btn-lg btn-light hvr-shrink"> <font-awesome-icon icon="fa-solid fa-arrow-left" /> </button>
                          <button :disabled="page === total" @click="setView(selectedView, page + 1)" type="button" class="btn btn-lg btn-light hvr-shrink"> <font-awesome-icon icon="fa-solid fa-arrow-right" /> </button>
                        </div>
                        <div class="float-md-end">
                          <label class="mt-3">Page {{ page }} of {{ total }}</label>
                        </div>
                      </div>
                    </div>
                  </div>
                </div><div class="col-md-4 order-md-1 col-lg-3 sidebar-filter">
                  <div class="input-group">
                    <input class="form-control shadow-none" type="text" placeholder="Search" aria-label="Search" v-model="search" @keyup.enter="searchProducts">
                    <button type="button" class="btn btn-primary custom-button" @click="searchProducts"><font-awesome-icon icon="fa-solid fa-magnifying-glass"/></button>
                  </div>
                    <div>
                      
                    </div>
                    <br>
                    <h6 class="text-uppercase font-weight-bold mb-3">Categories</h6>
                    <div v-for="category in ['Breads', 'Condiments', 'Dairy', 'Drinks', 'Frozen Foods', 'Meats', 'Snacks', 'Vegetables', 'Other']" :key="category">
                      <div class="mt-2 mb-2 pl-2">
                        <div class="form-check">
                          <input type="checkbox" class="form-check-input shadow-none" :id="'category-' + category" @click="toggleCategory(category)">
                          <label class="form-check-label" :for="'category-' + category">{{ category }}</label>
                        </div>
                      </div>
                    </div>
                    <button class="btn btn-lg btn-block btn-primary mt-3 custom-button" @click="applyFilters">Apply Filters</button>
                  
                  <div class="divider mt-5 mb-5 border-bottom border-secondary"></div>
                  <h6 class="text-uppercase mt-5 mb-3 font-weight-bold">Price</h6>
                  <div class="price-filter-control">
                    <input type="number" class="form-control w-50 pull-left mb-2 shadow-none" placeholder="Min" v-model="min" id="price-min-control">
                    <input type="number" class="form-control w-50 pull-right shadow-none" placeholder="Max" v-model="max" id="price-max-control">
                    <button class="btn btn-lg btn-block btn-primary mt-4 custom-button" @click="updateResults">Update Results</button>
                  </div>
                  <div class="divider mt-5 mb-5 border-bottom border-secondary"></div>
                   <p>Current List & Others:</p>
                   <div class="mt-2 mb-2 pl-2">
                   <a href="#" class="list">List1</a> (Current)
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                   <a href="#" class="list">List2</a>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                   <a href="#" class="list">List3</a>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                   <a href="#" class="list">List4</a>
                  </div>
                  <div class="mt-2 mb-2 pl-2">
                    
                    <a href="#" class="btn btn-md btn-block btn-primary custom-button">Create New List</a>
                  </div>
            
                </div>

              </div>
            </div>
          
</template>

<script>
import Products from './Buttons&Widgets/Products.vue'
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  name: 'ViewShopPage',
  created() {
    this.$store.commit('initializeCartFromStorage');
    this.fetchProducts();
    this.setView(9);
  },
  components: {
    Products,
  },
  data() {
    return {
      cartItems: [],
      selectedView: '9',
      selectedSort: 'Default',
      selectedCategories: [],
      products: [],
      list: [],
      sort: 'def',
      min: 0,
      max: 500,
      search: ''
    }
  },
  computed: {
    ...mapGetters(['totalItems']),
    items() {
      const start = (this.page - 1) * this.selectedView;
      const end = start + this.selectedView;
      return this.list.slice(start, end);
    },
  },
  methods: {
    scrollToTop() {
      const rootElement = document.documentElement;
      const scrollDuration = 250; // milliseconds
      const scrollStep = -rootElement.scrollTop / (scrollDuration / 15);

      rootElement.style.scrollBehavior = "smooth";
      rootElement.style.transition = `scrollTop ${scrollDuration}ms linear`;
      rootElement.scrollTop = 0;

      setTimeout(() => {
        rootElement.style.scrollBehavior = "";
        rootElement.style.transition = "";
      }, scrollDuration);
    },
    setView(viewnum, page = 1, sortOrder) {
      var temp = {query:{page:page, limit:viewnum, sort:sortOrder}};
      this.selectedView = viewnum;
      this.$router.push(temp);
      this.fetchProducts(viewnum, page, sortOrder);
    },
    setSort(sortType) {
      if (sortType == 'def') {
        this.selectedSort = 'Default';
        this.fetchProducts(this.selectedView, 1, 'def');
      } else if (sortType == 'price_dec'){
        this.selectedSort = 'Price Descending';
        this.fetchProducts(this.selectedView, 1, 'desc');
      } else if (sortType == 'price_asc'){
        this.selectedSort = 'Price Ascending';
        this.fetchProducts(this.selectedView, 1, 'asc');
      }
    },
    fetchProducts(limit = this.selectedView, page = 1, sort = this.sort, categories = this.selectedCategories.join(','), search = this.search) {
      axios.get(`http://localhost:5000/products?page=${page}&limit=${limit}&sort=${sort}&min=${this.min}&max=${this.max}&categories=${categories}&search=${search}`)
        .then(response => {
          this.list = response.data.data;
          this.total = response.data.totalPages;
          this.page = page;
           this.sort = sort;
    })
    .catch(error => {
      console.log(error);
    });
},
    updateResults() {
      this.fetchProducts(this.selectedView, 1, this.sort, this.selectedCategories.join(","), this.search);
    },
    applyFilters(){
      this.fetchProducts(this.selectedView, 1, this.sort, this.selectedCategories.join(","), this.search)
    },
    toggleCategory(category) {
  const index = this.selectedCategories.indexOf(category);
  if (index === -1) {
    this.selectedCategories.push(category);
  } else {
    this.selectedCategories.splice(index, 1);
  }
},
searchProducts(){
  this.fetchProducts(this.selectedView, 1, this.sort, this.selectedCategories.join(","), this.search);
}
  },
}
</script>
<style >

.list {
 color: black !important;
}

.card-img-top{
  height: 240px;
  position: relative;
}

.card{
   transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.card:hover {
  transform: translate(0, -6px);
  transition: all 0.2s ease-in-out;
}


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

.dropdown-menu a{
  cursor: pointer;
}



</style>