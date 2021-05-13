<template>
  <div id="app">
    <h1>🧚🏻 Heejini Youtube 🧚🏻</h1>
    <SearchBar/>
    <VideoDetail/>
    <VideoList/>
  </div>
</template>

<script>
import VideoList from '@/components/VideoList'
import SearchBar from '@/components/SearchBar'
import VideoDetail from '@/components/VideoDetail'

export default {
  name: 'App',
  components: {
    VideoList,
    SearchBar,
    VideoDetail,
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
