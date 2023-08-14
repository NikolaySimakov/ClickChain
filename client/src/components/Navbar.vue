<script setup></script>

<template>
  <nav class="fixed w-full z-20 top-0 left-0 bg-white border-b border-gray-200">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <router-link to="/" class="flex items-center font-bold text-2xl">
        <img src="/logo.png" alt="logo" width="44" />
        <div class="ml-3">Link Shortener</div>
      </router-link>
      <div class="flex md:order-2">
        <router-link
          to="/signin"
          class="group relative font-bold border-4 border-black text-black bg-white font-medium text-lg px-4 py-2 text-center mr-2"
        >
          <div
            class="absolute inset-0 w-0 bg-purple-500 transition-all duration-[250ms] ease-out group-hover:w-full"
          ></div>
          <span class="relative text-black group-hover:text-white">Sign In</span>
        </router-link>
        <router-link
          to="/signup"
          class="group relative font-bold border-4 border-black text-black bg-white font-medium text-lg px-4 py-2 text-center mr-2"
        >
          <div
            class="absolute inset-0 w-0 bg-purple-500 transition-all duration-[250ms] ease-out group-hover:w-full"
          ></div>
          <span class="relative text-black group-hover:text-white">Sign Up</span>
        </router-link>
      </div>
    </div>
  </nav>
</template>
