<template>
  <div id="wrapper">
    <!-- Sidebar -->
    <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion">

      <a class="sidebar-brand d-flex align-items-center justify-content-center">
        <div class="sidebar-brand-text mx-3">Task Manager</div>
      </a>

      <hr class="sidebar-divider my-0" />

      <li class="nav-item">
        <router-link class="nav-link" to="/dashboard">
          <i class="fas fa-fw fa-tachometer-alt"></i>
          <span>Dashboard</span>
        </router-link>
      </li>

      <li class="nav-item">
        <router-link class="nav-link" to="/projects">
          <i class="fas fa-fw fa-folder"></i>
          <span>Projects</span>
        </router-link>
      </li>

      <hr class="sidebar-divider d-none d-md-block" />
    </ul>

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">
      <div id="content">

        <!-- Topbar -->
        <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 shadow">
          <button
            class="btn btn-link d-md-none rounded-circle mr-3"
            @click="toggleSidebar"
          >
            <i class="fa fa-bars"></i>
          </button>

          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <button class="btn btn-danger btn-sm" @click="logout">
                Logout
              </button>
            </li>
          </ul>
        </nav>

        <!-- Page Content -->
        <div class="container-fluid">
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push("/login");
    },
    toggleSidebar() {
      document.body.classList.toggle("sidebar-toggled");
    }
  }
};
</script>
