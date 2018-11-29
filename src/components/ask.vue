<template>
  <div id="ask">
    <v-touch class="top" tag="div" v-on:tap = "asking">
      <input type = "text" placeholder = "在这里输入问题" disabled="disabled">
      <img src = "@/assets/img/jing.png" alt = "">
    </v-touch>
    <div class = "content">
      <v-touch tag="div" class="box" v-for="item in data" v-on:tap = "detail(item.id)">
        <p class="head">{{item.question}}</p>
        <p class="time">{{item.times}}</p>
      </v-touch>
    </div>
  </div>
</template>

<script>


export default {
  name: 'ask',
  data(){
      return{
          uid:sessionStorage.getItem('uid'),
          data:[]
      }
  },
    mounted(){
      fetch('/ajax/ask/').then(function(e){
          return e.text()
      }).then((e)=>{
          this.data=JSON.parse(e)
      })
    },
    methods:{
      detail(id){
          this.$router.push('/askDetail/'+id)
      },
        asking(){
          if (this.uid){
              this.$router.push('/asking')
          }else{
              this.$router.push('/login')
          }
        }
    }
}
</script>
<style scoped>
  *{
    margin:0;padding:0;
  }
  #ask{
    background:#F5F5F5;
    overflow: hidden;
  }
  .top{
        width:100%;height:0.8rem;
      background:#fff;position:fixed;top:0;left:0;
  }
  .top input{
      display: block;margin-top:0.45em;
      width:95%;height:0.7rem;margin-left:0.15rem;
      position:relative;text-indent: 3em;border:0;
      background:#F2F2F2;border-radius: 0.2rem;
      outline: none;
  }
  .top img{
      width:0.3rem;height:0.3rem;
      position: absolute;top:0.3rem;left:0.6rem;
  }
  .content{
    width:100%;margin-top:0.6rem;
  }
  .content .box{
    background:#fff;
    margin-bottom:0.2rem;
    width:100%;
    height:2rem;
    padding:0.1rem  0.05rem;
    color:#616161;
  }
  .box:last-child{
    padding-bottom:1.5rem;
  }
  .box .head{
    width:100%;height:1.5rem;
    color:#000;
    font-size:15px;
    font-weight:600;
  }
  .box .con{
    margin-top:0.05rem;
    width:100%;
    height:1rem;
    font-size:0.12rem;
  }
  .box .time{
    margin-top:0.1rem;
    width:100%;
    height:0.1rem;
    font-size:0.12rem;
  }
</style>
