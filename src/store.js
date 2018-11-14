import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    arr:[1,0,0,0]
  },
  mutations: {
    set(state,obj){
      for (var item in state.arr){
        state.arr[item]=0
      }
      state.arr[obj.num]=obj.value
    }
  },
  actions: {

  }
})
