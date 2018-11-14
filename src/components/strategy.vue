<template>
<div class="hots">
    <div class="top" @click="search">
        <input type="text" placeholder="请输入景点名">
        <img src="@/assets/img/jing.png" alt="">
    </div>
    <div class="min">
        <v-touch  @panstart="panstart" @panleft="panleft" @panright="panright" @panend="panend">
            <div class="view">
                <div class="bigBox" ref="box">
                     <div class="box" v-for="item in banners">
                        <img :src="item.img" alt="" @click="details(item.id)">
                        <p>{{ item.detail }}</p>
                    </div>
                </div>
            </div>
        </v-touch>
    </div>
    <div class="bottom">
        <div class="selects">
            <v-touch tag="p" class="province" v-for="item1 in cites" @tap="check(item1)" :class="{active:item1.state==1}">{{ item1.cname }}</v-touch>
        </div>
        <div class="banners">
            <div class="scenic" v-for="i in scenic">
                <img :src="i.img" alt="" @click="details(i.id)">
                <h4>{{ i.name }}</h4>
            </div>
        </div>
    </div>
</div>
</template>
<script>
    export default {
        data(){
            return{
                cites:[],
                scenic:[],
                banners:[],
                init:'',
                direction:'',
                length:'150',
                num:0,
            }
        },
        mounted(){
            fetch("/ajax/cites/").then(function(e){
                return e.text()
            }).then((e)=>{
                var arr=JSON.parse(e);
                for (var i in arr){
                    arr[i]['state'] = 0
                }
                arr[0]['state'] = 1;
                this.cites=arr;
                fetch("/ajax/scenicBanners/").then(function(e){
                    return e.text()
                }).then((e)=>{
                    this.banners=JSON.parse(e);
                    fetch('ajax/firstScenic').then(function(e){
                        return e.text()
                    }).then((e)=>{
                        this.scenic =JSON.parse(e)
                    })
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
            check(current){
                for (var item of this.cites){
                    item.state=0
                }
                current.state=1;
                fetch('/ajax/scenic/?cid='+current.id).then(function(e){
                    return e.text()
                }).then((e)=>{
                    this.scenic=JSON.parse(e)
                })
            },
            details(id){
                this.$router.push('/scenic/'+id)
            },
            search(){
                this.$router.push('/search')
            }
        }
    }
</script>
<style scoped>
    *{
        padding:0;margin:0;
    }
    img{
        display: block;
    }
    .active{
        color:red;
    }
    .top{
        width:100%;height:0.8rem;
    }
    .top input{
        display: block;margin-top:0.1em;
        width:95%;height:0.7rem;margin-left:0.15rem;
        position:relative;text-indent: 2.5em;border:0;
        background:#F2F2F2;border-radius: 0.2rem;
        outline: none;
    }
    .top img{
        width:0.3rem;height:0.3rem;
        position: absolute;top:0.35rem;left:0.6rem;
    }
    .min{
        margin-top:0.1rem;
        width:100%;height:4rem;
    }
     .min .view{
        width:100%;height:4rem;overflow: hidden;
    }
    .min .view .bigBox{
        width:400%;height:100%;
    }
    .min .bigBox .box{
        width:25%;height:100%;float:left;
        position:relative;
    }
    .min .bigBox .box img{
        width:100%;height:100%;
    }
    .min .bigBox .box p{
        width:100%;font-size: 15px;
        font-weight: 600;position: absolute;
        bottom:0.2rem;left:0.2rem;color:#fff;
    }
    .bottom{
        width:100%;height:6rem;
        margin-top:0.2rem;
    }
    .bottom .selects{
        width:100%;height:2.8rem;
        flex-wrap:wrap;
        display: flex;justify-content: flex-start;
        color:#757575;overflow:scroll;
    }
    .selects .province{
        margin-top:0.3rem;
        width:20%;height:0.4rem;
        text-align: center;
        font-size: 12px;
    }
    .bottom .banners{
        width:100%;height:4rem;
        margin-top:0.1rem;
        flex-wrap:wrap;
        display: flex;justify-content: flex-start;
    }
    .banners .scenic{
        width:30%;height:1.8rem;margin-top:0.13rem;
        font-size:12px;margin-left:0.2rem;
    }
    .banners .scenic img{
        width:100%;height:85%;
    }
    .banners .scenic h4{
        margin-top:0.1rem;color:#757575;
        width:100%;text-align: center;
    }
</style>