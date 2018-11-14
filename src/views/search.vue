<template>
    <div class="search">
        <Back msg="查询" />
         <div class="top" @click="search">
            <input type="text" placeholder="请输入城市名">
            <img src="@/assets/img/jing.png" alt="">
        </div>
        <div class="bottom">
           <p>热门推介</p>
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
        width:100%;height:0.8rem;
        margin-top:1.2rem;
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
        position: absolute;top:1.35rem;left:0.6rem;
    }
</style>