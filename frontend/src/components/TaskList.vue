<template>
    <div>
        <h2>Tasks</h2>
        <ul>
            <li v-for="task in Tasks" :key="task.id">
                {{ task.title }} - {{ task.status }}
            </li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'TaskList',
        props: ['projectId'],
        data() {
            return {
                Tasks: []
            }
        },
        mounted(){
            axios.get('http://localhost:8000/api/tasks/?project=${this.projectId}')
            .then(res => this.Tasks = res.data)
            .catch(err => console.error(err))
        }
    }
</script>