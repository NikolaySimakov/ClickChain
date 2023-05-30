<script setup></script>

<template>
  <nav class="fixed w-full z-20 top-0 left-0">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <router-link to="/" class="flex items-center font-bold text-2xl">
        <img src="public/logo.png" alt="logo" width="44" />
        <div class="ml-3">l1nk</div>
      </router-link>
      <div class="flex md:order-2">
        <button
          type="button"
          class="font-bold border-4 border-black text-black bg-white font-medium text-lg px-4 py-2 text-center mr-2"
        >
          Sign In
        </button>
        <button
          type="button"
          class="font-bold border-4 border-black text-black bg-white hover:bg-emerald-300 hover:text-white font-medium text-lg px-4 py-2 text-center mr-3 ml-2"
        >
          Login
        </button>
      </div>
    </div>
  </nav>
</template>
