<template>
    <div class="min-h-screen bg-gray-900 text-white p-4">
      <div class="max-w-3xl mx-auto">
        <!-- Title -->
        <h1 class="text-2xl font-bold mb-6">Search Results</h1>
  
        <!-- Search Box -->
        <div class="flex items-center bg-gray-800 p-4 rounded-lg shadow-md">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search..."
            class="flex-grow bg-transparent text-white outline-none px-2"
          />
        </div>
  
        <!-- Results -->
        <div v-if="filteredResults.length" class="mt-6 space-y-4">
          <div
            v-for="(result, index) in filteredResults"
            :key="index"
            class="p-4 bg-gray-800 rounded-lg shadow">
            <h2 class="text-lg font-semibold">{{ result.title }}</h2>
            <p class="text-gray-400">{{ result.description }}</p>
          </div>
        </div>
  
        <!-- No Results -->
        <div v-else class="mt-6 text-center text-gray-500">
          No results found.
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: "", // Bind input value
        results: [
         
        ],
      };
    },
    computed: {
      // Dynamically filter results based on the search query
      filteredResults() {
        const query = this.searchQuery.toLowerCase();
        return this.results.filter(
          (item) =>
            item.title.toLowerCase().includes(query) ||
            item.description.toLowerCase().includes(query)
        );
      },
    },
  };
  </script>
  
  <style>
  @import "tailwindcss/tailwind.css";
  </style>
  