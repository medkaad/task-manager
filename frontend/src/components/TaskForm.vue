<template>
    <div>
        <h3>Add Task</h3>
        <form @submit.prevent="submitTask">
            <input v-model="title" placeholder="Task title" required />
            <textarea v-model="description" placeholder="Description"></textarea>
            <select v-model="status">
                <option value="todo">To do</option>
                <option value="doing">Doing</option>
                <option value="done">Done</option>
            </select>
            <button type="submit">Add Task</button>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'TaskForm',
        props: ['projectId'],
        data() {
            return {
                title: '',
                description: '',
                status: 'todo'
            }
        },
        methods: {
            submitTask() {
                axios.post('http://localhost:8000/api/tasks/', {
                    title: this.title,
                    description: this.description,
                    status: this.status,
                    project: this.projectId
                })
                .then(() => {
                    this.title = ''
                    this.description = ''
                    this.status = 'todo'
                    this.$emit('task-added') // pour rafraîchir la liste
                })
                .catch(err => console.error(err))
            }
        }
    }
</script>