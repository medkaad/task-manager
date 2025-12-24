<template>
  <div>
    <h1 class="h3 mb-3">Project Tasks</h1>

    <TaskForm :projectId="id" @task-added="refresh" />
    <TaskList ref="taskList" :projectId="id" />
  </div>
</template>

<script>
import TaskForm from "../components/TaskForm.vue";
import TaskList from "../components/TaskList.vue";

export default {
  props: ["id"],
  components: { TaskForm, TaskList },
  methods: {
    refresh() {
      this.$refs.taskList.fetchTasks();
    }
  }
};
</script>
