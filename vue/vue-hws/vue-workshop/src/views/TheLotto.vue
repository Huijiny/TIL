<template>
  <div>
    <h2>로또</h2>
    <button @click="getLottoNums">Get Lucky Numbers</button>
    <p>{{ lottoNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      lottoNums: [],
    }
  },
  methods: {
    getLottoNums: function () {
      const numbers = _.range(1, 46)
      this.lottoNums = _.sortBy(_.sampleSize(numbers, 6))
    }
  }
}
</script>

<style>

</style>