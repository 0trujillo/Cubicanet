
<template>
  <div class="main-bg">
    <nav class="main-nav">
      <router-link to="/" class="nav-link">Inicio</router-link>
      
      <router-link to="/tarja" class="nav-link">Tarja</router-link>
    </nav>
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
// Lógica global opcional
</script>

<style scoped>
.main-bg {
  min-height: 100vh;
  background: linear-gradient(90deg, rgb(33, 33, 161));
}
.main-nav {
  background: #fff;
  opacity: 0.95;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  padding: 1rem 2rem;
  display: flex;
  gap: 2rem;
  border-bottom: 1px solid #eee;
}
.nav-link {
  font-weight: bold;
  color: #6d28d9;
  text-decoration: none;
  padding: 0.2rem 0.7rem;
  border-radius: 4px;
  transition: background 0.2s, color 0.2s;
}
.nav-link:hover {
  background: #ede9fe;
  color: #db2777;
}
.main-content {
  padding: 2rem 1rem;
}
</style>

