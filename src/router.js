import Vue from 'vue'
import Router from 'vue-router'
import ask from './components/ask.vue'
import askDetail from './views/askDetail.vue'
import home from './views/home.vue'
import strategy from './components/strategy.vue'
import scenic from './views/scenic.vue'
import answer from './views/answer.vue'
import writing from './views/writing.vue'
import notes from './components/notes.vue'
import noteDetail from './views/noteDetail.vue'
import person from './components/person.vue'
import asking from './views/asking.vue'
import login from './views/login.vue'
import reg from './views/reg.vue'
import search from './views/search.vue'
import collection from './views/my_collections.vue'
import my_travels from './views/my_travels.vue'
import my_ask from './views/my_ask.vue'
import my_answer from './views/my_answer.vue'
import about from './views/About.vue'
import information from './views/information.vue'
import gaikuang from './views/introduce.vue'
import meishi from './views/food.vue'
import zhusu from './views/live.vue'
import luxian from './views/route.vue'
import account from './views/account.vue'
import rePassWord from './views/rePassWord.vue'

Vue.use(Router);

export default new Router({
  routes: [
      {
        path:'/reg',
        name:'reg',
        component:reg ,
      },
      {
        path:'/login',
        name:'login',
        component:login ,
      },
      {
      path: '/',
      name: 'home',
      component: home,
      children:[
          {
              path: '/strategy',
              name: 'strategy',
              component: strategy
            },
          {
              path: '/ask',
              name: 'ask',
              component: ask
            },
          {
              path: '/notes',
              name: 'notes',
              component: notes
            },
          {
              path: '/person',
              name: '/person',
              component: person
            },
      ]
    },
      {
      path: '/scenic/:id',
      name: 'scenic',
      component: scenic
    },
      {
      path: '/askDetail/:id',
      name: 'askDetail',
      component: askDetail
    },
      {
      path: '/answer/:id/:question',
      name: 'answer',
      component: answer
    },
      {
      path: '/asking',
      name: 'asking',
      component: asking
    },
      {
      path: '/notedetail/:id/:title',
      name: 'notedetail',
      component: noteDetail
    },
       {
      path: '/collection',
      name: 'collection',
      component: collection
    },
      {
      path: '/account',
      name: 'account',
      component: account
    },
      {
      path: '/rePassWord',
      name: 'rePassWord',
      component: rePassWord
    },
      {
        path:'/search',
         name:'search',
         component:search
    },
      {
          path:'/my_travels',
          name:'my_travels',
          component:my_travels,
      },
      {
          path:'/my_ask',
          name:'my_ask',
          component:my_ask,
      },
       {
          path:'/my_answer',
          name:'my_answer',
          component:my_answer,
      },
      {
          path:'/about',
          name:'about',
          component:about,
      },
      {
          path:'/information',
          name:'information',
          component:information,
      },
       {
          path:'/meishi/:id',
          name:'meishi',
          component:meishi,
      },
      {
          path:'/zhusu/:id',
          name:'zhusu',
          component:zhusu,
      },
      {
          path:'/luxian/:id',
          name:'luxian',
          component:luxian,
      },
      {
          path:'/gaikuang/:id',
          name:'gaikuang',
          component:gaikuang,
      },
      {
          path:'/writing',
          name:'writing',
          component:writing,
      },

  ]
})
