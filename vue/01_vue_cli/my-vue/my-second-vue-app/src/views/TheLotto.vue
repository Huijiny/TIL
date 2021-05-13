<template>
  <div>
    <h2>로또 번호 추첨</h2>
    <button @click="getLottoNums">
      로또 추첨!
    </button>
    <p>{{ $route.params }}</p>
    <p>{{ selectedLottoNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name:'TheLotto',
  data: function () {
    return {
      selectedLottoNums: [],
      sampeNums: [],
    }
  },
  methods: {
    getLottoNums: function () {
      const numbers = _.range(1, 46)
      this.sampeNums = _.sampleSize(numbers, this.$route.params.lottoNum)
      this.selectedLottoNums = _.sortBy(this.sampeNums)
    }
  }
}
</script>

<style>

</style>