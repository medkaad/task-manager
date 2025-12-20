<template>
  <form @submit.prevent="login">
    <input v-model="username" placeholder="Username" required />
    <input type="password" v-model="password" placeholder="Password" required />
    <button type="submit">Login</button>
  </form>
</template>

<script>
import axios from 'axios'
import { setToken } from '../services/api'

export default {
  data() {
    return { username: '', password: '' }
  },
  methods: {
    login() {
      axios.post('http://localhost:8000/api/token/', {
        username: this.username,
        password: this.password
      })
      .then(res => {
        setToken(res.data.access)
        localStorage.setItem('access_token', res.data.access)
      })
      .catch(err => console.error(err))
    }
  }
}
</script>
