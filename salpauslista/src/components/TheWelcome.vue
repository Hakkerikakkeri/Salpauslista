<template>
  <div class="container">
    <h1 class="title">Data:</h1>
    <div v-if="jsonData" class="data-container">
      <div class="excel-table">
        <div class="excel-row header-row">
          <div class="excel-cell" v-for="(header, index) in headers" :key="index">{{ header }}</div>
        </div>
        <template v-for="(rowData, index) in jsonData['Kohde 1']" :key="index">
          <div class="excel-row" :class="{ 'year-row': isYearRow(rowData) }">
            <div class="toggle-cell" v-if="isYearRow(rowData)">
              <button class="toggle-button" @click="toggleYear(index)">
                {{ openYears.includes(index) && '+ ' }}
              </button>
            </div>
            <div class="excel-cell" v-for="(value, key) in rowData" :key="key">{{ value }}</div>
          </div>
          <div v-if="openYears.includes(index) && !isYearRow(rowData) && index !== 0" class="extra-data">
            <div class="excel-row" v-for="(value, key) in extraData[index]" :key="key">
              <div class="excel-cell">{{ key }}</div>
              <div class="excel-cell">{{ value }}</div>
            </div>
          </div>
        </template>
      </div>
    </div>
    <p v-else>No data available</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import jsonData from '../data/tilastovuosi2.json';

const headers = Object.keys(jsonData['Kohde 1'][0]); // Extract headers from the first object

const openYears = ref([]);
const extraData = ref(Array(jsonData['Kohde 1'].length).fill({}));

function toggleYear(index) {
  if (!openYears.value.includes(index)) {
    openYears.value.push(index);
    // Populate extra data when opening
    extraData.value[index] = jsonData['Kohde 1'][index];
  } else {
    // Close the year if already open
    const yearIndex = openYears.value.indexOf(index);
    if (yearIndex !== -1) {
      openYears.value.splice(yearIndex, 1);
    }
  }
}

function isYearRow(rowData) {
  return rowData.hasOwnProperty('vuosiluku');
}

onMounted(() => {
  // Populate openYears with the indices of the year rows initially
  jsonData['Kohde 1'].forEach((rowData, index) => {
    if (isYearRow(rowData)) {
      openYears.value.push(index);
    }
  });
});
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

.year-row {
  font-weight: bold;
}
</style>
