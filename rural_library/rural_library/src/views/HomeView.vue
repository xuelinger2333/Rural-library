<template>
  <div class="home">
    <div>
      <h1 class="head">全国农家书屋统计数据</h1>
    </div>

    <div class="image-layout">
      
      <div class="left-image">
        <button @click="returnCountry">返回全国</button>
        <div class="mapp">
          <aMap :reCountry="reCountry"></aMap>
        </div>
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
    <ChinaMap></ChinaMap>
  </div>
</template>

<script>
import { provinceAndCityData, regionData, provinceAndCityDataPlus, regionDataPlus, CodeToText, TextToCode } from 'element-china-area-data'
import aMap from "@/components/amap.vue"

export default {
  name: 'HomeView',
  components:
  {
    aMap
  },
  data(){
    return{
      provinceAndCityData,
      reCountry:true,
    }
  },
  methods: {
  			//点击全国按钮
		    returnCountry() {
		      this.reCountry = true;
		      setTimeout(() => {
		        this.reCountry = false;
		      }, 500);
		    },
  		}
}
</script>

<style scoped>
.mapp {
  width: 48vw;
  height: 69vh;
  z-index: 2;
}

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