<template>
  <div class="container">
    <h1 class="title">Data:</h1>
    <div v-if="jsonData" class="data-container">
      <div class="excel-table">
        <div class="excel-row header-row">
          <div class="excel-cell" v-for="(header, index) in headers" :key="index">{{ header }}</div>
        </div>
        <template v-for="(rowData, index) in jsonData['Kohde 1'].slice(1)" :key="index">
          <div class="excel-row">
            <div class="excel-cell" v-for="(value, key) in rowData" :key="key">{{ value }}</div>
            <div class="excel-cell">
            </div>
          </div>
          <div v-if="openYears[index]" class="extra-data">
            <!-- Additional data for the opened year -->
          </div>
        </template>
      </div>
    </div>
    <p v-else>No data available</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import jsonData from '../data/tilastovuosi.json';

const headers = Object.values(jsonData['Kohde 1'][0]); // Extract headers from the first object

const openYears = ref(Array(jsonData['Kohde 1'].length - 1).fill(false));

function toggleYear(index) {
  openYears.value[index] = !openYears.value[index];
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
  overflow: auto;
}

.excel-table {
  display: table;
  

}

.excel-row {
  display: table-row;
}

.excel-cell {
  display: table-cell;
  padding: 8px;
}

.header-row {
  font-weight: bold;
  background-color: #f2f2f2;
}

.excel-cell:first-child {
  min-width: 100px; /* Adjust the width of the first column if needed */
}

.toggle-button {
  width: 20px;
  height: 20px;
  border: none;
  background-color: transparent;
  cursor: pointer;
}

.extra-data {
  padding-left: 30px; /* Adjust indentation for the extra data */
}
</style>
