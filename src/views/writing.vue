<template>
    <div id="askDetail">
        <Back msg="写游记" />
        <textarea name="" id="" cols="50" rows="38" v-model="note" placeholder="将您的经历写下来吧...">
        </textarea>
        <div class="imgs">
            <div class="img" v-for="img in imgs">
                <img :src="img" alt="">
            </div>
        </div>
      <div class="commit">
           <img @click="commit" src="@/assets/img/commit.png" alt="">
           <img  class='addImage' src="@/assets/img/addImage.png" alt="" @click.stop="uploadHeadImg">
          <input type="file" accept="image/*" @change="handleFile" class="hiddenInput"/>
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
                error:'',
                imgs:[],
                img_files:'',
                note:''
            }
        },
        methods:{
            uploadHeadImg: function () {
                this.$el.querySelector('.hiddenInput').click()
            },
            handleFile: function (e) {
                let $target = e.target || e.srcElement;
                let file = $target.files[0];
                var reader = new FileReader();
                reader.onload = (data) => {
                     let res = data.target || data.srcElement;
                     this.imgs.push(res.result);
                     this.img_files = file
                };
                reader.readAsDataURL(file)
            },
             commit(){
                 if (this.note.length >=20){
                     this.error = '';
                     var form = new FormData();
                     form.append('uid',this.uid);
                     form.append('note',this.note);
                     form.append('img_files',this.img_files);
                     this.axios.post('/ajax/writing',form)
                         .then((e)=>{
                             this.$router.push('/notes')
                         })
                         .catch((error)=>{
                              this.error = '提示：加载失败，请重新输入！'
                         })
                 }else{
                     this.error = '提示：输入的内容不得少于20个字'
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
    .imgs{
        width:100%;;
        height:auto;
        padding-bottom:2rem;
        overflow: hidden;
    }
    .imgs img{
        width:2rem;height:1rem;margin-top:0.2rem;
        margin-left:0.2rem;float:left;
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
   .commit .addImage{
        float:right;margin-left:0.2rem;
    }
    .commit p{
    float:left;font-size:0.3rem;color:red;
    line-height:0.8rem;text-indent: 1em;
}
</style>