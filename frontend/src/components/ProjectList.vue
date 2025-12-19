<template>
  <div>
    <h2>Projects</h2>
    <ul>
      <li v-for="project in projects" :key="project.id">{{ project.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProjectList',
  data() {
    return {
      projects: []
    }
  },
  mounted() {
    axios.get('http://localhost:8000/api/projects/')
      .then(res => this.projects = res.data)
      .catch(err => console.error(err))
  }
}
</script>