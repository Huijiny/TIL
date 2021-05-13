<template>
  <ul>
    <VideoListItem
    v-for="(video, idx) in videos" 
    :key="idx"
    :video="video"
    @video-data="onVideoSelect"
    />
    
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
export default {
  name:'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
    },
  },
  methods: {
    onVideoSelect: function (video) {
      this.$emit('video-data', video)
    }
  }
}
</script>

<style>

</style>