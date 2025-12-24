<template>
  <div class="container mt-5">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" class="form-control mb-2" />
      <input v-model="password" type="password" placeholder="Password" class="form-control mb-2" />
      <button class="btn btn-primary">Login</button>
      <p class="text-danger mt-2">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  data() {
    return { username: "", password: "", error: null };
  },
  methods: {
    async login() {
      try {
        const res = await api.post("token/", { username: this.username, password: this.password });
        localStorage.setItem("access_token", res.data.access);
        localStorage.setItem("refresh_token", res.data.refresh);
        this.$router.push("/");
      } catch {
        this.error = "Invalid credentials";
      }
    },
  },
};
</script>
