<template>
  <div class="about">
      <Back msg="关于轻游"/>
      <div class="box">
          <div class="title">版权声明</div>
          <p>

1、所有来源版权均为本站所有，若您需要引用、转载，只需要注明来源及原文链接即可，如涉及大面积转载，请来信告知，获取授权。<br>

2、本站所提供的文章资讯、软件资源、素材源码等内容均为第三方作者提供、网友推荐、互联网整理而来（部分报媒/平媒内容转载自网络合作媒体），仅供学习参考，如有侵犯您的版权，请联系我们，本站将在三个工作日内改正。<br>

3、若您的网站或机构从本站获取的一切资源进行商业使用，除来源为本站的资料需与本站协商外，其他资源请自行联系版权所有人。<br>

4、最模板不保证资源的准确性、安全性和完整性，请您在阅读、下载及使用过程中自行确认，本站亦不承担上述资源对您或您的网站造成的任何形式的损失或伤害。 <br>

5、未经最模板允许，不得盗链、盗用本站资源；不得复制或仿造本网站，不得在本站所属的服务器上建立镜像，最模板对其自行开发的或和他人共同开发的所有内容、技术手段和服务拥有全部知识产权，任何人不得侵害或破坏，也不得擅自使用。<br>

6、互联网的本质是自由与分享，我们真诚的希望，每一份有价值的正能量能够在互联网中自由传播，能够为每一个企业提供发展动力。
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

          }
      }
  }
</script>
<style scoped>
.box {
    width:100%;height:auto;margin-top:1.2rem

}
    .box .title{
        width:100%;
        font-size:18px;
        text-align:center;
    }
    .box p{
        width:100%;height:auto;
        font-size:15px;
        line-height:0.5rem;
    }
</style>