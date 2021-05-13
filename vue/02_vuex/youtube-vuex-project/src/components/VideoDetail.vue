<template>
  <div>
    <iframe :src="selectVideoSrc" frameborder="0"></iframe>
    <h2>{{ selectVideoTitle | unescapeSentence }}</h2>
    <p>{{ selectVideoDescription | unescapeSentence }}</p>
    <hr>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex'

export default {
  name: 'VideoDetail',
  computed: {
    ...mapGetters([
      'selectVideoSrc',
      'selectVideoTitle',
      'selectVideoDescription',
    ])
  },
  filters: {
    unescapeSentence: function (rawText) {
      return _.unescape(rawText)
    },
  }
}
</script>

<style>

</style>