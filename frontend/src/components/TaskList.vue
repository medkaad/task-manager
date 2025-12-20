<template>
    <div>
        <h2>Tasks</h2>
        <TaskForm :projectId="projectId" @task-added="fetchTasks" />
        <ul>
            <li v-for="task in Tasks" :key="task.id">
                {{ task.title }} - {{ task.status }}
            </li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios'
import TaskForm from './TaskForm.vue';

    export default {
        name: 'TaskList',
        props: ['projectId'],
        components: {TaskForm},
        data() {
            return {
                Tasks: []
            }
        },
        mounted() { this.fetchTasks() },
        methods: {
            fetchTasks() {
                axios.get('http://localhost:8000/api/tasks/?project=${this.projectId}')
                .then(res => this.tasks = res.data)
                .catch(err => console.error(err))
            }
        }
    }
</script>