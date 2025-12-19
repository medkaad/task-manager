<template>
  <div>
    <h1>Task Manager</h1>
    <ProjectList />
  </div>
</template>

<script>
import ProjectList from './components/ProjectList.vue'

export default {
  components: { ProjectList }
}
</script>