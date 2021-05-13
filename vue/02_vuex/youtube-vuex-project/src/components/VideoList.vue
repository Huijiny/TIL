<template>
  <div>
    <VideoListItem 
      v-for="(video, index) in videos" 
      :key="index"
      :video="video"
    />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  computed: {
    videos: function () {
      return this.$store.state.videos
    }
  }
}
</script>

<style>

</style>