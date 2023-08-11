<script setup></script>

<template>
  <nav class="fixed w-full z-20 top-0 left-0 bg-white border-b border-gray-200">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <router-link to="/" class="flex items-center font-bold text-2xl">
        <img src="/logo.png" alt="logo" width="44" />
        <div class="ml-3">Link Shortener</div>
      </router-link>
      <div class="flex md:order-2">
        <button
          type="button"
          class="font-bold border-4 border-black text-black bg-white font-medium text-lg px-4 py-2 text-center mr-2"
          @click="$router.push('signin')"
        >
          Sign In
        </button>
        <button
          type="button"
          class="font-bold border-4 border-black text-black bg-white font-medium text-lg px-4 py-2 text-center mr-3 ml-2"
          @click="$router.push('login')"
        >
          Login
        </button>
      </div>
    </div>
  </nav>
</template>
