<template>
  <li @click="onVideoSelect">
    <img :src="youtubeImgSrc" alt="">
    {{ video.snippet.title | stringUnescape}}
  </li>
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
  computed: {
    youtubeImgSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    onVideoSelect: function () {
      this.$emit('video-data', this.video)
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>