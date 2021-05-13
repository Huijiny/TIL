<template>
  <ul>
    <VideoListItem 
      v-for="(video, index) in videos" 
      :key="index"
      :video="video"
      @select-video="onSelectVideo"
    />
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
    },
  }, 
  methods: {
    onSelectVideo: function (video) {
      console.log(video)
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>