<template>
    <div id="noteDetail">
        <Back msg="游记"/>
        <div class="con">
            <p class="head">{{title}}</p>
            <div class="content" v-for="note_detail in note_details">
                <p class="text">&nbsp;&nbsp;&nbsp;&nbsp;{{note_detail.note}}</p>
                <img :src="note_detail.img_url" alt="">
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
                note_details:[],
                title:this.$route.params.title,
            }
        },
        mounted(){
            var nid =this.$route.params.id;
          fetch('/ajax/note_detail/?nid='+nid)
              .then(function(e){
              return e.text()
            })
              .then((e)=>{
                  var obj = JSON.parse(e);
                  obj['img_urls'] = obj['img_urls'].split(',');
                  obj['note'] = obj['note'].split('|');
                  for(var i in obj['img_urls']){
                      var note_detail = {};
                      note_detail['img_url'] = obj['img_urls'][i];
                      if (obj['note'][i]){
                          note_detail['note'] = obj['note'][i];
                      }
                      this.note_details.push(note_detail)
                  }
              })
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
        width:100%;height:1rem;
         font-size:16px;font-weight:600;
    }
     .con .content{
         width:100%;height:auto;margin-top:0.4rem;
         font-size:14px;color:#757575;letter-spacing: 1px;
    }
    .content img{
        margin-top:0.1rem;width:100%;height:4.5rem;
    }
    .content .text{
        width:100%;height:auto;margin-top:-0.2rem;
    }
</style>