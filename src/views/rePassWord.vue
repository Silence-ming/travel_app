<template>
    <div class="rePassWord">
         <Back msg="密码修改" />
         <div class="box">
             <div>
                  <label>请输入旧密码：</label>
                 <input type="password" v-model="oldPassWord" @change="handleChanges"><br>
             </div>
           <div>
                 <label>请输入新密码 <span>(6-18位，至少包含一个大写字母、数字、特殊字符)</span>：</label>
                 <input type="password" v-model="newPassWord" @change="handleChanges"><br>
           </div>
            <div>
                 <label>请再次输入新密码 <span>（两次密码需一致）</span>：</label><br>
                 <input type="password" v-model="newPassWord1" @change="handleChanges">
            </div>
             <v-touch tag="div" v-on:tap="commits" class="commit">提交</v-touch>
             <p class="error">{{error}}</p>
         </div>
    </div>
</template>
<script>
  import Back from '@/components/back.vue'
  export default {
      components:{Back},
      data(){
          return{
              uid:sessionStorage.getItem('uid'),
              oldPassWord:null,
              newPassWord:null,
              newPassWord1:null,
              error:'',
          }
      },
      methods:{
          handleChanges(){
             this.error = '';
          },
          commits(){
              let reg =/^(?=.*[A-Z])(?=.*[0-9])(?=.*[~!@&%$^#_.])[A-Za-z0-9~!@&%$^#_.]{8,16}$/;

                if (this.newPassWord == this.newPassWord1 && this.newPassWord !=this.oldPassWord && reg.test(this.newPassWord) ==true){
                    fetch(`/ajax/rePassWord?uid=${this.uid}&oldPassWord=${this.oldPassWord}&newPassWord=${this.newPassWord}`).then(function(e){
                        return e.text()
                    }).then((e)=>{
                        if (e == 'yes'){
                            this.$router.back()
                        }else{
                            this.error = '旧密码输入有误，请从新输入'
                        }
                    })
                }else if(this.newPassWord ==this.oldPassWord) {
                    this.error = '旧密码不能与新密码一致，请重新输入';
                }else if(this.newPassWord !=this.newPassWord1) {
                    this.error = '两次密码不一致，请重新输入';
                }else if (reg.test(this.newPassWord) == false){
                    this.error = '新密码不符合规则，请重新输入'
                }
          }
      }
  }
</script>
<style scoped>
    *{
        margin:0;padding:0;
    }
    .box{
        margin-top:1.2rem;
        width:100%;
        height:auto;
    }
    label{
        font-size:15px;
    }
    .box input{
        width:100%;
        height:0.8rem;
        border:0;outline:0;
        border-bottom:1px solid #000;
        margin-top:0;
    }
    .commit{
       font-size:15px;
        position:fixed;
        top:.3rem;right:.6rem;
        color:#5ABFED;
        z-index: 99;
    }
    .error{
        width:4rem;height:.7rem;
        font-size:14px;margin-top:.5rem;
        line-height:.7rem;float:left;
        margin-left:.2rem;color:red;
    }
    label span{
        color:#A5A5A5;
    }
</style>
