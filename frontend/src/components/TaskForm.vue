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
      <div class="form-group mt-2">
        <label>Priority</label>
        <select v-model="priority" class="form-control">
          <option value="">-- Auto (AI) --</option>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>
      <button @click="predictPriority" type="button" class="btn btn-warning btn-sm mt-1">
        Let AI decide
      </button>
      <br/>
      <div v-if="lastPriority" class="alert alert-info p-1 mt-1">
        Suggestion: <strong>{{ lastPriority }}</strong>
      </div>
      <button type="submit" class="btn btn-primary btn-sm">Add Task</button>
      <p v-if="lastPriority" class="mt-2 text-info">
        AI suggested priority: <strong>{{ lastPriority }}</strong>
      </p>
    </form>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  props:["projectId"],
  data(){ return { title:"", description:"", status:"todo", lastPriority: null, priority: "" }; },
  methods: {
  async predictPriority() {
    if (!this.description) return;
    try {
      const res = await api.post("/predict-priority/", {
        description: this.description
      });
      this.priority = res.data.priority;
      this.lastPriority = this.priority;
      this.$emit("notify", {
        type: "info",
        message: `🧠 IA suggère : ${this.priority.toUpperCase()}`
      });
    } catch (err) {
      console.error(err);
      this.$emit("notify", {
        type: "error",
        message: "⚠️ Erreur IA"
      });
    }
  },
  async submitTask() {
    const payload = {
      title: this.title,
      description: this.description,
      status: this.status,
      project: this.projectId,
      priority: this.priority || null
    };
    try {
      await api.post("/tasks/", payload);
      this.title = "";
      this.description = "";
      this.status = "todo";
      this.priority = "";
      this.$emit("task-added");
      this.$emit("notify", { type: "success", message: "Task ajoutée ✔️" });
    } catch (error) {
      this.$emit("notify", { type: "error", message: "Erreur ajout task" });
    }
  }
}
};
</script>
