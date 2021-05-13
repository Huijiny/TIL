<template>
  <div v-if="video"> 
    <iframe :src="videoUrl" frameborder="0"></iframe>
    <h2>{{ video.snippet.title | stringUnescape }}</h2>
    <p>{{ video.snippet.description | stringUnescape }}</p>
    <hr>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name:'VideoDetail',
  props: {
    video: {
      type: [String, Object],
    }
  },
  computed: {
    videoUrl: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
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