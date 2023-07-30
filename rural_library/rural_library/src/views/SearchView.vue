<template>
    <div id="app">
      <div class="search">
        <el-space wrap>
        所在地
        <el-cascader
          size="large"
          :options="provinceAndCityData"
          v-model="selectedOptions">
        </el-cascader>
        <el-button type="primary" color="#9c8e60" plain @click="showInfo">查询</el-button>
      </el-space>
      <br>

      <div class="hidden">
      <div class="info">
      <el-space direction="vertical" size="large">
        <el-card v-for="(item, index) in list " :key="index" shadow="hover" style="width: 800px" @click="showDetail(item)">
          <div class="card">
            <img class="graph" :src=item.avatar>
            <div class="text">
              <p>书屋名称：{{ item.name }}</p>
              <p>书屋地点：{{ item.place }}</p>
              <p>致电：{{ item.telephone }}</p>
            </div>
          </div>
        </el-card>
      </el-space>
      </div>
      </div>
      </div>
    </div>

  </template>
  
  <script >
    import { provinceAndCityData } from 'element-china-area-data'
    export default {
      data () {
        return {
          list: [],
          provinceAndCityData,
          selectedOptions: [],
        }
      },

      methods: {
        showDetail(item){
          var oCard = document.querySelector('.info');
        },
        showInfo(){
          var myHeaders = new Headers();
          myHeaders.append("User-Agent", "Apifox/1.0.0 (https://apifox.com)");
          myHeaders.append("Accept", "*/*");
          myHeaders.append("Host", "mock.apifox.cn");
          myHeaders.append("Connection", "keep-alive");
          var prvc= this.selectedOptions[0];
          var city= this.selectedOptions[1];
          var requestOptions = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow',
          };

          fetch(`https://mock.apifox.cn/m1/2827678-0-default/library/${prvc}/${city}`, requestOptions)
          .then(response => response.json())
          .then(result => {
            console.log(result);
            this.list = result;
          })
          .catch(error => console.log('error', error));
        }
      }

    }
  </script>

<style scoped>
    #app{
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      background-image: url(../assets/net_background.png);
      background-size:100% 100%;
      background-attachment: fixed;
    }
    .search {
      top: 70px;
      right: 0;
      left: 0;
      position: absolute;
    }
    .info {
      position: absolute;
      top: 0;
      right: -17px;
      left: 0;
      bottom: 0;
      overflow-y: scroll;
      overflow-x: hidden;
    }
    .card {
      cursor: pointer;
      display: flex;
      margin-left: 10px;
    }
    p {
      text-align: left;
      margin: 5px;
    }
    .text {
      margin-left: 10px;
      width: 800px;
      background-color :#f0e2b5; 
      display: flex;
      flex-direction:column;
    }
    .hidden {
      position: fixed;
      top: 140px;
      right: 20px;
      left: 20px;
      bottom: 20px;
      overflow: hidden;
    }
</style>