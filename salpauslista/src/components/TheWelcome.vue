<template>
  <div class="container">
    <h1 class="title">Ammatillisen tutkinnon suorittaneiden työllistyminen ja jatko-opintoihin sijoittuminen</h1>
    <div v-if="formattedData" class="data-container">
      <div class="excel-table">
        <div class="excel-row header-row">
          <div class="excel-cell" v-for="(header, index) in headers" :key="index">{{ header }}</div>
        </div>
        <template v-for="(rowData, index) in formattedData" :key="index">
          <div v-if="index !== 0" class="excel-row"> <!-- Skip the first row -->
            <div class="excel-cell" v-for="(value, key) in rowData" :key="key">{{ value }}</div>
          </div>
          <div v-if="openYears[index - 1]" class="extra-data"> <!-- Adjust index for openYears -->
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

const formattedData = jsonData['Kohde 1'].map((row, index) => {
    if (index === 0) return row;
    const formattedRow = {};
    Object.entries(row).forEach(([key, value]) => {
        if (typeof value === "string" && value === "1-4") {
            value = "2";
        }
        formattedRow[key] = value;
    });
    return formattedRow;
});

const headers = Object.values(formattedData[0]);
const openYears = ref(Array(formattedData.length - 1).fill(false));
</script>

<style scoped>
.container {
  font-size: 13px;
  max-width: 800px;
  margin: auto;
  padding: 20px;
  color: black;
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
