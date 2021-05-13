<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Parent 
      @parent-data="getParentData"
      @child-data="getChildData"
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
    />
  </div>
</template>

<script>
import Parent from './components/Parent.vue'

export default {
  name: 'App',
  components: {
    Parent,
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    getParentData: function (parentData) {
      this.parentData = parentData
    },
    getChildData: function (childData) {
      this.childData = childData
    }
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
