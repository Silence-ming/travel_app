import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/assets/js/rem.js'
import '@/assets/font/iconfont.css'
import VueTouch from 'vue-touch'
import axios from 'axios'
import Qs from 'qs'

Vue.prototype.axios = axios;
Vue.prototype.qs = Qs;
Vue.config.productionTip = false;
// var VueTouch = require('vue-touch');
Vue.use(VueTouch,{name: 'v-touch'});
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
