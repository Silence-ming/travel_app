<template>
    <div id="askDetail">
        <Back :msg="question" />
      <textarea name="" id="" cols="50" rows="38" v-model="answer"></textarea>
      <div class="commit">
           <img @click="commit" src="@/assets/img/commit.png" alt="">
          <p>{{error}}</p>
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
                qid:this.$route.params.id ,
                answer:'请在此输入内容...',
                error:''
            }
        },
        computed:{
          question(){
              var question = this.$route.params.question;
              if (question.length >= 12){
                  return question.slice(0,12)+'...'
              }else{
                  return question
              }
            }
        },
        methods:{
            commit(){
                 if (this.answer.length >=20){
                     this.error = '';
                     fetch(`/ajax/answer?qid=${this.qid}&answer=${this.answer}&uid=${this.uid}`).then(function(e){
                         return e.text()
                     }).then((e)=>{
                         if (e =='ok'){
                             this.$router.push(`/askDetail/${this.qid}`)
                         }else{
                             this.error = '提示：加载失败，请重新输入！'
                         }
                     })
                 }else{
                     this.error = '提示：输入的答案不得少于20个字'
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
    .hiddenInput{
        display: none;
    }
    textarea{
      width:100%;height:9.5rem;color:#757575;letter-spacing: 1px;
      margin-top:1.2rem;outline: none;border:0;overflow:scroll;
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