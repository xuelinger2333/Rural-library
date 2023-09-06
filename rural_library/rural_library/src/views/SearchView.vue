<template>
    <div id="app">
      <div class="search">
        <el-space wrap>
        <p>所在地</p>
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

        <div v-for="(item, index) in list " :key="index" shadow="hover" class="elcard" style="width: 800px" @click="showDetail(item)">
          <div class="card">
            <div class="text">
              <p>书屋名称：{{ item.name }}</p>
              <p>书屋地点：{{ item.place }}</p>
              <p>致电：{{ item.telephone }}</p>
            </div>
          </div>
        </div>

      </el-space>
      </div>
      </div>
      </div>
      <div class="motto">
        <p id="shu">书山有路勤为径，学海无涯苦作舟。</p>
      </div>
      <div class="ocean">
            <svg class="waves" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                <defs>
                    <path id="gentle-wave"
                        d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                </defs>
                <g class="parallax">
                    <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(242,175,155,0.7)" />
                    <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255, 255,0.5)" />
                    <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(208,229,242,1)" />
                    <use xlink:href="#gentle-wave" x="48" y="7" fill="rgba(103, 163, 215, 1)" />
                </g>
            </svg>
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
          let str = this.selectedOptions.join('');
          let str_prefex = this.selectedOptions[0];
          switch(str_prefex){
            case "50":
              console.log("50")
              this.list = [{
                name: "礼朝屋基农家书屋",
                place: "重庆市渝北区兴隆镇牛皇村",
                avatar:12,
                telephone: "199-0835-3995",
                id: 1
              },
              {
                name: "新寨村",
                place: "重庆市渝北区兴隆镇新寨村",
                avatar:12,
                telephone: "139-8337-0606",
                id: 2
              },
              {
                name: "建新村",
                place: "重庆市高新区建新村",
                avatar:12,
                telephone: "150-2374-5430",
                id: 3
              }
            ]
            return
          }
          switch(str)
          {
            case "323201":
              this.list = [
                {
                  name: "朱家边社区",
                  place: "南京市溧水区白马镇朱家边社区党群服务中心一楼",
                  avatar:12,
                  telephone: "",
                  id:1
                },
                {
                  name: "睦邻书房",
                  place: "南京市江宁区秣陵街道吉山社区",
                  avatar:12,
                  telephone: "",
                  id:2
                },
                {
                  name: "夏桥书房",
                  place: "南京市浦口区星甸街道石窑社区",
                  avatar:12,
                  telephone: "",
                  id:2
                },
                {
                  name: "荷香社区",
                  place: "南京市溧水区柘塘街道",
                  avatar:12,
                  telephone: "",
                  id:2
                },
              ]
              return;
            case "515101":
              this.list = [{
                name: "天府之家",
                place: "四川省成都市新津区普兴街道岳店村农家书屋",
                avatar:12,
                telephone: "",
                id:1
              },{
                name: "昌衡书院",
                place: "彭州市九尺镇昌衡村3组尹昌衡故居片区",
                avatar:12,
                telephone: "",
                id:2
              },{
                name: "梨花读",
                place: "彭州市葛仙山镇熙玉村——千亩梨园景区",
                avatar:12,
                telephone: "",
                id:2
              }
              ]
              return;
            case "626208":
              this.list = [{
                name: "西沟村",
                place: "甘肃省平凉市崆峒区",
                avatar:12,
                telephone: "",
                id:1
              },
              {
                name: "南台村",
                place: "甘肃省平凉市崆峒区柳湖镇南台村",
                avatar:12,
                telephone: "",
                id:2
              },{
                name: "段渠村",
                place: "甘肃省平凉市三合乡段渠村",
                avatar:12,
                telephone: "",
                id:2
              },{
                name: "古岔村",
                place: "甘肃省平凉市三合乡古岔村",
                avatar:12,
                telephone: "",
                id:2
              },{
                name: "下杨村",
                place: "甘肃省平凉市崆峒区上杨乡下杨村",
                avatar:12,
                telephone: "",
                id:2
              },{
                name: "早庄村",
                place: "甘肃省平凉市崆峒区上杨乡早庄村",
                avatar:12,
                telephone: "",
                id:2
              }
            ]
              return
          }
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
      background-color: #edece8;
      background-size:100% 100%;
      background-attachment: fixed;
    }
    .search {
      z-index: 20;
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
    .elcard {

      background-color: #cad5dc;
      padding: 20px;
      margin-top: 10px;
      border-radius: 20px;
      transition: all 0.5s;
    }
    .elcard:hover {
      box-shadow: inset 1px 1px 6px rgba(255, 255, 255, 0.3),
                  2px 2px 15px rgba(0, 0, 0, 0.5);
      transform: translateY(-.08rem);
    }
    .card {
      cursor: pointer;
      display: flex;
      margin-left: 10px;
    }
    p {
      font-family: "Kyo";
      text-align: left;
      margin: 5px;
    }
    .text {
      margin-left: 10px;
      width: 800px;
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
.motto {
  position: absolute;
  top:217px;
  left:143px;
}
#shu {
  font-size: 30px;
}

    .waves {
            position: fixed;
            bottom:0px;
            width: 100%;
            right:0px;
            height: 20vh;
            min-height: 100px;
            max-height: 150px;
            z-index: 0;
        }


        .parallax>use {
            /* 使use元素执行move-forever动画 */
            animation: move-forever 25s cubic-bezier(.55, .5, .45, .5) infinite;
        }

        .parallax>use:nth-child(1) {
            /* 延迟2秒启动动画  */
            animation-delay: -2s;
            /* 设置动画持续时间为7秒 */
            animation-duration: 7s;
        }

        .parallax>use:nth-child(2) {
            animation-delay: -3s;
            animation-duration: 10s;
        }

        .parallax>use:nth-child(3) {
            animation-delay: -4s;
            animation-duration: 13s;
        }

        .parallax>use:nth-child(4) {
            animation-delay: -5s;
            animation-duration: 20s;
        }

        @keyframes move-forever {
            0% {
                transform: translate3d(-90px, 0, 0);
            }

            100% {
                transform: translate3d(85px, 0, 0);
            }
        }

        @media (max-width: 768px) {
            .waves {
                height: 40px;
                min-height: 40px;
            }

            .content {
                height: 30vh;
            }

            h1 {
                font-size: 24px;
            }
        } 
</style>