<template>
    <div id="colletion">
        <Back msg="我的问题"/>
        <div class="white"></div>
        <div class="con" v-for="item in myAsks" @click="detail(item)" >
            <div class="top">
                <p v-text="item.question"></p>
            </div>
            <div class="bottom">
                <p v-text="item.times"></p>
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
                myAsks:[],
                uid:sessionStorage.getItem("uid")
            }
        },
        mounted(){
            fetch('/ajax/myAsks/?uid='+this.uid).then(function(e){
                return(e.text())
            }).then((e)=>{
                this.myAsks=JSON.parse(e)
            })
        },
        methods:{
            detail(item){
                this.$router.push('/askDetail/'+item.id)
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
    height: auto;
    margin: 0 auto;
    margin-top: 0.2rem;
    border-radius: 0.2rem;
    overflow: hidden;
    border: 0.01rem solid #E8E8E8;
    box-shadow: 0 0 0.4rem 0.03rem #E8E8E8;
}
    .con .top{
        width:100%;
        height:auto;
        font-size:15px;
        padding:0.2rem;
        box-sizing:border-box;
        overflow: hidden;
        padding-bottom:0.1rem;
    }
    .con .bottom{
        width:100%;
        height: 20%;
        color:#616161;
        margin-left:0.2rem;
        font-size:13px;
        padding-bottom:0.1rem;
    }
</style>
