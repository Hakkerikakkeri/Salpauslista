<script setup lang="ts">
import { ref, onMounted } from 'vue';

const data = ref(null);

onMounted(async () => {
  try {
    const response = await fetch('https://api.allorigins.win/get?url=' + encodeURIComponent('http://api.vipunen.fi/api/resources/julkaisut'));
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    const responseData = await response.json();
    data.value = JSON.parse(responseData.contents);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});
</script>

<template>
  <div>
    <h1 class="title">Data fetched:</h1>
    <pre class="data">{{ data }}</pre>
  </div>
</template>