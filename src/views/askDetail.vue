<template>
    <div id="askDetail">
        <Back msg="回答"/>
        <div class="head">
            <div class="top">
                <span class="h3">{{data.question}}</span>
            </div>
            <div class="bt">
                <p class="time">{{data.times}}</p>
                <v-touch tag="p" class="tell" @tap="write">写回答</v-touch>
            </div>
        </div>
        <div class="answer">
            <div class="box" v-for="item in answers">
                <div class="one">
                    <img :src="item.head" alt="">
                    <span class="name">{{item.name}}</span>
                </div>
                <p class="text" v-html="item.answer"></p>
                <div class="time">发布于 <span>{{item.times}}</span></div>
            </div>
        </div>
    </div>
</template>
<script>
    import Back from '@/components/back.vue'
    export default{
        name:'askDetail',
        components:{Back},
        data(){
            return{
                data:{},
                answers:[]
            }
        },
        mounted(){
            var id=this.$route.params.id;
            fetch('/ajax/askQuestion/?id='+id).then(function(e){
                  return e.text()
              }).then((e)=>{
                  this.data=JSON.parse(e);
                    fetch('/ajax/askDetail/?id='+id).then(function(e){
                      return e.text()
                  }).then((e)=>{
                      this.answers=JSON.parse(e)
                    })
                })
        },
        methods:{
            write(){
                this.$router.push(`/answer/${this.$route.params.id}/${this.data.question}`)
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
  .head{
    width:100%;
    padding:0.1rem  0.05rem;
    padding-top:1rem;
  }
  .head .top{
      width:100%;height:0.5rem;font-size: 15px;
      font-weight:600;
  }
  .top .h3{
    width:50%;
    color:#000;
  }
  .bt{
      width:100%;
  }
    .bt .time{
    margin-top:0.4rem;
    height:0.1rem;
    font-size:12px;
    float:left;
  }
    .bt .tell{
    margin-top:0.4rem;
    font-size:15px;margin-right:0.4rem;
    float:right;color:#5ABFED;
    }
    .answer{
        width:100%;height:auto;
        margin-top:0.2rem;
    }

    .answer .box{
        width:100%;height:auto;
        overflow:hidden;color:#757575;
        border-bottom:5px solid #E6E6E6;padding:0.1rem 0;
    }
    .answer .box .one{
        width:100%;height:0.6rem;
    }
    .answer .box img{
        width:0.5rem;height:0.5rem;float:left;
        border-radius: 50%;display: inline-block;
        margin-top:0.1rem;margin-left:0.1rem;
    }
    .answer .box .name{
        width:1rem;height:0.5rem;color:#9BE6FF;display: block;
        margin-left:0.2rem;font-size: 13px;float: left;margin-top:0.15rem
    }
    .answer .box p{
        width:100%;height:auto;font-size:14px;
        margin-top:0.1rem;margin-left:0.1rem;
    }
    .answer .box .time{
        width:100%;font-size: 12px;margin-left:0.1rem;
        margin-top:0.1rem;
    }
    .answer-img img{
        width:100%;
    }
</style>