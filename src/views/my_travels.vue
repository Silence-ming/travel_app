<template>
    <div id="my_travel">
        <Back msg="我的游记"/>
        <div class="white"></div>
        <div class="con" v-for="item in my_travels" @click="detail(item)" >
            <div class="left">
                <p v-text="item.experience"></p>
                <span v-text="item.times"></span>
            </div>
            <div class="right">
                <img :src="item.img" alt="">
            </div>
        </div>
    </div>
</template>

<script>
     import Back from '@/components/back.vue'
    export default {
        name: "shoucang",
        components:{Back},
        data(){
            return{
                my_travels:[],
                uid:sessionStorage.getItem("uid")
            }
        },
        mounted(){
            fetch('/ajax/MyTravel/?uid='+this.uid).then(function(e){
                return(e.text())
            }).then((e)=>{
                this.my_travels=JSON.parse(e)
            })
        },
        methods:{
            detail(item){
                this.$router.push('/noteDetail/'+item.id)
            }
        }
    }
</script>

<style scoped>
    *{
        margin: 0;
        padding: 0;
        list-style: none;
    }
#my_travel{
    width:100%;height:auto;
}
.white{
    width:100%;
    height:0.9rem;
}
.con{
    width: 7.04rem;
    height: 1.7rem;
    margin: 0 auto;
    margin-top: 0.2rem;
    border-radius: 0.2rem;
    overflow: hidden;
    border: 0.01rem solid #E8E8E8;
    box-shadow: 0 0 0.4rem 0.03rem #E8E8E8;
}
.con .left{
    width:70%;
    height: 100%;
    float:left;
}
.con .right{
    width: 30%;
    height: 100%;
    float:right;
}
.con .left p{
    width:100%;
    height:1.3rem;
    font-size:14px;
    padding:0.2rem;
    box-sizing: border-box;
    overflow: hidden;
}
.con .left span{
    display: block;
    width:100%;
    height:0.2rem;
    font-size:12px;
    color:#616161;
    margin-left:0.2rem;
}
    .con .right img{
        display: block;
        width:100%;
        height:100%;
        background:green;
        border-radius:0.2rem;
    }
</style>