<template>
  <div>
    <iframe :src="youtubeUrl" frameborder="0"></iframe>
    <hr>
    {{ video.snippet.title | stringUnescape}}
    {{ video.snippet.description | stringUnescape}}
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: [String, Object]
    },
  },
  computed: {
    youtubeUrl: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
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