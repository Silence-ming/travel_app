<template>
    <div id="home">
        <router-view/>
        <div class="banner">
            <div class="box" @click="hots" :class="{active:arr[0]==1}">
                <span class="iconfont">&#xe633;</span>
                <p>攻略</p>
            </div>
            <div class="box" @click="asks" ref="box2" :class="{active:arr[1]==1}">
                <span class="iconfont">&#xe671;</span>
                <p>问答</p>
            </div>
            <div class="box" @click="notes" ref="box3" :class="{active:arr[2]==1}">
                <span class="iconfont">&#xe63e;</span>
                <p>游记</p>
            </div>
            <div class="box" @click="person" ref="box4" :class="{active:arr[3]==1}">
                <span class="iconfont">&#xe650;</span>
                <p>个人中心</p>
            </div>
        </div>
    </div>
</template>
<script>
    export default{
        name:'home',
        data(){
            return{
            }
        },
        computed:{
            arr(){
                return this.$store.state.arr
            }
        },
        methods:{
            hots(){
                this.$store.commit('set',{num:0,value:1});
                this.$router.push('/strategy')
            },
            asks(){
                this.$store.commit('set',{num:1,value:1});
                this.$router.push('/ask')
            },
            notes(){
                this.$store.commit('set',{num:2,value:1});
                this.$router.push('/notes')
            },
            person(){
                if (sessionStorage.getItem('uid')){
                    this.$store.commit('set',{num:3,value:1});
                    this.$router.push('/person')
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
    img{
        display: block;
    }
    .active{
        color:#2FCBFF;
    }
    .banner{
        width:100%;height:1rem;border-top:1px solid #707070;
        display:flex;justify-content: space-around;box-sizing: border-box;
        position:fixed;bottom:0;left:0;z-index: 99;background: #fff;color:#757575;
    }
    .banner .box{
        margin-top:0.1rem;
        width:1rem;height:0.6rem;
    }
    .box span{
        width:0.4rem;height:0.4rem;font-size:20px;
        margin-left:0.3rem;display:block;
    }
    .box p{
        font-size: 12px;
        margin-top:0.05rem;
        width:100%;text-align: center;
    }
</style>