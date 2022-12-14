<script setup>
import { ref } from "vue";
import useLinkForm from "../composable/forms/useLinkForm";

const longLink = ref("");
const linkForm = useLinkForm(longLink);
</script>

<template>
  <div class="w-2/3 xl:w-1/2 mx-auto flex">
    <input
      name="long-link-input"
      id="long-link-input"
      type="url"
      placeholder="Type long link"
      class="flex-1 border-4 border-black py-4 bg-white pl-4 pr-6 outline-0 w-full"
      :class="linkForm.inputStyle.value"
      v-model="longLink"
      @keyup.enter="linkForm.buttonSettings.onClick"
      required
    />
    <button
      class="flex-none py-4 px-9 font-bold border-4 border-black -ml-4"
      :class="linkForm.buttonSettings.style"
      :disabled="!linkForm.buttonSettings.onClick"
      @click="linkForm.buttonSettings.onClick"
    >
      {{ linkForm.buttonSettings.message }}
    </button>
  </div>
</template>
