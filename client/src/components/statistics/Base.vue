<template>
  <div class="border-4 border-black w-fit p-4 mt-20">
    <div class="my-2">
      <p class="font-medium">Total Clicks</p>
      <h3 class="font-bold text-4xl">{{ props.totalClicks }}</h3>
    </div>
    <div class="my-2">
      <p class="font-medium">Average Per Day</p>
      <h3 class="font-bold text-4xl">{{ props.averagePerDay }}</h3>
    </div>
    <div class="my-2">
      <p class="font-medium">Unique Clicks</p>
      <h3 class="font-bold text-4xl">{{ props.uniqueClicks }}</h3>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  totalClicks: Number,
  averagePerDay: Number,
  uniqueClicks: Number,
});
</script>
