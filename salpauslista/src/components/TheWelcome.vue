<template>
  <div class="container">
    <h1 class="title">Tutkinnon suorittaneiden sijoittuminen</h1>
    <div class="years-container">
      <div class="year" v-for="year in validYears" :key="year" @click="showAlaData(year)">
        {{ year }}
      </div>
    </div>
    <div v-if="filteredAlaEntries.length > 0" class="data-container">
      <div class="excel-table">
        <div class="excel-row header-row">
          <div class="excel-cell" v-for="(header, index) in headers" :key="index">{{ header }}</div>
        </div>

        <template v-for="(yearData, yearIndex) in filteredAlaEntries" :key="yearIndex">
          <template v-for="(rowData, rowIndex) in yearData" :key="rowIndex">
            <div class="excel-row">
              <div class="excel-cell" v-for="(value, key) in rowData" :key="key">
                {{ value === '1-4' ? 2 : value }}
              </div>
            </div>
          </template>
        </template>
      </div>
    </div>
    <p v-else>No data available</p>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import jsonData from '../data/tilastovuosi2.json';

const headers = Object.values(jsonData['Kohde 1'][0]);

const validYears = Array.from({ length: 13 }, (_, index) => (2009 + index).toString());

const selectedYear = ref<string|null>(null);

const filteredAlaEntries = computed(() => {
  if (selectedYear.value) {
    const data = jsonData['Kohde 1'];
    const filteredData = [];
    let foundSelectedYear = false;
    let yearData = [];

    for (const row of data) {
      if (row['vuosiluku'] === selectedYear.value) {
        foundSelectedYear = true;
      } else if (foundSelectedYear) {
        if (row['vuosiluku']) {
          filteredData.push(yearData);
          yearData = [];
          break;
        }
        yearData.push(row);
      }
    }

    if (yearData.length > 0) {
      filteredData.push(yearData);
    }

    return filteredData;
  } else {
    return [];
  }
});

function showAlaData(year: string) {
  selectedYear.value = year;
}
</script>

<style scoped>

.years-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
}

.year {
  cursor: pointer;
  padding: 5px 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin: 5px; /* Add margin for better spacing */
}

.year:hover {
  background-color: #f0f0f0;
}
</style>
