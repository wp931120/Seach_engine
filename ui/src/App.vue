<template>
<div style="margin-top: 15px;">
  <el-input placeholder="请输入内容" v-model="input" class="input-with-select">
    <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
  </el-input>
<ul>
  <li  v-for="item in message" >
     <p v-html = "item._source.title"></p>
      <p v-html = "item._source.content"></p>
  </li>
  </ul>
</div>

</template>

<script>
export default {
  name: 'App',
  data(){
    return{
      input :" ",
      message: [],
      title:"",
      content:"",
    }
  },
  methods : {
    search : function(){
       let input = this.input
       let data = {"data":input}
       this.$axios.post("http://localhost:5000/search",this.$qs.stringify(data))
            .then((response)=>{
              this.message = response.data["data"]
              console.log(response.data)
         }).catch(function(res){
               console.log(res)
         })
        }
      },
      
      
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
