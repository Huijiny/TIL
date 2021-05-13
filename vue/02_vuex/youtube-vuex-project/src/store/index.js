import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios' 

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    videos: [],
    selectedVideo: '',
  },
  mutations: {
    SEARCH_ITEM: function (state, videos) {
      state.videos = videos
    },
    SELECT_VIDEO: function (state, video) {
      state.selectedVideo = video
    }
  },
  actions: {
    searchItem: function({ commit }, query) {
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: query,
      }
      axios({
        url: API_URL,
        method: 'GET',
        params,
      })
        .then(res => {
          const videos = res.data.items
          commit('SEARCH_ITEM', videos)
        })
        .catch(err => {
          console.log(err)
        })
    },
    selectVideo: function ({ commit }, video) {
      commit('SELECT_VIDEO', video)
    }
  },
  getters: {
    selectVideoSrc: function (state) {
      const videoId = state.selectedVideo.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
    selectVideoTitle: function (state) {
      console.log(state.selectVideo)
      return state.selectedVideo.snippet.title
    },
    selectVideoDescription: function (state) {
      return state.selectedVideo.snippet.description
    }
  },
  modules: {
  }
})
