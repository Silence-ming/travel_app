<template>
    <div id="noteDetail">
        <Back msg="游记"/>
        <div class="con">
            <p class="head">旅行的自拍，一是带自己，二是带风景，</p>
            <div class="content">
                <img src="@/assets/img/111.jpg" alt="">
                <p class="text">一个人的旅行，因为随心随性，不用管别人的喜好，无论看到怎样的景色或瞬间，让自己眼前一亮，或内心一动的画面，马上拍下来。</p>
                <img src="@/assets/img/1.jpg" alt="">
                <p class="text">一个人的旅行，因为随心随性，不用管别人的喜好，无论看到怎样的景色或瞬间，让自己眼前一亮，或内心一动的画面，马上拍下来。</p>
                <img src="@/assets/img/1111.jpg" alt="">
                <p class="text">一个人的旅行，因为随心随性，不用管别人的喜好，无论看到怎样的景色或瞬间，让自己眼前一亮，或内心一动的画面，马上拍下来。</p>
            </div>
        </div>
    </div>
</template>
<script>
    import Back from '@/components/back.vue'
    export default{
        name:'noteDetail',
        components:{Back},
        data(){
            return{

            }
        },
        methods:{

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
    .con{
         width:100%;height:auto;margin-top:1.2rem;
    }
     .con .head{
        width:100%;height:0.5rem;
         font-size:16px;font-weight:600;
    }
     .con .content{
         width:100%;height:auto;margin-top:0.2rem;
         font-size:14px;color:#757575;
    }
    .content img{
        margin-top:0.1rem;width:100%;height:3rem;
    }
    .content .text{
        width:100%;height:auto;margin-top:0.1rem;
    }
</style>