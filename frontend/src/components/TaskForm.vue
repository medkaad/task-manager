<template>
  <div class="card p-2 mb-3">
    <h5>Add Task</h5>
    <form @submit.prevent="submitTask">
      <input v-model="title" placeholder="Task title" class="form-control mb-1" required/>
      <textarea v-model="description" placeholder="Description" class="form-control mb-1"></textarea>

      <select v-model="status" class="form-control mb-1">
        <option value="todo">To do</option>
        <option value="doing">Doing</option>
        <option value="done">Done</option>
      </select>

      <!-- Priority input + AI suggestion -->
      <div class="input-group mt-2">
        <input v-model="priority" placeholder="Priority (AI optional)" class="form-control" />
        <button type="button" class="btn btn-warning" @click="predictPriority">
          🤖 Let AI decide
        </button>
      </div>

      <!-- IA suggestion -->
      <div v-if="lastPriority" class="alert alert-info p-1 mt-2">
        🧠 IA suggère : <strong>{{ lastPriority.toUpperCase() }}</strong>
      </div>

      <button type="submit" class="btn btn-primary btn-sm mt-2">Add Task</button>
    </form>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  props: ["projectId"],
  data() {
    return {
      title: "",
      description: "",
      status: "todo",
      priority: "",
      lastPriority: null,
    };
  },
  methods: {
    async predictPriority() {
      if (!this.description) return;

      try {
        const res = await api.post("predict-priority/", {
          description: this.description,
        });

        this.priority = res.data.priority;      // 🔥 met directement dans l’input
        this.lastPriority = res.data.priority;  // 🔥 affiche suggestion

        this.$emit("notify", {
          type: "info",
          message: `IA suggère : ${this.priority.toUpperCase()}`
        });

      } catch (err) {
        console.error(err);
        this.$emit("notify", { type: "error", message: "⚠️ Erreur IA" });
      }
    },

    async submitTask() {
      const payload = {
        title: this.title,
        description: this.description,
        status: this.status,
        priority: this.priority || null,
        project: this.projectId,
      };

      try {
        await api.post("tasks/", payload);

        // Reset
        this.title = "";
        this.description = "";
        this.priority = "";
        this.status = "todo";

        this.$emit("task-added");
        this.$emit("notify", { type: "success", message: "Task ajoutée ✔️" });

      } catch {
        this.$emit("notify", { type: "error", message: "Erreur ajout task" });
      }
    }
  }
};
</script>
