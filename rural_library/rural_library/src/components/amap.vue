<template>
    <div
      id="container"
    ></div>
  </template>
  
  <script>
  import AMap from "AMap"
  import AMapUI from "AMapUI"
  export default {
      props:{
          reCountry: Boolean
      },
      data() {
          return {
          amap: null,
          districtExplorer: null,
          tipMarker: null,
          $tipMarkerContent: null,
          currentAreaNode: null,
          aReCountry: this.reCountry
          };
      },
      mounted() {
          this.amap = new AMap.Map("container", {
          defaultCursor: "pointer",
          center: [103.714129, 38.150339], // 地图中心点
          zoom: 4, // 地图显示的缩放级别
          resizeEnable: true, //是否监控地图容器尺寸变化
          mapStyle: "amap://styles/normal" // 地图样式
          });
          this.drawArea();
      },
      methods:{
          drawArea()
          {
              AMapUI.load(
                  ["ui/geo/DistrictExplorer", "lib/$"],
                  (DistrictExplorer, $) => {
                      //创建一个实例
                      this.districtExplorer = window.districtExplorer = new DistrictExplorer({
                          eventSupport: true, //打开事件支持
                          map: this.amap
                      });
  
                      //当前聚焦的区域
                      this.$tipMarkerContent = $('<div class="tipMarker top"></div>');
                      this.tipMarker = new AMap.Marker({
                          //源码为 content: this.$tipMarkerContent.get(0)，在初始时为null会直接报错
                          content: this.$tipMarkerContent ? this.$tipMarkerContent.get(0) : null,
                          offset: new AMap.Pixel(0, 0),
                          bubble: true
                      });
  
                      //监听feature的hover事件
                      this.districtExplorer.on(
                          "featureMouseout featureMouseover",
                          (e, feature) => {
                              this.toggleHoverFeature(
                                  feature,
                                  e.type === "featureMouseover",
                                  e.originalEvent ? e.originalEvent.lnglat : null
                              );
                          }
                      );
  
                      //监听鼠标在feature上滑动
                      this.districtExplorer.on("featureMousemove", e => {
                          //更新提示位置
                          this.tipMarker.setPosition(e.originalEvent.lnglat);
                      });
                      //feature被点击
                      this.districtExplorer.on("featureClick", (e, feature) => {
                          const props = feature.properties;
                          //  if (props.level === "province") {
                          // 只下钻到省一级 （省：province，市：city，县：district）
                          // 若是下钻到县一级，那么这个if判断就可以注释掉
                          this.switchToAreaNode(props.adcode);
                          this.aReCountry = false;
                          // }
                      });
                      //全国
                      this.switchToAreaNode(100000);
                  }
              );
          },
  
          //根据Hover状态设置相关样式
          toggleHoverFeature(feature, isHover, position) 
          {
            this.tipMarker.setMap(isHover ? this.amap : null);

            if (!feature) {
                return;
            }

            var props = feature.properties;

            if (isHover) {

                //更新提示内容
                // this.$tipMarkerContent ? this.$tipMarkerContent.html(props.adcode) : null;
                // 此行代码待检查，会导致一开始的时候的hover事件直接报错
                //更新位置
                this.tipMarker.setPosition(position || props.center);
            }

            $('#area-tree').find('h2[data-adcode="' + props.adcode + '"]').toggleClass('hover', isHover);

            //更新相关多边形的样式
            var polys = districtExplorer.findFeaturePolygonsByAdcode(props.adcode);
            for (var i = 0, len = polys.length; i < len; i++) {

                polys[i].setOptions({
                    fillOpacity: isHover ? 0.5 : 0.2
                });
            }
          },
  
          //切换区域
          switchToAreaNode(adcode, callback)
          {
              if (
                  this.currentAreaNode &&
                  "" + this.currentAreaNode.getAdcode() === "" + adcode)
                  {
                      return;
                  }
                  this.loadAreaNode(adcode, (error, areaNode) => {
                  if (error) 
                  {
                      if (callback) { callback(error); }
                      return;
                  }
                  this.currentAreaNode = areaNode;
                  //设置当前使用的定位用节点
                  this.districtExplorer.setAreaNodesForLocating([this.currentAreaNode]);
                  this.refreshAreaNode(areaNode);
                  if (callback) { callback(null, areaNode); }
              });
          },
  
          refreshAreaNode(areaNode)
          {
              this.districtExplorer.setHoverFeature(null);
              this.renderAreaPolygons(areaNode);
          },
  
          renderAreaPolygons(areaNode)
          {
              //更新地图视野
              if (!this.aReCountry) {
                  this.amap.setBounds(areaNode.getBounds(), null, null, true);
              } else {
                  this.amap.setZoom(4);
                  this.amap.setCenter(new AMap.LngLat(103.714129, 38.150339));
              }
              //清除已有的绘制内容
              this.districtExplorer.clearFeaturePolygons();
              //绘制子区域
              this.districtExplorer.renderSubFeatures(areaNode, () => {
                  return {
                  cursor: "default",
                  bubble: true,
                  strokeColor: "#fff", //线颜色
                  strokeOpacity: 0.4, //线透明度
                  strokeWeight: 1, //线宽
                  fillOpacity: 0 //填充透明度
                  };
              });
              //绘制父区域
              this.districtExplorer.renderParentFeature(areaNode, {
                  cursor: "default",
                  bubble: true,
                  strokeColor: "#fff", //线颜色
                  strokeOpacity: 1, //线透明度
                  strokeWeight: 1, //线宽
                  fillOpacity: 0 //填充透明度
              });
          },
  
          //加载区域
          loadAreaNode(adcode, callback) 
          {
              console.log(adcode);
              console.log(callback);
              this.districtExplorer.loadAreaNode(adcode, (error, areaNode) => 
                  {
                      if (error) 
                      {
                          if (callback) 
                          {
                              callback(error);
                          }
                          window.console.error(error);
                          return;
                      }
                      if (callback) 
                      {
                          callback(null, areaNode);
                      }
                  }
              );
          },
  
      }
  }
  </script>
  
  <style lang="less" scoped>
  
  #container {
      width: 100%;
      height: 100%;
  }
  
  </style>
  
  