<template>
  <button class="btn btn-danger btn-sm" @click="logout">Logout</button>
</template>

<script>
export default {
  methods: {
    logout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      this.$router.push("/login");
    },
  },
};
</script>
