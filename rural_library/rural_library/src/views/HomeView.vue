<template>
  <div class="home">
    <div>
      <h1 class="head">全国农家书屋统计数据</h1>
    </div>

    <div class="image-layout">
      
      <div class="left-image">
        <!-- ref = "mapContainer" -->
        A
      </div>

      <div class="right-images">
        <div class="right-image-top">
          B
        </div>

        <div class="right-image-bottom">
          C
        </div>
      </div>
    </div>

    <div class="other"> others</div>
  </div>
</template>

<script>
//import { init } from 'echarts'

export default {
  name: 'HomeView',
  // 目前还未学会echarts及其引入方式，开发时若使用下面代码暂时（）需额外使用npm install echarts
  // 为不影响原有引入方式暂以注解写这一段代码（也许这一段也有错呢
  // mounted() {
  //   const mapChart = init(this.$refs.mapContainer)
  //   this.renderMapChart(mapChart)
  // },
  // methods: {
  //   renderMapChart(chart) {
  //     const option = {
  //       series: [{
  //         type: 'map',
  //         map: 'china'
  //         // 其他地图配置项和数据
  //       }]
  //     }
  //     chart.setOption(option)
  //   }
  // }
}
</script>

<style scoped>
.head {
  position: relative;
  top: 70px;
  text-align: center;
}

.image-layout {
  position: relative;
  top: 100px;
  display: grid;
  grid-template-columns: 2fr 1fr; /* 左2/3，右1/3 */
  gap: 10px; /* 图片之间的间距 */
}

.left-image {
  grid-column: 1; /* 左边图片占据第一列 */
  grid-row: 1 / span 2; /* 左边图片跨越两行 */
}

.right-images {
  display: grid;
  grid-template-rows: 1fr 1fr; /* 右边图片上下各占一半 */
  grid-row: 1 / span 2; /* 右边图片区域跨越两行 */
}

.right-image-top {
  grid-row: 1; /* 上边图片占据第一行 */
}

.right-image-bottom {
  grid-row: 2; /* 下边图片占据第二行 */
}

img {
  width: 100%;
  height: auto;
}

.other
{
  position: relative;
  top: 200px;
}
</style>