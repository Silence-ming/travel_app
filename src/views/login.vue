<template>
  <div class="box">
      <div class="title">
          <div class="top">
              <span>轻</span><span>游</span>
          </div>
          <div class="bottom">
              <div class="ztx"></div><span>一次说走就走的旅行</span><div class="ytx"></div>
          </div>
      </div>
      <div class="con">
          <div class="user">
              <img src="@/assets/img/user.png" alt="">
              <input type="text" placeholder="请在此处输入您的用户名" name="userName" v-model="userName" autocomplete="off" @keyup.enter="submit">
              <!--<span class="circle5" v-bind:style="tishi2"></span>-->
          </div>
          <div class="password">
              <img src="@/assets/img/pass.png" alt="">
              <input type="password" placeholder="请输入您的密码" name="password" v-model="password" @keyup.enter="submit">
              <!--<span class="circle5" v-bind:style="tishi3"></span>-->
              <div class="error" v-bind:style="mimatishi"><img src="@/assets/img/error.png" alt="" >账户和密码不一致</div>
          </div>
          <!--<div class="forget"><div class="circle"></div><a href="">忘记密码</a></div>-->
      </div>
      <button type="button" class="login" @click="submit" @keyup.enter="submit">立即登录</button>
      <router-link :to="{name:'reg'}" class="regus" tag="a"><span class="zbt"></span>还没加入轻游?&nbsp;&nbsp;注册加入我们<span class="ybt"></span></router-link>
  </div>
</template>

<script>
export default {
    name: 'login',
    data() {
        return {
            userName: "",
            password: "",
            mimatishi:{display:"none"},
            tishi3:{display:"none",background:"red"},
            tishi2:{display:"none",background:"red"},
        }
    },
    methods: {
        submit() {
             // this.$ajax({
             //     method:'post',
             //     url:'ajax/login/',
             //     data:{
             //         userName:this.userName,
             //         password:this.password,
             //     },
             //     success:function(data){
             //         console.log(data)
             //     },
             //     error:function(){
             //         alert('请求失败')
             //     }
             // })
            fetch(`/ajax/login/?userName=${this.userName}&password=${this.password}`)
            .then((res) => {
                return res.text()
            })
            .then((res) => {
                 if (res == "error") {
                    this.mimatishi.display="block"
                }else{
                    sessionStorage.setItem('uid',res);
                    sessionStorage.setItem('name',this.userName);
                    this.$router.push("/strategy")
                }
            })
        }
    }
}
</script>
<style scoped>
*{
    margin: 0;
    padding: 0;
    list-style: none;
}
a{
    text-decoration: none;
}
body{
    background: #fbfbfb;
}
.box{
    width: 100%;
}
.title{
    margin-top: 1.14rem;
    width: 100%;
    height: auto;
}
.top{
    text-align: center;
    font-size: 0.58rem;
    line-height: 0.58rem;
    /*方正粗圆简体*/
}
.top span:first-child{
    color: #5DD096;
}
.top span:last-child{
    color: #FFCE3C;
}
.bottom{
    font-size: 0.18rem;
    text-align: center;
    margin-top: 0.22rem;
    letter-spacing: 2px;
    position: relative;
}
.bottom .ztx{
    width: 0.28rem;
    height: 0.02rem;
    position: absolute;
    top: 0;bottom: 0;
    left: 2rem;
    margin: auto;
    background: -webkit-linear-gradient(left, #fff , #5DD096);
}
.bottom span{
    color: #BDBDBD;
}
.bottom .ytx{
    width: 0.28rem;
    height: 0.02rem;
    position: absolute;
    right: 2rem;
    top: 0;bottom: 0;
    margin: auto;
    background: -webkit-linear-gradient(left,  #5DD096,#fff)
}
.con{
    width: 5.84rem;
    margin:0 auto;
    margin-top: 0.8rem;
    height: 3.27rem;
    border-radius: 5px;
    box-shadow: 0 0 12px 6px #E8E8E8;
    background: white;
    position: relative;
    overflow: hidden;
}
.user,.password{
    width: 4.44rem;
    height: 0.4rem;
    display: flex;
}
.user{
    margin-top: 0.91rem;
    position: relative;
}
.password{
    margin-top: 0.52rem;
    position: relative;
}
.user input,.password input{
    border:none;
    border-bottom: 2px solid #E8E8E8;
    text-indent: 5px;
    padding-bottom: 1px;
    font-size: 0.22rem;
    width: 4.44rem;
    margin-left: 0.7rem;
    outline: none;

}
input::-webkit-input-placeholder{
    color: #E8E8E8;
    letter-spacing: 1px;
    font-size: 0.22rem;
    font-family: "苹方 粗体";
}
.user img,.password img{
    width: 1.02rem;
    height: 1.02rem;
    margin-top: -0.24rem;
    position: absolute;
}
.forget{
    width: 1.4rem;
    height: auto;
    margin-left: 4.37rem;
    margin-top: 0.34rem;
    display: flex;
    align-content: center;
}
.forget a{
    font-size: 0.22rem;
    font-family: "苹方 粗体";
    margin-left: 0.13rem;
    color: #000000;
    opacity: 0.4;
}
.circle{
    width: 0.18rem;
    height: 0.18rem;
    border-radius: 50%;
    margin: auto 0;
    background-color: deepskyblue;
    margin-top: 0.12rem;
}
.login{
    display: block;
    width: 2.8rem;
    height: 0.58rem;
    border-radius: 15pt;
    font-family: PingFangSC-Semibold, sans-serif;
    font-size: 12pt;
    color: #24f8b4;
    background: #D8FAF1;
    border: 1px solid #fff;
    margin: 0 auto;
    margin-top: 0.51rem;
    outline: none;
}
.regus{
    display: block;
    width: 100%;
    height: auto;
    font-size: 0.22rem;
    font-family: PingFangSC-Semibold, sans-serif;
    text-align: center;
    margin-top: 0.37rem;
    color: #BDBDBD;
    position: relative;
}
.regus .zbt{
    display: block;
    width: 0.15rem;
    height: 0.07rem;
    background: #FCE775;
    position: absolute;
    top: 0;bottom: 0;left: 1.9rem;
    margin: auto;
    border-radius: 0.05rem;
}
.regus .ybt{
    display: block;
    width: 0.15rem;
    height: 0.07rem;
    background: #FCE775;
    position: absolute;
    top: 0;bottom: 0;right: 1.9rem;
    margin: auto;
    border-radius: 0.05rem;
}
.error{
    width: 2.96rem;
    height: 0.5rem;
    border-radius: 0.3rem;
    box-shadow: 0 0 6px 2px #E8E8E8;
    font-size: 0.22rem;
    color: red;
    position: absolute;
    left: 0.8rem;
    top: 0.36rem;
    line-height: 0.5rem;
    text-indent: 0.6rem;
}
.error img{
    position: absolute;
    width: 0.6rem;
    height: 0.6rem;
    top: 0.24rem;
    left: -0.46px;
}
.user span,.password span{
    display: block;
    width: 0.13rem;
    height: 0.13rem;
    border-radius: 50%;
    background: red;
    position: absolute;
    top: 0.1rem;
    right: 0.3rem;
    margin: auto;
}
</style>
