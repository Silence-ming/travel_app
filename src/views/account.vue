<template>
    <div class="account">
         <Back msg="账号设置" />
         <div class="box">
            <v-touch class="sel" tag="div" v-on:tap='rePassWord'>
                <img src="@/assets/img/pass.png" alt=""><span>密码修改</span>
            </v-touch>
         </div>
    </div>
</template>
<script>
  import Back from '@/components/back.vue'
  export default {
      components:{Back},
      data(){
          return{
          }
      },
      methods:{
          rePassWord(){
              this.$router.push('/rePassWord')
          }
      }
  }
</script>
<style scoped>
    .box{
        margin-top:1.2rem;
        width:100%;
        height:auto;
    }
    .box .sel {
        width:100%;height:1rem;font-size:14px;color:#757575;
        line-height: 0.9rem;border-bottom: 1px solid #F5F5F5;
        text-indent: 0.5em;
    }
    .sel img{
        display: block;
        width:1rem;height:1rem;
        float:left;
    }
    .sel span{
        display: block;
        width:3rem;height:1rem;
        line-height:1rem;
        float:left;
    }
</style>
