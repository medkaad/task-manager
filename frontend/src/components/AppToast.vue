<template>
  <div
    v-if="visible"
    class="toast-container position-fixed top-0 end-0 p-3"
    style="z-index: 9999"
  >
    <div
      class="toast show text-white"
      :class="type === 'danger' ? 'bg-danger' : 'bg-success'"
    >
      <div class="d-flex">
        <div class="toast-body">
          {{ message }}
        </div>
        <button
          class="btn-close btn-close-white me-2 m-auto"
          @click="hide"
        ></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    message: String,
    type: {
      type: String,
      default: "success"
    }
  },
  data() {
    return {
      visible: true
    };
  },
  mounted() {
    setTimeout(this.hide, 3000);
  },
  methods: {
    hide() {
      this.visible = false;
      this.$emit("close");
    }
  }
};
</script>
