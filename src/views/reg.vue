<template>
    <div class="box">
        <div class="title">
            <div class="top">
                <span>轻</span><span>游</span>
            </div>
            <div class="bottom">
                <div class="ztx"></div><span>来一场所走就走的旅行</span><div class="ytx"></div>
            </div>
            <div class="quan">
                <div class="circle3">
                    <div class="mini"></div>
                </div>
                <div class="circle4">
                </div>
            </div>
        </div>
        <div class="con">
            <div class="user">
                <img src="@/assets/img/user.png" alt="">
                <input type="text" placeholder="请在此处输入您的用户名" name="userName" v-model="userName" autocomplete="off">
                <span class="circle5" v-bind:style="tishi2"></span>
                <div class="error" v-bind:style="objstyle"><img src="@/assets/img/error.png" alt="">用户已存在</div>
                <div class="error" v-bind:style="objstyle2"><img src="@/assets/img/error.png" alt="">用户名称不符合规范</div>
            </div>
            <div class="password">
                <img src="@/assets/img/pass.png" alt="">
                <input type="password" placeholder="请输入您的密码" name="password" v-model="password">
                <span class="circle5" v-bind:style="tishi"></span>
                <div class="error" v-bind:style="mimatishi"><img src="@/assets/img/error.png" alt="">密码需要至少6位</div>
            </div>
            <div class="password2">
                <img src="@/assets/img/pass.png" alt="">
                <input type="password" placeholder="请再次确认您的密码" name="password1" v-model="password1">
                <span class="circle5" v-bind:style="tishi3"></span>
                <div class="error" v-bind:style="pipei"><img src="@/assets/img/error.png" alt="" >俩次密码不一致</div>
            </div>
        </div>
        <button type="button" class="join" @click="submit">加入轻游</button>
        <div class="tiaokuan">已有轻游账号？请点击 <span @click="returnlogin" class="returnlogin">这里</span></div>
    </div>
</template>

<script>
    export default {
        name: "reg",
        data(){
            return{
                userName:"",
                password:"",
                password1:"",
                objstyle:{display:"none"},
                pipei:{display:"none"},
                tishi:{display:"none",background:"red"},
                mimatishi:{display:"none"},
                tishi2:{display:"none",background:"red"},
                objstyle2:{display:"none"},
                tishi3:{display:"none",background:"red"},
            }
        },
        watch:{
             password:function () {
                 this.mimatishi.display="block"
                 this.tishi.display="block"
                 if(this.password.length>5){
                     this.tishi.background="green"
                     this.mimatishi.display="none"
                 }else if (this.password.length<6){
                     this.tishi.background="red"
                 }
             },
             userName:function () {
                 this.tishi2.display="block"
                 var reg=/^[a-zA-Z]+\w$/
                 var result=reg.test(this.userName)
                 if(result==true){
                     this.tishi2.background="green"
                     this.objstyle2.display="none"
                 }else {
                     this.tishi2.background="red"
                     this.objstyle2.display="block"
                 }
             },
             password1:function () {
                 this.tishi3.display="block"
                 this.pipei.display="block"
                 if (this.password==this.password1) {
                     this.tishi3.background="green"
                     this.pipei.display="none"
                 }
             }
        },
        methods:{
             returnlogin(){
                this.$router.push('/login/')
            },
            submit() {
            fetch(`/ajax/reg/?userName=${this.userName}&password=${this.password}&password1=${this.password1}`).then((res) => {
                return res.text()
            }).then((res)=>{
               if (res=="ok"){
                    this.$router.push("/login")
                }
                else if(res=="cunzai"){
                    this.objstyle.display="block"
                    this.$router.push("/reg")
                }
                else if (res=="no") {
                    this.pipei.display="block"
                    this.$router.push("/reg")
                }
            })
        }
        }
    }
//    俩个密码验证通过后台，用户存在与否验证通过后台。用户格式通过前台验证。
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
.returnlogin{
    color:#5BCCF7;
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
    margin-top: 0.58rem;
    height: 3.56rem;
    border-radius: 5px;
    box-shadow: 0 0 12px 6px #E8E8E8;
    background: white;
    position: relative;
    overflow: hidden;
}
.user,.password,.password2{
    width: 4.44rem;
    height: 0.4rem;
    display: flex;
}
.user{
    margin-top: 0.87rem;
}
.password{
    margin-top: 0.52rem;
}
.password2{
    margin-top: 0.52rem;
}
.user input,.password input,.password2 input{
    border:none;
    border-bottom: 2px solid #E8E8E8;
    text-indent: 5px;
    padding-bottom: 1px;
    font-size: 0.22rem;
    width: 4.44rem;
    margin-left: 0.7rem;
    outline: none;
}
.user,.password,.password2{
    position: relative;
}
.user span,.password span,.password2 span{
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
input::-webkit-input-placeholder{
    color: #E8E8E8;
    letter-spacing: 1px;
    font-size: 0.22rem;
    font-family: "苹方 粗体";
}
.user img,.password img,.password2 img{
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
    font-family: PingFangSC-Semibold, sans-serif;
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
.join{
    display: block;
    width: 2.8rem;
    height: 0.58rem;
    border-radius: 15pt;
    font-family: PingFangSC-Semibold, sans-serif;
    font-size: 12pt;
    color: #fff;
    background: #D8FAF1;
    border: 1px solid #fff;
    margin: 0 auto;
    margin-top: 0.51rem;
    background: -webkit-linear-gradient(left,  #72f0d2,#5beabb)
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
.tiaokuan{
    width: 100%;
    height: auto;
    font-size: 0.2rem;
    text-align: center;
    margin-top: 0.23rem;
    position: relative;
    color:#BDBDBD;
}
.circle2{
    display: block;
    width: 0.15rem;
    height: 0.15rem;
    border-radius: 50%;
    background: #72f0d2;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 1.8rem;
    margin: auto;
}
.quan{
    width: 100%;
    height: auto;
    display: flex;
    justify-content: center;
    margin-top: 0.64rem;
}
.circle4{
    width: 0.13rem;
    height: 0.13rem;
    border-radius: 50%;
    background: #75FBBF;
    margin-top: 0.05rem;
    margin-left: 0.3rem;
}
.circle3{
    width: 0.22rem;
    height: 0.22rem;
    border-radius: 50%;
    background-color: #C5FBE3;
    display: flex;
    justify-content: center;
    align-items: center;
}
.circle3 .mini{
    width: 0.08rem;
    height: 0.08rem;
    border-radius: 50%;
    border: 0.02rem double #75FBBF;
    background: white;
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
</style>