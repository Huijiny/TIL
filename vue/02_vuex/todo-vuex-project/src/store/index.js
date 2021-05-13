import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todos: []
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO: function (state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          return {
            ...todo,
            completed: !todo.completed,
          }
        }
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodo: function({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    }
  },
  getters: {
    completedTodoCount: function (state) {
      return state.todos.filter(todo => {
        return todo.completed === true
      }).length
    },
    uncompletedTodoCount: function (state) {
      return state.todos.filter(todo => {
        return todo.completed === false
      }).length
    }
  },
  modules: {
  }
})
