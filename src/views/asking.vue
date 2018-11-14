<template>
    <div id="askDetail">
        <Back msg="提问" />
      <textarea name="" id="" cols="50" rows="38" v-model="question"></textarea>
      <div class="commit">
          <p>{{error}}</p>
           <img @click="commit" src="@/assets/img/commit.png" alt="">
      </div>
    </div>
</template>
<script>
    import Back from '@/components/back.vue'
    export default{
        name:'askDetail',
        components:{Back},
        data(){
            return{
              uid:sessionStorage.getItem('uid'),
              question:'请输入您的问题...',
                error:'',
            }
        },
        methods:{
            commit(){
                if (this.question.length >= 12){
                    this.error = '';
                     fetch(`/ajax/asking?question=${this.question}&uid=${this.uid}`).then(function(e){
                         return e.text()
                     }).then((e)=>{
                         if (e =='ok'){
                             this.$router.push('/ask')
                         }else{
                             this.error = '提示：加载失败，请重新输入！'
                         }
                     })
                }else{
                    this.error = '提示：输入的问题不得小于12个字'
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
    textarea{
      width:100%;height:auto;color:#757575;letter-spacing: 1px;
      margin-top:1.2rem;outline: none;border:0;
    }
  .commit{
    width:100%;height:0.8rem;
    z-index: 99;
    background:#E6E6E6;position:fixed;bottom:0;left:0;
  }
  .commit img{
    width:0.6rem;height:0.6rem;float:right;margin-right:0.2rem;
    margin-top:0.1rem;
  }
    .commit p{
        float:left;font-size:0.3rem;color:red;
        line-height:0.8rem;text-indent: 1em;
    }
</style>