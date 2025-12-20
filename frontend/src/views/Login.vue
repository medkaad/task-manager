<template>
  <div>
    <h2>Login</h2>

    <form @submit.prevent="login">
      <input
        v-model="username"
        placeholder="Username"
        required
      />

      <input
        type="password"
        v-model="password"
        placeholder="Password"
        required
      />

      <button type="submit">Login</button>
    </form>

    <p v-if="error" style="color:red">{{ error }}</p>
  </div>
</template>

<script>
import api, { setAuthToken } from "../services/api"

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      error: null,
    }
  },
  methods: {
    login() {
      this.error = null

      api.post("token/", {
        username: this.username,
        password: this.password,
      })
      .then(res => {
        const token = res.data.access
        localStorage.setItem("access_token", token)
        setAuthToken(token)
        this.$emit("login-success")
      })
      .catch(() => {
        this.error = "Invalid username or password"
      })
    }
  }
}
</script>
