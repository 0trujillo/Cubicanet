<template>
  <div class="min-h-screen bg-gradient-to-r from-purple-800 via-pink-600 to-red-500">
    <nav class="bg-white bg-opacity-80 shadow p-4 flex gap-4">
      <router-link to="/" class="font-bold text-purple-700 hover:underline">Inicio</router-link>
      <router-link to="/empleados" class="font-bold text-pink-700 hover:underline">CRUD Empleados</router-link>
      <router-link to="/tarja" class="font-bold text-red-700 hover:underline">Tarja</router-link>
    </nav>
    <main class="p-6">
      <router-view />
    </main>
  </div>
</template>
