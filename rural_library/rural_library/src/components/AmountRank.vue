<template>
  <div
    class="echart"
    ref="AmountRank"
    id="AmountRank"
    :style="{ float: 'center', width: '100%', height: '260px' }"
  ></div>
</template>

<script>
import * as echarts from "echarts";
import bus from 'vue3-eventbus';
import { markRaw } from 'vue'

export default {
  data() {
    return {
      name: "AmountRank",
      AmountRank: {},
      option : {
        tooltip: {},
        legend: {
          data: ["书目数量"]
        },
        xAxis: {
          data: []
        },
        yAxis: {},
        series: [
          {
            name: "书目数量",
            type: "bar", //类型为柱状图
            data: []
          }
        ]
      },
      bookName: [],
      bookData: [],
    };
  },
  mounted() {
    this.initEcharts();
    bus.on('province', this.updateAmountRank) 
  },
  methods: {
    initEcharts() {
      const option = {
        tooltip: {},
        legend: {
          data: ["书目数量"]
        },
        xAxis: {
          data: []
        },
        yAxis: {},
        series: [
          {
            type: "bar", //类型为柱状图
            name: "书目数量",
            data: []
          }
        ]
      };
      this.AmountRank = markRaw(echarts.init(document.getElementById("AmountRank")));// 图标初始化
      this.AmountRank.setOption(option);// 渲染页面
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        this.AmountRank.resize();
      });
    },

    updateAmountRank(provinceAndlibData ) 
    {
      // console.log("AmountRank Received" , provinceAndlibData.province.data,provinceAndlibData.libData);
      // console.log(this.option); console.log(this.bookName);
      // update bookName and bookData

      let libraryName = [];
      let bookAmount = [];
      
      for(let key in provinceAndlibData.libData)
      {
        //有数据代码
        //libraryName.push(provinceAndlibData.libData[key].libraryName);
        //bookAmount.push(provinceAndlibData.libData[key].bookAmount);
      }

      this.option.xAxis.data = libraryName;
      this.option.series[0].data = bookAmount;
      this.AmountRank.setOption(this.option , true);
    }
    
  }
};
</script>