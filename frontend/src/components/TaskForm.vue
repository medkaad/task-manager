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
      <button type="submit" class="btn btn-primary btn-sm">Add Task</button>
    </form>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  props:["projectId"],
  data(){ return { title:"", description:"", status:"todo" }; },
  methods:{
    submitTask(){
      api.post("tasks/",{
        title:this.title,
        description:this.description,
        status:this.status,
        project:this.projectId
      }).then(()=>{
        this.title=""; this.description=""; this.status="todo";
        this.$emit("task-added");
      });
    }
  }
};
</script>
