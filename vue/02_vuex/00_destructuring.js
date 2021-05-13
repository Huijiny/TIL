const context = {
  commit: function () {
    console.log('안녕하세요 commit!')
  },
  state: {
    todo: '할 일 1',
  },
  getters: {},
  mutations: {},
}

//1. 하나 하나 할당
// const commit = context.commit
// const state = context.state

// console.log(commit())
// console.log(state)

//2. 이름으로 가져온다.
const { commit, state } = context
console.log(commit())
console.log(state)