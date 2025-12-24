<template>
  <router-view />

  <AppToast
    v-if="toast"
    :message="toast.message"
    :type="toast.type"
    @close="toast = null"
  />
</template>

<script>
import AppToast from "./components/AppToast.vue";

export default {
  name: "App",
  components: {
    AppToast
  },
  data() {
    return {
      toast: null
    };
  },
  methods: {
    showToast(message, type = "success") {
      this.toast = { message, type };
    }
  }
};
</script>
