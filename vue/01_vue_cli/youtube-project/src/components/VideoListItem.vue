<template>
  <li @click="selectVideo">
    <img :src="youtubeImgSrc" alt="">
    <!-- <span>{{ video.snippet.title }}</span> -->
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
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    youtubeImgSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  },
  
}
</script>

<style>

</style>