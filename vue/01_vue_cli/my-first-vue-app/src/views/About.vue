<template>
  <div class="about">
    <h1>This is an about page</h1>
    <NewComponent my-message="this is prop data" @child-input-change="parentGetChange"/>
  </div>
</template>

<script>
import NewComponent from '@/components/NewComponent.vue'
// '/src'

export default {
  name: 'About',
  components: {
    NewComponent,
  },
  methods: {
    parentGetChange: function (textInput) {
      console.log(`이것은 하위 컴포넌트 NewComponet로 부터 받은 ${textInput} 이다. `)
    }
  }
}
</script>

