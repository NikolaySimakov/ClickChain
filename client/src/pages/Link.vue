<script setup>
import LinkForm from "../components/LinkForm.vue";
import LinkCard from "../components/LinkCard.vue";
import Navbar from "../components/Navbar.vue";

import { ref, computed, onMounted } from "vue";
import { useLinkStore } from "../stores/links";

const store = useLinkStore();
const linksHistory = ref([]);

onMounted(async () => {
  store
    .getLinksHistory()
    .then(() => {
      linksHistory.value = store.getHistory;
    })
    .catch(() => {
      linksHistory.value = [];
    });
});
</script>

<template>
  <Navbar />
  <div class="grid h-screen place-items-center mt-28">
    <div class="text-purple-500 text-5xl font-bold">Create Short Links!</div>
    <div class="text-xl text-center my-8">
      <div>Web application for creating shortened links and collecting</div>
      <div>click-through statistics</div>
    </div>
    <LinkForm />
    <div class="w-2/3 xl:w-1/2 mx-auto mt-16" v-show="linksHistory.length !== 0">
      <div class="text-lg">Links history</div>
      <div v-for="link in linksHistory" :key="link">
        <LinkCard
          :token="link.token"
          :longLink="link.long_link"
          :date="link.activation_date"
          :clicks="link.clicks"
        />
      </div>
    </div>
  </div>
</template>
