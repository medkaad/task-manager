<template>
  <div class="card mb-3">
  <div class="card-body">
    <h5 class="card-title">Create Project</h5>

    <form @submit.prevent="createProject">
      <div class="input-group">
        <input
          v-model="newProjectName"
          class="form-control"
          placeholder="Project name"
          required
        />
        <button class="btn btn-success">Add</button>
      </div>
    </form>
  </div>
</div>

  <div>
    <h1 class="h3 mb-3">Projects</h1>

    <ul class="list-group mb-3">
      <li
  v-for="project in projects"
  :key="project.id"
  class="list-group-item d-flex justify-content-between align-items-center"
>
  <span>{{ project.name }}</span>

  <div>
    <button
      class="btn btn-warning btn-sm me-2"
      @click="startEdit(project)"
    >
      Edit
    </button>

    <router-link
      class="btn btn-primary btn-sm me-2"
      :to="`/projects/${project.id}`"
    >
      View
    </router-link>

    <button
      class="btn btn-danger btn-sm"
      @click="deleteProject(project.id)"
    >
      Delete
    </button>
  </div>
</li>

    

    </ul>

    <!-- Edit Form -->
    <div v-if="editingProject" class="card card-body">
      <h5>Edit Project</h5>
      <input
        v-model="editingProject.name"
        class="form-control mb-2"
      />
      <button class="btn btn-success btn-sm me-2" @click="updateProject">
        Save
      </button>
      <button class="btn btn-secondary btn-sm" @click="editingProject = null">
        Cancel
      </button>
    </div>
  </div>
</template>

<script>
import api from "../services/api";



export default {
  data() {
    return {
      projects: [],
      editingProject: null,
      newProjectName: "",
    };
  },
  methods: {
    fetchProjects() {
      api.get("projects/").then(res => (this.projects = res.data));
    },
    startEdit(project) {
      this.editingProject = { ...project };
    },
    createProject() {
  api.post("projects/", { name: this.newProjectName })
    .then(() => {
      this.$root.showToast("Project created successfully");
      this.newProjectName = "";
      this.fetchProjects();
    })
    .catch(() => {
      this.$root.showToast("Error creating project", "danger");
    });
},
    updateProject() {
      api
        .put(`projects/${this.editingProject.id}/`, this.editingProject)
        .then(() => {
          this.editingProject = null;
          this.fetchProjects();
        });
    },
    deleteProject(projectId) {
        if (!confirm("Are you sure you want to delete this project?")) return;

        api.delete(`projects/${projectId}/`)
        .then(() => {
        this.fetchProjects();
        })
        .catch(err => console.error(err));
    },
  },
  mounted() {
    this.fetchProjects();
    this.$root.showToast("Toast fonctionne 🎉");
  },
  

};
</script>
