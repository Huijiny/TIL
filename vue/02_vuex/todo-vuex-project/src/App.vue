<template>
  <div id="app"> 
    <h1>Todo List</h1>
    <h2>완료된 할 일 : {{ completedTodoCount }}</h2>
    <h2>해야할 일: {{ uncompletedTodoCount }}</h2>
    <TodoForm/>
    <TodoList/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    // completedTodoCount: function () {
    //   return this.$store.getters.completedTodoCount
    // },
    // uncompletedTodoCount: function () {
    //   return this.$store.getters.uncompletedTodoCount
    // }
    ...mapGetters([
      'completedTodoCount',
      'uncompletedTodoCount',
    ])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
