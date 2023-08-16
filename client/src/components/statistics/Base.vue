<template>
  <div class="border-4 border-black w-fit p-4 mt-20">
    <div class="my-2">
      <p class="font-medium">Total Clicks</p>
      <h3 class="font-bold text-4xl">{{ totalClicks }}</h3>
    </div>
    <div class="my-2">
      <p class="font-medium">Average Per Day</p>
      <h3 class="font-bold text-4xl">{{ averagePerDay }}</h3>
    </div>
    <div class="my-2">
      <p class="font-medium">Unique Clicks</p>
      <h3 class="font-bold text-4xl">{{ uniqueClicks }}</h3>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const totalClicks = ref(0);
const averagePerDay = ref(0);
const uniqueClicks = ref(0);
</script>
