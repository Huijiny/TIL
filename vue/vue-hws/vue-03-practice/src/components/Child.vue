<template>
  <div>
    <h1>Child</h1>
    <input type="text" @input="sendChildData" :value="childData">
    <p>AppData: {{ appData }}</p>
    <p>ParentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    appData: {
      type: String
    },
    parentData: {
      type: String
    },
    childData: {
      type: String
    }
  },
  methods: {
    sendChildData: function (event) {
      this.$emit('child-data', event.target.value)
    },
  }
}
</script>

<style>

</style>