<template>
    <div class="box">
        <div class="title">
            <div class="top">
                <span>轻</span><span>游</span>
            </div>
            <div class="bottom">
                <div class="ztx"></div><span>来一场所走就走的旅行</span><div class="ytx">
            </div>
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
                <input type="text" placeholder="用户名" name="userName" v-model="userName" autocomplete="off" @change="inputChange" @keyup.enter = 'submit'>
            </div>
            <div class="password">
                <img src="@/assets/img/pass.png" alt="">
                <input type="password" placeholder="密码" name="password" v-model="password" @change="inputChange" @keyup.enter = 'submit'>
            </div>
            <div class="password2">
                <img src="@/assets/img/pass.png" alt="">
                <input type="password" placeholder="确认密码" name="password1" v-model="password1" @change="inputChange" @keyup.enter = 'submit'>
            </div>
            <div class="sign">
                <p>
                    <span>提示：</span>
                    用户名为字母开头，2-8位；<br>
                    密码为6-18位，至少包含一个大写字母、数字、特殊字符
                </p>
            </div>
            <div class="error">
                <p>{{error}}</p>
            </div>
        </div>
        <button type="button" class="join" @click="submit">加入轻游</button>
        <div class="tiaokuan">
            已有轻游账号？请点击
            <span @click="returnlogin" class="returnlogin">这里</span>
        </div>
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
                error:'',
            }
        },
        methods:{
            inputChange(){
              this.error = '';
            },
             returnlogin(){
                this.$router.push('/login/')
            },
            submit() {
                 let reg =/^(?=.*[A-Z])(?=.*[0-9])(?=.*[~!@&%$^#_.])[A-Za-z0-9~!@&%$^#_.]{8,16}$/;
                if (this.password == this.password1 && reg.test(this.password) ==true){
                    fetch(`/ajax/reg/?userName=${this.userName}&password=${this.password}&password1=${this.password1}`)
                     .then((res) => {
                        return res.text()
                    })
                    .then((res)=>{
                        if (res == 'exit'){
                            this.error = '用户名已存在'
                        }else if(res == 'ok'){
                            this.$router.push('/login')
                        }
                    })
                    .catch(function(){
                        alert('网络连接错误')
                    })
                }else if(this.password !=this.password1) {
                    this.error = '两次密码不一致，请重新输入';
                }else if (reg.test(this.password) == false){
                    this.error = '密码不符合规则，请重新输入'
                }
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
    height: 5.5rem;
    border-radius: 5px;
    box-shadow: 0 0 12px 6px #E8E8E8;
    background: white;
    position: relative;
    overflow: hidden;
}
.con .sign{
    width:5rem;height:auto;margin-top:.2rem;
    font-size:14px;color:#ccc;
    line-height:.4rem;margin-left:.4rem;
}
.con .error{
    width:100%;height:auto;margin-top:.2rem;
    font-size:14px;color:red;
    text-align: center;
}
.sign span{
    color:#FCE775;
}
.user,.password,.password2{
    width: 100%;
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
    outline:none;
    background: -webkit-linear-gradient(left,  #72f0d2,#5beabb)
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
</style>