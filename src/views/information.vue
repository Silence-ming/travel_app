<template>
  <div class="about">
      <Back msg="个人信息" />
      <v-touch class="commits" tag="p" v-on:tap="commits" :class="{opacity:flag == 0}" >保存</v-touch>
      <div class="box">
          <div class="head">
              <span>头像</span>
              <img :src="head" alt="" @click.stop="uploadHeadImg">
              <input type="file" accept="image/*" @change="handleFile" class="hiddenInput"/>
          </div>
          <div class="name">
              <span >昵称</span>
              <input v-model="uname" class="names" @change="handleChange">
          </div>
          <div class="note">
              <span>个性签名</span>
              <input v-model="note" class="notes" @change="handleChange">
          </div>
          <p class="notice">
              {{notice}}
          </p>
          <p class="errors">
              {{error}}
          </p>
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
              head:'',
              img_file:"",
              uname:'',
              note:'',
              newName:'',
              newNote:'',
              flag:0,
              error:'',
              notice:'昵称长度不超过10，个性签名长度不超过30',
          }
      },
      watch:{
          uname:function(newName,oldName){
              this.newName = newName
          },
          note:function(newNote,oldNote){
               this.newNote = newNote
          }
      },
        mounted(){
          fetch('ajax/information/?uid='+this.uid).then(function(e){
              return e.text()
          }).then((e)=>{
              this.head=JSON.parse(e)['head'];
              this.uname=JSON.parse(e)['uname'];
              this.note=JSON.parse(e)['note'];
          });
        },
      methods:{
        uploadHeadImg() {
            this.$el.querySelector('.hiddenInput').click();
        },
        handleFile(e) {
            let $target = e.target || e.srcElement;
            let file = $target.files[0];
            var reader = new FileReader();
            reader.onload = (data) => {
                 let res = data.target || data.srcElement;
                 this.head = res.result;
                 this.img_file = file
            };
            reader.readAsDataURL(file);
            this.error = '';
            this.flag = 1;
        },
        handleChange(){
          this.error = '';
          this.flag = 1
        },
          commits(){
            if (this.flag == 1){
                if (this.newName.length <= 10 && this.newNote.length <=30){
                    var form = new FormData();
                    form.append('name',this.newName);
                    form.append('note',this.newNote);
                    form.append('uid',this.uid);
                    form.append('img_file',this.img_file);
                    this.axios.post('/ajax/update_info',form)
                        .then((e)=>{
                            this.$router.push('/person')
                         })
                        .catch((error)=>{
                                  this.error = '提示：加载失败，请重新输入！'
                         })
                }else{
                    this.error = '输入内容过长，请重新输入'
                }
            }

          },
      }
  }
</script>
<style scoped>
.box{
    width:100%;
    height:5rem;
    margin-top:1.2rem;
    font-size:15px;
}
    .errors,.notice{
        width:100%;
        height:0.5rem;
        margin-top:0.2rem;
        margin-left:0.2rem;
        color:red;border-bottom: 0px solid #fff;
    }
    .box div{
        width:100%;
        height:1.2rem;
        border-bottom:1px solid #000;
    }
    .hiddenInput{
        display: none;
    }
    div span:first-child{
        display: block;
        float:left;
        padding:0.1rem;
        margin-top:0.5rem;
    }
     div span:last-child{
        display: block;
        float:right;
        padding:0.1rem;
         margin-top:0.5rem;
    }
     .head img{
        display: block;
        float:right;
        width:0.8rem;
         height:0.8rem;
         border-radius:50%;
         margin-top:0.2rem;
    }
    .notes,.names{
        width:5rem;
        height:0.5rem;
        overflow: hidden;
        text-align:right;
        outline: none;
        border:0;
        margin-top:0.5rem;
        margin-left:0.7rem;
    }
    .names{
        margin-left:1.3rem;
    }
    .commits{
        font-size:15px;
        position:fixed;
        top:.1rem;right:.6rem;
        color:#5ABFED;
        z-index: 99;
    }
    .notice{
        color:#ccc;
    }
    .opacity{
        opacity: .5;
    }
</style>