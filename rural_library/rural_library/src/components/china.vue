<template>
    <div id="main"></div>
</template>
<script>

import * as echarts from 'echarts';
import bus from 'vue3-eventbus';
import axios from 'axios'
import { provinceAndCityData } from 'element-china-area-data';

const chinaJson = require('../utils/china.json');
export default {
  data() {
    return {
      myChart: null,
      dataList: [
        { name: "南海诸岛" },
        { ename: "beijing", name: "北京"},
        { ename: "tianjin", name: "天津" },
        { ename: "shanghai", name: "上海" },
        { ename: "chongqing", name: "重庆" },
        { ename: "hebei", name: "河北" },
        { ename: "henan", name: "河南"},
        { ename: "yunnan", name: "云南" },
        { ename: "liaoning", name: "辽宁" },
        { ename: "heilongjiang", name: "黑龙江" },
        { ename: "hunan", name: "湖南"},
        { ename: "anhui", name: "安徽" },
        { ename: "shandong", name: "山东" },
        { ename: "xinjiang", name: "新疆" },
        { ename: "jiangsu", name: "江苏" },
        { ename: "zhejiang", name: "浙江" },
        { ename: "jiangxi", name: "江西" },
        { ename: "hubei", name: "湖北" },
        { ename: "guangxi", name: "广西"},
        { ename: "gansu", name: "甘肃" },
        { ename: "shanxi", name: "山西" },
        { ename: "neimenggu", name: "内蒙古" },
        { ename: "shanxi1", name: "陕西" },
        { ename: "jilin", name: "吉林" },
        { ename: "fujian", name: "福建" },
        { ename: "guizhou", name: "贵州" },
        { ename: "guangdong", name: "广东" },
        { ename: "qinghai", name: "青海" },
        { ename: "xizang", name: "西藏" },
        { ename: "sichuan", name: "四川" },
        { ename: "ningxia", name: "宁夏" },
        { ename: "hainan", name: "海南" },
        { name: "台湾"},
        { ename: "xianggang", name: "香港" },
        { ename: "aomen", name: "澳门" },
      ],
    };
  },


  methods: {
    initEchart() {

      // let dataList = this.dataList;
      // // 随机生成数据，此后该数据应当由后端返回

      // for(let i = 0; i < dataList.length; i++){
      //     dataList[i].value = Math.ceil(Math.random() * 1000 - 1);
      // }

      echarts.registerMap('china', chinaJson);
      // 基于准备好的dom，初始化echarts实例
      this.myChart = echarts.init(document.getElementById('main'));
      var option = {
        tooltip: {
          //数据格式化
          formatter: function(params, callback) {
            return (
              params.seriesName + "<br />" + params.name + "：" + params.value
            );
          },
        },
        visualMap: {
          min: 0,
          max: 1000,
          left: "left",
          top: "bottom",
          text: ["高", "低"], //取值范围的文字
          inRange: {
            color: ["#d0e5f2", "#67a3d7"], //取值范围的颜色
          },
          show: true, //图注
        },
        geo: {
          map: 'china', //引入地图数据
          roam: false, //不开启缩放和平移
          zoom: 1, //视角缩放比例
          label: {
            normal: {
              show: true,
              fontSize: "10",
              color: "rgba(0,0,0,0.7)",
            },
          },
          itemStyle: {
            normal: {
              borderColor: "rgba(0, 0, 0, 0.2)",
            },
            emphasis: { //高亮的显示设置
              areaColor: "skyblue", //鼠标选择区域颜色
              shadowOffsetX: 0,
              shadowOffsetY: 0,
              shadowBlur: 20,
              borderWidth: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
          },
        },
        // 鼠标悬浮提示框
        series: [
          {
            name: "省份",
            type: "map",
            geoIndex: 0,
            data: this.dataList,
          },
        ],
      };
      this.myChart.setOption(option);

      //鼠标悬浮事件
      this.myChart.on("mouseover",function(params){
        //console.log(params)  //这里的params是鼠标悬浮的图表节点的数据
      })
      
      //鼠标点击事件
      this.myChart.on("click",function(params){
        //axios.post('http://127.0.0.1:4523/m2/3164066-0-default/103433132', {
          axios.post('https://mock.apifox.cn/m1/3175907-0-default/provinceName', {
          name: params.name,
          ename: params.ename
        })
        .then(function (response) {
          console.log("Mouse Clicked Sccessfully",response.data);
          bus.emit('province', {province:params , libData:response.data});
        })
        .catch(function (error) {
          console.log(error);
        });

        //console.log(params)  //这里的params是鼠标点击的图表节点的数据
      })
    },
  },
  mounted() {

    
    //axios.get('http://127.0.0.1:4523/m2/3164066-0-default/103528141')
    axios.get('https://mock.apifox.cn/m1/3175907-0-default/')
    .then((response) => {
      
      // console.log("1",this.dataList);
      // console.log("China Map Info Received Successfully" , response.data);
      let i = -1;
      for (let key in response.data) {
          i++;
          //this.dataList[i] = response.data[key];
          this.dataList[i] = 0;
      };
      // console.log("2",this.dataList);
      this.initEchart();
      // console.log("3",this.dataList);
    });

  },
}
</script>
<style scoped>
#main {
    min-height: 450px;
    min-width : 600px;
    margin: auto;
    background-color: transparent;
}
</style>


