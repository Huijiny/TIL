<template>
  <div>
    TodoList
    <TodoListItem/>
  </div>
</template>

<script>
import TodoListItem from './TodoListItem.vue'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  }
}
</script>

<style>

</style>