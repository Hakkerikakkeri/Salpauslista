<template>
  <div class="container">
    <h1 class="title">Tutkinnon suorittaneiden sijoittuminen</h1>
    <div v-if="jsonData" class="data-container">
      <div class="excel-table">
        <div class="excel-row header-row">
          <div class="excel-cell" v-for="(header, index) in headers" :key="index">{{ header }}</div>
        </div>

        <template v-for="(rowData, rowIndex) in jsonData['Kohde 1']" :key="rowIndex">
          <div class="excel-row" v-if="rowIndex !== 0">
            <div class="excel-cell" v-for="(value, key) in rowData" :key="key">
              {{ value === '1-4' ? 2 : value }}
            </div>
          </div>
          <div v-if="openYears[rowIndex] && rowIndex !== 0" class="extra-data">
          </div>
        </template>
      </div>
    </div>
    <p v-else>No data available</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import jsonData from '../data/tilastovuosi2.json';

const headers = Object.values(jsonData['Kohde 1'][0]);

const openYears = ref(Array(jsonData['Kohde 1'].length).fill(false));


</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  color: black;
}

.data-container {
  border: 1px solid #ccc;
  border-radius: 5px;
  overflow: auto;
}

.excel-table {
  display: table;
  width: 100%;
  border-collapse: collapse;
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

.toggle-cell {
  display: table-cell;
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
