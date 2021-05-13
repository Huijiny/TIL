<template>
  <div>
    <input @keyup.enter="searchItem" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    searchItem: function (event) {
      this.query = event.target.value
      this.$store.dispatch('searchItem', this.query)
    }
  }
}
</script>

<style>

</style>