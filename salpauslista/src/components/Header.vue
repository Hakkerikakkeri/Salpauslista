<script setup lang="ts">
import { ref, onMounted } from 'vue';

const isSticky = ref(false);

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

const handleScroll = () => {
  if (window.pageYOffset > 0) {
    isSticky.value = true;
  } else {
    isSticky.value = false;
  }
};
</script>

<template>
  <div :class="{ 'header': true, 'sticky': isSticky }">
    <img class="logo" src="https://kuljettajaopetus.fi/dokumentit/asiakkaat/salpaus/kuvat/logo_iso.png">
    <input class="searchbar" placeholder="Hae kentästä">
    <button class="excel-button">Lataa excelinä</button>
  </div>
</template>