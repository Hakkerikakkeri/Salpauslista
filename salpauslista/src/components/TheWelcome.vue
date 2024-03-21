<template>
  <div class="container">
    <h1 class="title">Tutkinnon suorittaneiden sijoittuminen</h1>
    <div v-if="jsonData" class="data-container">
      <div class="excel-table">
        <div class="excel-row header-row">
          <div class="excel-cell" v-for="(header, index) in headers" :key="index">{{ header }}</div>
        </div>

        <template v-for="(rowData, rowIndex) in jsonData['Kohde 1']" :key="rowIndex">
          <div class="excel-row" v-if="!rowData.hasOwnProperty('ala') && rowData.hasOwnProperty('vuosiluku')">
            <div class="excel-cell" v-for="(value, key) in rowData" :key="key">
              {{ value === '1-4' ? 2 : value }}
            </div>
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
