<template>
  <div>
    <h1>Parent</h1>
    <input @input="getParentData" type="text" :value="parentData">
    <p>AppData: {{ appData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Child
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @child-data="getChildData"
    />
  </div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  components: {
    Child,
  },
  props: {
    appData: {
      type: String,
    },
    parentData: {
      type: String,
    }, 
    childData: {
      type: String,
    }
  },
  methods: {
    getChildData: function (childData) {
      this.$emit('child-data', childData)
    },
    getParentData: function (event) {
      this.$emit('parent-data', event.target.value)
    }
  }
}
</script>

<style>

</style>