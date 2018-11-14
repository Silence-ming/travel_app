<template>
    <div id="detail">
        <div class="back">
            <img src="@/assets/img/back.png" alt="" @click="back">
            <h1>{{msg}}</h1>
        </div>
    </div>
</template>
<script>
    export default{
        name:'Back',
        props: {
            msg: String
          },
        methods:{
            back(){
                this.$router.back()
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
    .back{
        width:100%;
        height:1rem;
        background:#E6E6E6;
        position:fixed;top:0;left:0;
        z-index: 99;
    }
    .back img{
        width:0.7rem;
        height:0.5rem;
        margin-top:0.15rem;
        margin-left:0.1rem;float:left;
    }
    .back h1{
        font-size: 20px;float:left;margin-left:0.5rem;line-height: 0.8rem;
    }
</style>