<template>
    <div class="search">
        <Back msg="查询" />
         <div class="top">
            <input type="text" placeholder="请输入景点名" v-model="searchInfo">
            <img src="@/assets/img/jing.png" alt="">
        </div>
        <div class="bottom">
            <div @click="details(scenic.id)" class="con" v-for="scenic in filterScenic">
                <div class="left">
                    <img :src="scenic.img" alt="">
                    <p class="name">{{scenic.name}}</p>
                </div>
                <div class="right">
                    <p>{{scenic.detail}}</p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import Back from '@/components/back.vue'
    export default {
        components:{Back},
        //v-focus
        directives: {
            focus: {
              update: function (el, {value}) {
                if (value) {
                  el.focus()
                }
              }
            }
        },
        data(){
            return {
                scenices:[],
                searchInfo:"",
            }
        },
        created(){
          fetch('ajax/getScenices').then(function(e){
              return e.text()
          }).then((e)=>{
              this.scenices = JSON.parse(e);
              for (var scenic of this.scenices){
                  if (scenic.detail != null){
                      scenic.detail = scenic.detail.slice(0,30)+' ...'
                  }
                  scenic.name = scenic.name.slice(0,8);
              }
          })
        },
        computed:{
            filterScenic:function(){
                return this.scenices.filter((scenic)=>{
                    return scenic.name.match(this.searchInfo.replace(/\s+/g,""))
                })
            }
        },
        methods:{
            details(id){
                this.$router.push('/scenic/'+id)
            }
        }
    }
</script>
<style scoped="scoped">
    *{
        padding:0;margin:0;
    }
    img{
        display: block;
    }
    .top{
        width:100%;height:1rem;
        position:fixed;background:#fff;
        top:1rem;left:0;
    }
    .top input{
        display: block;margin-top:0.5em;
        width:95%;height:0.7rem;margin-left:0.15rem;
        position:relative;text-indent: 2.5em;border:0;
        background:#F2F2F2;border-radius: 0.2rem;
        outline: none;
    }
    .top img{
        width:0.3rem;height:0.3rem;
        position: absolute;top:0.3rem;left:0.4rem;
    }
    .bottom{
        width:100%;height:auto;margin-top:2rem;
    }
    .bottom .con{
        width:100%;height:2.1rem;border-radius:.2rem;
        margin-top:.2rem;background:#F2F2F2;
    }
    .con .left{
        width:30%;height:100%;float:left;
        overflow: hidden;
    }
    .left img{
        display: block;
        width:2rem;height:1.5rem;
        margin-left:.1rem;margin-top:.1rem;
    }
    .left .name{
        font-size:13px;
        margin-top:.1rem;font-weight:600;
        width:100%;text-align: center;
    }
    .con .right{
        width:67%;float:left;
        height:100%;
        font-size:16px;
    }
    .right p{
        width:100%;height:100%;letter-spacing:1px;
        padding:.1rem;overflow:hidden;
    }
</style>