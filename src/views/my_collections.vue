<template>
    <div id="colletion">
        <Back msg="我的收藏"/>
        <div class="white"></div>
        <div class="con" v-for="item in collections" @click="details(item)" >
            <div class="up">
                <span class="imgs"><img :src="item.img" alt=""></span>
                <span class='content' v-text="item.detail"></span>
            </div>
            <div class="down">
                <p v-text="item.name" style="color:#8DE3F5"></p>
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
                collections:[],
                uid:sessionStorage.getItem("uid")
            }
        },
        mounted(){
            fetch('/ajax/collections/?uid='+this.uid).then(function(e){
                return(e.text())
            }).then((e)=>{
                this.collections=JSON.parse(e)
            })
        },
        methods:{
            details(item){
                this.$router.push('/scenic/'+item.id)
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
#colletion{
    width:100%;height:auto;
    overflow: auto;
}
.white{
    width:100%;
    height:0.9rem;
}
.con{
    width: 7.04rem;
    height: 1.6rem;
    margin: 0 auto;
    margin-top: 0.2rem;
    border-radius: 0.2rem;
    overflow: hidden;
    border: 0.01rem solid #E8E8E8;
    box-shadow: 0 0 0.4rem 0.03rem #E8E8E8;
}
    .con .up{
        width: 100%;
        height: auto;
        margin-top: 0.3rem;
    }
    .con .down{
        width: 100%;
        height: auto;
        margin-top: 0.04rem;
    }
     .con .up span:first-child{
         display: block;
         width: 0.7rem;
         height: 0.7rem;
         float: left;
         margin-left: 0.3rem;
         position: relative;
     }
     .con .up span:first-child img{
         width: 0.7rem;
         height: 0.7rem;
         position: absolute;
         border-radius:50%;
         border:1px solid #cacaca;
     }
    .con .up span:nth-child(2){
         display: block;
         width: 5rem;
         height: 0.8rem;
         font-size: 0.26rem;
        margin-left: 1.2rem;
    }
        .con .down p{
            float: left;
            font-size: 0.2rem;
             margin-left: 0.4rem;
    }

</style>