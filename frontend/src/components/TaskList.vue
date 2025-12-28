<template>
  <ul class="list-group mb-2">
    <li v-for="task in tasks" :key="task.id" class="list-group-item d-flex justify-content-between">
      <div>
        <strong>{{ task.title }}</strong> - {{ task.status }}
        <span
          class="badge ms-2"
          :class="{
           'bg-danger': task.priority === 'high',
            'bg-warning': task.priority === 'medium',
           'bg-success': task.priority === 'low'
          }">
          {{ task.priority }}
        </span>
      </div>
      <div>
        <button class="btn btn-sm btn-warning me-1" @click="editTask(task)">Edit</button>
        <button class="btn btn-sm btn-danger" @click="deleteTask(task.id)">Delete</button>
      </div>
    </li>
    <div v-if="editingTask" class="card card-body mb-2">
      <input v-model="editingTask.title" class="form-control mb-1"/>
      <textarea v-model="editingTask.description" class="form-control mb-1"></textarea>
      <select v-model="editingTask.status" class="form-control mb-1">
        <option value="todo">To do</option>
        <option value="doing">Doing</option>
        <option value="done">Done</option>
      </select>
      <button class="btn btn-success btn-sm" @click="updateTask">Save</button>
      <button class="btn btn-secondary btn-sm" @click="editingTask=null">Cancel</button>
    </div>
  </ul>
</template>

<script>
import api from "../services/api";

export default {
  props: ["projectId"],
  data() { return { tasks: [], editingTask: null }; },
  methods: {
    fetchTasks() { 
      if(!this.projectId) return;
      api.get(`tasks/?project=${this.projectId}`).then(res => this.tasks = res.data); 
    },
    editTask(task) { this.editingTask = { ...task }; },
    updateTask() {
      api.put(`tasks/${this.editingTask.id}/`, this.editingTask).then(() => {
        this.editingTask=null; this.fetchTasks();
      });
    },
    deleteTask(taskId){
      if(!confirm("Delete this task?")) return;
      api.delete(`tasks/${taskId}/`).then(()=>this.fetchTasks());
    }
  },
  watch:{ projectId(){ this.fetchTasks(); }},
  mounted(){ this.fetchTasks(); }
};
</script>
