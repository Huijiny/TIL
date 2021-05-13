<template>
  <div>
    <h2>점심메뉴</h2>
    <button @click="pickOneLunchMenu">Pick Lunch</button>
    <p>{{ selectedLunchMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      menus: ['소고기', '양념치킨', '냉면'],
      selectedLunchMenu: '',
    }
  },
  methods: {
    pickOneLunchMenu: function () {
      this.selectedLunchMenu = _.sample(this.menus)
    }
  }
}
</script>

<style>

</style>