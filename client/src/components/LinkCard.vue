<script setup>
import { ref, computed, onMounted } from "vue";
import { CONFIG } from "../config";
import QRCode from "qrcode";

const qrcode = ref(null);

const props = defineProps({
  token: String,
  longLink: String,
  date: String,
  clicks: Number,
});

const shortLink = computed(() => {
  return CONFIG.DOMAIN + props.token;
});

const dateFormatter = (d) => {
  const date = new Date(d);
  const formattedDate = date.toLocaleDateString("en-US", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
  return formattedDate;
};

function generateQRCode() {
  QRCode.toCanvas(qrcode.value, shortLink.value);
}

onMounted(() => {
  generateQRCode();
});
</script>

<template>
  <div
    class="border-4 border-black bg-white w-full my-4 md:transition md:duration-500 md:hover:scale-105 p-4 overflow-hidden"
  >
    <router-link :to="'/' + token + '/detail'">
      <div class="flex items-center justify-center">
        <div class="flex-1 max-h-full">
          <canvas ref="qrcode"></canvas>
        </div>
        <div class="flex-initial w-96 mx-4">
          <div class="font-bold">{{ shortLink }}</div>
          <div class="my-3 text-gray-400">{{ props.longLink }}</div>
          <div class="text-gray-400">{{ dateFormatter(props.date) }}</div>
        </div>
        <div class="flex-initial w-32 relative">
          <div class="absolute right-0 bottom-0">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="w-6 h-6 inline"
            >
              <path
                d="M18.375 2.25c-1.035 0-1.875.84-1.875 1.875v15.75c0 1.035.84 1.875 1.875 1.875h.75c1.035 0 1.875-.84 1.875-1.875V4.125c0-1.036-.84-1.875-1.875-1.875h-.75zM9.75 8.625c0-1.036.84-1.875 1.875-1.875h.75c1.036 0 1.875.84 1.875 1.875v11.25c0 1.035-.84 1.875-1.875 1.875h-.75a1.875 1.875 0 01-1.875-1.875V8.625zM3 13.125c0-1.036.84-1.875 1.875-1.875h.75c1.036 0 1.875.84 1.875 1.875v6.75c0 1.035-.84 1.875-1.875 1.875h-.75A1.875 1.875 0 013 19.875v-6.75z"
              />
            </svg>
            <span class="inline-block align-baseline font-bold ml-1">
              {{ props.clicks }}
            </span>
          </div>
        </div>
      </div>
    </router-link>
  </div>
</template>
