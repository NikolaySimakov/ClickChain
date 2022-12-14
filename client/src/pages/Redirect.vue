<script setup>
import { useRoute } from "vue-router";
import { ref, computed, onMounted } from "vue";
import { useStore } from "vuex";

const store = useStore();
const route = useRoute();

const path = computed(() => route.path);

const linkNotFound = ref(false);

onMounted(async () => {
  const token = path.value.slice(1);

  store
    .dispatch("getLongLink", token)
    .then(() => {
      window.location.href = store.getters.longLink;
    })
    .catch(() => {
      linkNotFound.value = true;
    });
});
</script>

<template>
  <div class="grid h-screen place-items-center">
    <div v-if="linkNotFound" class="flex items-center">
      <div class="text-5xl font-bold text-red-500">404</div>
      <div class="mx-4 text-6xl">|</div>
      <div class="text-3xl">link is inactive</div>
    </div>
    <div v-else>
      <div class="lds-ellipsis">
        <div></div>
        <div></div>
        <div></div>
        <div></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.lds-ellipsis {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}

.lds-ellipsis div {
  position: absolute;
  top: 33px;
  width: 13px;
  height: 13px;
  border-radius: 50%;
  background: #55497124;
  animation-timing-function: cubic-bezier(0, 1, 1, 0);
}

.lds-ellipsis div:nth-child(1) {
  left: 8px;
  animation: lds-ellipsis1 0.6s infinite;
}

.lds-ellipsis div:nth-child(2) {
  left: 8px;
  animation: lds-ellipsis2 0.6s infinite;
}

.lds-ellipsis div:nth-child(3) {
  left: 32px;
  animation: lds-ellipsis2 0.6s infinite;
}

.lds-ellipsis div:nth-child(4) {
  left: 56px;
  animation: lds-ellipsis3 0.6s infinite;
}

@keyframes lds-ellipsis1 {
  0% {
    transform: scale(0);
  }

  100% {
    transform: scale(1);
  }
}

@keyframes lds-ellipsis3 {
  0% {
    transform: scale(1);
  }

  100% {
    transform: scale(0);
  }
}

@keyframes lds-ellipsis2 {
  0% {
    transform: translate(0, 0);
  }

  100% {
    transform: translate(24px, 0);
  }
}
</style>
