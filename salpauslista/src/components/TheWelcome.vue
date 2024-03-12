<template>
  <div class="container">
    <h1 class="title">Data:</h1>
    <div v-if="jsonData" class="data-container">
      <div v-for="(yearData, year) in jsonData['Kohde 1']" :key="year">
        <div class="year-header" @click="toggleYear(year)">
          <span v-if="isYearOpen(year)">▼</span>
          <span v-else>►</span>
          <span>{{ yearData.vuosi}}</span>
        </div>
        <div v-if="isYearOpen(year)" class="data-list">
          <div v-for="(value, key) in yearData" :key="key" v-if="key !== 'text'">
            {{ key }}: {{ value }}
          </div>
        </div>
      </div>
    </div>
    <p v-else>No data available</p>
  </div>
</template>



<script setup lang="ts">
import { ref } from 'vue';
import jsonData from '../data/tilastovuosi.json';

const openYear = ref(null);

function toggleYear(year) {
  openYear.value = openYear.value === year ? null : year;
}

function isYearOpen(year) {
  return openYear.value === year;
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  color: black;
}

.title {
  font-size: 24px;
  margin-bottom: 10px;
}

.data-container {
  border: 1px solid #ccc;
  padding: 10px;
  overflow-x: auto;
}

.year-header {
  cursor: pointer;
  display: flex;
  align-items: center;
}

.data-list {
  margin-left: 20px;
}

.year-header span {
  margin-right: 5px;
}

.year-header:hover {
  background-color: #f2f2f2;
}
</style>
