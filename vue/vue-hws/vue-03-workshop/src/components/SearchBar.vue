<template>
  <div>
    <input @keyup.enter="sendSearchQuery" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    sendSearchQuery: function (event) {
      this.$emit('search-data', event.target.value)
    }
  }
}
</script>

<style>

</style>