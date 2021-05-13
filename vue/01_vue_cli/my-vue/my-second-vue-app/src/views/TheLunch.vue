<template>
  <div>
    <button @click="pickOneLunchMenu">메뉴 추천!</button>
    <p>오늘의 점심 메뉴 : {{ selectedLunchMenu }}</p>

    <input v-model.number="lottoNum" type="number">
    <button @click="setLottoNum">로또</button>

  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['간장계란밥', '스팸', '시래기국밥'],
      selectedLunchMenu: '',
      lottoNum: '',
    }
  },
  methods: {
    pickOneLunchMenu: function () {
      this.selectedLunchMenu = _.sample(this.lunch)
    },
    setLottoNum: function () {
      this.$router.push({ name: 'TheLotto', params:{ lottoNum: this.lottoNum }})
    }
  }
}
</script>

<style>

</style>