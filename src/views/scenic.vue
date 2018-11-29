<template>
    <div id="scenic">
        <Back :msg="data.name" />
        <div class="top">
            <img :src="data.img" alt="">
            <p>{{ data.name }}</p>
        </div>
        <v-touch tag='p' v-on:tap='collect' class="collec">{{collect_message}}</v-touch>
        <div class="min">
            <h3>景点介绍</h3>
            <p>{{ data.detail }}</p>
        </div>
        <div class="bottom">
            <h3>旅游攻略</h3>
            <div class="box">
                 <v-touch tag="div" v-on:tap="sel1(data.id)" class="select">概况</v-touch>
                 <v-touch tag="div" v-on:tap="sel2(data.id)" class="select">美食</v-touch>
                 <v-touch tag="div" v-on:tap="sel3(data.id)" class="select">住宿</v-touch>
                 <v-touch tag="div" v-on:tap="sel4(data.id)" class="select">路线</v-touch>
            </div>
        </div>
    </div>
</template>
<script>
    import Back from '@/components/back.vue'
    export default {
        name:'scenic',
        components:{
            Back
        },
        data(){
            return{
                uid:sessionStorage.getItem('uid'),
                sid:'',
                data:{},
                collect_message:'',
            }
        },
        mounted(){
            this.sid= this.$route.params.id;
             fetch('/ajax/scenicDetail/?id='+this.sid).then(function(e){
                    return e.text()
                }).then((e)=>{
                    this.data=JSON.parse(e)
                    this.axios.get(`/ajax/collectInfo/?uid=${this.uid}&sid=${this.sid}`)
                        .then((e)=>{
                            if (e.data == 'ok'){
                                this.collect_message = '取消收藏'
                            }else{
                                this.collect_message = '收藏'
                            }
                        })
                })
        },
        methods:{
            collect(){
                var form =new FormData();
                form.append('uid',this.uid);
                form.append('sid',this.sid);
                form.append('flag',this.flag);
              this.axios.post('/ajax/collect',form)
                  .then((e)=>{
                      if (e.data == 'insert'){
                          this.collect_message = '取消收藏'
                      }else if(e.data == 'delete'){
                          this.collect_message = '收藏'
                      }
                  })
                  .catch((error)=>{
                      alert('服务器请求异常')
                  })
            },
            sel1(id){
                this.$router.push('/gaikuang/'+id)
            },
            sel2(id){
                this.$router.push('/meishi/'+id)
            },
            sel3(id){
                this.$router.push('/zhusu/'+id)
            },
            sel4(id){
                this.$router.push('/luxian/'+id)
            },
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
    .top{
        width:100%;height:4rem;
        position:relative;padding-top:1rem;
    }
    .top img{
        width:100%;height:100%;
    }
    .top p{
        position:absolute;bottom:0.1rem;left:0.1rem;
        font-size:15px;color:#fff;
    }
    .min{
        width:100%;height:auto;margin-top:0.2rem;
    }
    .min h3{
        font-size: 15px; letter-spacing: 0.05rem;
    }
    .min p{
        width:100%;height:auto;font-size:13px;
        color:#757575;margin-top:0.1rem;
        text-indent: 2em;line-height: 0.5rem;
    }
    .bottom{
        width:100%;height:1rem;
        margin-top:0.2rem;
    }
    .bottom h3{
         font-size: 15px;
         letter-spacing: 0.05rem;
    }
    .bottom .box{
         width:100%;height:1rem;margin-top:0.1rem;
        display: flex;justify-content: space-between;
    }
    .bottom .box .select{
        width:25%;text-align: center;font-size: 14px;color:deepskyblue;

    }
     .collec{
        font-size:15px;
        position:fixed;
        top:.3rem;right:0.6rem;
        color:#5ABFED;
        z-index: 99;
         font-weight:600;
    }
</style>