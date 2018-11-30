<template>
  <div id="notes">
     <div class="top">
        <v-touch  @panstart="panstart" @panleft="panleft" @panright="panright" @panend="panend">
            <div class="view">
                <div class="bigBox" ref="box">
                     <v-touch tag="div" class="box" v-for="item in banner" v-on:tap="details(item)">
                        <img :src="item.img" alt="">
                        <p>{{ item.title }}</p>
                    </v-touch>
                </div>
            </div>
        </v-touch>
    </div>
     <div class="bottom">
         <v-touch tag="div" class="box" v-for="item in notes" v-on:tap="details(item)">
             <div class="left">
                 <div class="t">
                     <img :src="item.head" alt="">
                     <span>{{item.name}}</span>
                 </div>
                 <div class="title">{{item.title.slice(0,25)}}</div>
                 <div class="con">{{item.experience.slice(0,25)+'......'}}</div>
             </div>
             <div class="right">
                 <img :src="item.img" alt="">
             </div>
         </v-touch>
    </div>
      <v-touch class="asking" tag="div" @tap="writing">
          <p class="text">写游记</p>
     </v-touch>
  </div>
</template>

<script>
export default {
  name: 'ask',
  data(){
      return{
          uid:sessionStorage.getItem('uid'),
          banner:[],
          init:'',
          direction:'',
          length:'150',
          num:0,
          notes:[]
      }
  },
     mounted(){
      fetch('/ajax/notes/').then(function(e){
          return e.text()
      }).then((e)=>{
          this.notes=JSON.parse(e);
           fetch("/ajax/noteBanner/").then(function(e){
                return e.text()
            }).then((e)=>{
                this.banner=JSON.parse(e)
            })
      })
    },
    methods:{
           panstart(){
                this.init=this.$refs.box.offsetLeft
            },
            panleft(e){
                this.$refs.box.style.transition='';
                this.$refs.box.style.marginLeft=this.init+e.deltaX+'px';
                this.direction='left'
            },
            panright(e){
                this.$refs.box.style.transition='';
                this.$refs.box.style.marginLeft=this.init+e.deltaX+'px';
                this.direction='right'
            },
            panend(e){
                this.$refs.box.style.transition='margin 0.3s linear';
                if (e.distance>this.length){
                    if(this.direction=='left'){
                        this.num++;
                        if (this.num>3){
                            this.num=3
                        }
                        this.$refs.box.style.marginLeft=-this.num*100+'%'
                    }else if(this.direction=='right'){
                        this.num--;
                        if (this.num<0){
                            this.num=0
                        }
                         this.$refs.box.style.marginLeft=-this.num*100+'%'
                    }
                }else{
                    this.$refs.box.style.marginLeft=-this.num*100+'%'
                }
            },
            details(item){
               this.$router.push('/notedetail/'+item.id+'/'+item.title)
            },
            writing(){
              if (this.uid){
                  this.$router.push('/writing')
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
  #notes{
    overflow: hidden;
  }
  img{
    display: block;
  }
   .top{
        margin-top:0.1rem;
        width:100%;height:4rem;
    }
     .top .view{
        width:100%;height:4rem;overflow: hidden;
    }
    .top .view .bigBox{
        width:400%;height:100%;
    }
    .top .bigBox .box{
        width:25%;height:100%;float:left;
        position:relative;
    }
    .top .bigBox .box img{
        width:100%;height:100%;
    }
    .top .bigBox .box p{
        width:95%;font-size: 15px;height:auto;
        font-weight: 600;position: absolute;
        bottom:0.2rem;left:0.2rem;color:#fff;
    }
  .bottom{
    width:100%;height:auto;
  }
  .bottom .box{
    width:100%;height:2.3rem;margin-top:0.2rem;
  }
  .bottom .box:last-child{
    padding-bottom:4.5rem;
  }
  .box .left{
    width:60%;height:2.5rem;
    float:left;
  }
  .left .t{
    width:100%;height:0.5rem;
  }
  .t img{
    width:0.5rem;height:0.5rem;margin-left:0.1rem;
    margin-top:0.05rem;border-radius: 50%;float:left;
  }
  .t span{
    display: block;width:1rem;height:0.5rem;float:left;
    margin-left:0.1rem;margin-top:0.15rem;font-size:13px;color:#2FCBFF;
  }
  .left .title{
    width:100%;height:auto;margin-left:0.1rem;
    font-size:15px;overflow: hidden;
  }
  .left .con{
      width:100%;height:auto;margin-top:0.1rem;
      font-size:14px;color:#757575;margin-left: 0.1rem;
  }
  .box .right{
    width:40%;height:2rem;margin-top:0.05rem;
    float:right;
  }
  .right img{
    width:95%;height:2.1rem;margin-left:0.2rem;
      margin-top:.1rem;
  }
    .asking{
    width:1.8rem;height:0.8rem;border-radius: 0.5rem;
    background:#FCE247;position:fixed;
    bottom:1.5rem;left:0;right:0;margin:0 auto;

  }
  .asking .text{
    font-size:18px;
    line-height: 0.8rem;font-weight:600;text-align:center;
  }
</style>
