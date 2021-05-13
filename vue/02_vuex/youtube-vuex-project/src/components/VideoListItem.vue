<template>
  <div @click="selectVideo">
    <img :src="youtubeImgSrc" alt="">
    <h2>{{ video.snippet.title | unescapeSentence}}</h2>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
    },
  },
  methods: {
    selectVideo: function() {
      this.$store.dispatch('selectVideo', this.video)
    }
  },
  computed: {
    youtubeImgSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    unescapeSentence: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>