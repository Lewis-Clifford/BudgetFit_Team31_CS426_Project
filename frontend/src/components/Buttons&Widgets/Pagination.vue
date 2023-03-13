<template>
    <nav>
      <ul class="pagination">
        <li v-if="currentPage > 1" class="page-item">
          <a class="page-link" href="#" @click.prevent="prevPage">Previous</a>
        </li>
        <li v-for="pageNumber in pages" :key="pageNumber" :class="['page-item', { active: pageNumber === currentPage }]">
          <a class="page-link" href="#" @click.prevent="changePage(pageNumber)">{{ pageNumber }}</a>
        </li>
        <li v-if="currentPage < totalPages" class="page-item">
          <a class="page-link" href="#" @click.prevent="nextPage">Next</a>
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    props: {
      currentPage: {
        type: Number,
        required: true
      },
      totalPages: {
        type: Number,
        required: true
      }
    },
    computed: {
      pages() {
        const pages = [];
        for (let i = 1; i <= this.totalPages; i++) {
          pages.push(i);
        }
        return pages;
      }
    },
    methods: {
      changePage(pageNumber) {
        this.$emit("page-changed", pageNumber);
      },
      prevPage() {
        this.changePage(this.currentPage - 1);
      },
      nextPage() {
        this.changePage(this.currentPage + 1);
      }
    }
  };
  </script>