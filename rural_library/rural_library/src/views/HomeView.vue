<template>
  <div class="home">
    <div>
      <h1 class="head">全国农家书屋统计数据</h1>
    </div>

    <div class="image-layout">
      
      <div class="left-image">
  
        <div class="mapp">
          <China></China>
        </div>
      </div>

      <div class="right-images">
        <div class="right-image-top">
          <ScorePie></ScorePie>
        </div>

        <div class="right-image-bottom">
          <AmountRank></AmountRank>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { provinceAndCityData, regionData, provinceAndCityDataPlus, regionDataPlus, CodeToText, TextToCode } from 'element-china-area-data'
//import aMap from "@/components/amap.vue"
import China from "@/components/china.vue"
import ScorePie from "@/components/ScorePie.vue"
import AmountRank from "@/components/AmountRank.vue"


export default {
  name: 'HomeView',
  components:
  {
    //aMap,
    China,
    ScorePie,
    AmountRank
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
.home {
  background-color: #edece8;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  overflow-x: hidden;
  overflow-y: scroll;
}
.mapp {
  width: 48vw;
  height: 100%;
  z-index: 2;
  background-color: #cad5dc;
  border-radius: 20px;
}

.head {
  position: relative;
  top: 70px;
  font-family: "Kyo";
  text-align: center;
}

.image-layout {
  margin-left: 20px;
  margin-right: 20px;
  position: relative;
  top: 80px;
  display: grid;
  grid-template-columns: 1fr 1fr; /* 左1/2，右1/2 */
  gap: 20px; /* 图片之间的间距 */
  height: 65vh;
}

.left-image {
  grid-column: 1; /* 左边图片占据第一列 */
  grid-row: 1 / span 2; /* 左边图片跨越两行 */
}

.right-images {
  background-color: #cad5dc;
  border-radius: 20px;
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


</style>