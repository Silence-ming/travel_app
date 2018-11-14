<template>
  <div id="person">
     <div class="top">
         <!--<p class="logo">欢迎来到轻游</p>-->
         <div class="data">
             <img class='head' :src="person.head" alt="">
            <p class="name">{{person.uname}}</p>
         </div>
         <p class="note">{{person.note}}</p>
     </div>
      <div class="min">
          <v-touch class="box box1" tag="div" v-on:tap="collection">
              <div class="iconfont i1">&#xe61a;</div>
              <p>我的收藏</p>
          </v-touch>
          <v-touch class="box box2" tag="div" v-on:tap="travel">
              <div class="iconfont i2">&#xe63e;</div>
              <p>我的游记</p>
          </v-touch>
          <v-touch class="box box3" tag="div" v-on:tap="myAsk">
              <div class="iconfont i3">&#xe60a;</div>
              <p>我的问题</p>
          </v-touch>
           <v-touch class="box box4" tag="div" v-on:tap="myAnswer">
              <div class="iconfont i4">&#xe66e;</div>
              <p>我的回答</p>
          </v-touch>
      </div>
      <div class="bottom">
          <v-touch class="select" tag="div" v-on:tap="information">
                <div class="iconfont ic0">&#xe650;</div>
               <p>个人信息</p>
          </v-touch>
          <v-touch class="select" tag="div" v-on:tap="account">
              <div class="iconfont ic1">&#xe61b;</div>
               <p>账号设置</p>
          </v-touch>
          <v-touch class="select" tag="div" v-on:tap="about">
             <div class="iconfont ic2">&#xe602;</div>
               <p>关于轻游</p>
          </v-touch>
          <v-touch class="select" tag="div" v-on:tap="edit">
              <div class="iconfont ic3">&#xe638;</div>
               <p>退出登陆</p>
          </v-touch>
      </div>
  </div>
</template>

<script>
export default {
  name: 'ask',
  data(){
      return{
          person:{},
          uid:sessionStorage.getItem('uid')
      }
  },
    mounted(){
      fetch('ajax/person/?id='+this.uid).then(function(e){
          return e.text()
      }).then((e)=>{
          this.person=JSON.parse(e)
      })
    },
    methods:{
      collection(){
            this.$router.push('/collection')
      },
        travel(){
             this.$router.push('/my_travels')
        },
        myAsk(){
             this.$router.push('/my_ask')
        },
        myAnswer(){
             this.$router.push('/my_answer')
        },
        edit(){
            sessionStorage.removeItem('uid');
            sessionStorage.removeItem('uname');
            this.$router.push('/login')
        },
        information(){
            this.$router.push('/information')
        },
        account(){
            this.$router.push('/account')
        },
        about(){
            this.$router.push('/about')
        }
    }
}
</script>
<style scoped>
  *{
    margin:0;padding:0;
  }
  img{
    display: block;
  }
  #person{
      background:#F5F5F5;
  }
  .top{
      width:100%;height:4rem;
      background:#fff;overflow:hidden ;
  }

  .top .data{
      width:100%;height:1rem;margin-top:0.8rem;margin-left:0.5rem;
  }
    .data .head{
        width:1.5rem;height:1.5rem;float:left;
        border-radius: 50%;
    }
    .data .name{
        font-size:30px;
        float:left;margin-left:0.2rem;margin-top:0.2rem;
    }
    .top .note{
        font-size:15px;font-family:'楷体';margin-top:1rem;margin-left:0.5rem;
        color:#757575;
    }
    .min{
        background:#fff;margin-top:0.2rem;
        width:100%;height:2rem;display: flex;justify-content: space-around;
    }
    .min .box{
        margin-top:0.35rem;
        width:1.5rem;height:1rem;
    }
    .min .box .iconfont{
        width:0.7rem;height:0.7rem;border-radius:50%;
        margin-left:0.25rem;font-size:25px;
    }
    .i1{
        color:#FCE247;
    }
    .i2{
        color:#5ABFED;
    }
    .i3{
        color:#88D876;
    }
    .min .box p{
        font-size:13px;color:#757575;margin-top:0.1rem;
    }
     .bottom{
        margin-top:0.2rem;background:#fff;
        width:100%;height:auto;
    }
    .bottom .select{
        width:100%;height:0.9rem;font-size:14px;color:#757575;
        line-height: 0.9rem;border-bottom: 1px solid #F5F5F5;
        text-indent: 0.5em;
    }
    .select .iconfont{
        float:left;font-size:20px
    }
    .ic1{
        color:#FCE247;
    }
    .ic2{
        color:#5ABFED;
    }
    .ic3{
        color:#88D876;
    }
    .i4{
        color:#5ABFED;
    }
    .ic0{
        color:#5ABFED;
    }
    .select p {
        float: left;
        margin-left: 0.1rem;
    }
</style>
