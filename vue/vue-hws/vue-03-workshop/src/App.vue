<template>
  <div id="app">
    <h1>My first youtube project</h1>
    <SearchBar
      @search-data="onSearchData"
    />
    <VideoDetail
      :video="selectedVideo"
    />
    <VideoList 
      :videos="videos"
      @video-data="onVideoSelect"
    />
    
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      searchData: '',
      videos: [],
      selectedVideo: '',
    }
  },
  methods: {
    onVideoSelect: function (video) {
      this.selectedVideo = video
      console.log(this.selectedVideo)
    },
    onSearchData: function (query) {
      this.searchData = query
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.searchData,
      }

      axios({
        url: API_URL,
        method: 'GET',
        params,
      }) 
        .then(res => {
          this.videos = res.data.items
        })
        .catch(err => {
          console.log(err)
        })

    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
