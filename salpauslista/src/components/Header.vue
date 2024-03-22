<template>
  <div class="container">
    <div class="header">
      <img class="logo" src="https://kuljettajaopetus.fi/dokumentit/asiakkaat/salpaus/kuvat/logo_iso.png">
      <input class="searchbar" placeholder="Hae kentästä" v-model="searchQuery" @input="search">
      <button class="excel-button">Lataa excelinä</button>
    </div>

    <div v-if="showPopup" class="popup-container">
      <div class="popup">
        <ul>
          <li v-for="(item, index) in searchResults" :key="index">{{ item }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import jsonData from '../data/tilastovuosi2.json';

const searchQuery = ref('');
const searchResults = ref([]);
const showPopup = ref(false);

const search = () => {
  console.log('Search query:', searchQuery.value.trim());
  if (searchQuery.value.trim() === '') {
    showPopup.value = false;
    return;
  }
  const regex = new RegExp(searchQuery.value.trim(), 'i');
  console.log('Regex:', regex);

  const filteredRows = jsonData['Kohde 1'].filter(row => {
    return Object.values(row).some(value => regex.test(value));
  });
  console.log('Filtered rows:', filteredRows);
  searchResults.value = filteredRows.map(row => Object.values(row).join(', '));
  console.log('Search results:', searchResults.value);
  showPopup.value = true;
};
</script>

<style>
.header {
  display: flex;
  align-items: center;
}

.logo {
  width: 300px;
  height: auto;
}

.searchbar {
  width: 300px;
  height: 40px;
}

.popup-container {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  background-color: transparent;
}

.popup {
  background-color: #ffffff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
  max-height: 200px;
  min-width: 700px;
  max-width: 700px;
  overflow-y: auto;
}

.popup ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.popup li {
  margin-bottom: 8px;
}
</style>
