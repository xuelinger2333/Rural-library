<template>
    <div 
        class="echart" 
        id="ScorePie" 
        :style="{ float: 'center', width: '100%', height: '240px' }">
    </div>
</template>

<script>
import * as echarts from "echarts";
import bus from 'vue3-eventbus'

export default {
    data() {
        return {
            params: null,
            ScorePie: {},
            pieData: [],
            option : 
            {
                legend: 
                {
                    data: this.dataName,
                    right: "10%",
                    top: "30%",
                    orient: "vertical"
                },

                title: 
                {
                    text: "评级占比",
                    top: "10%",
                    left: "center"
                },

                series: [
                    {
                        type: "pie",
                        label: 
                        {
                            show: true,
                            formatter: "{b} : {c} ({d}%)" // b代表名称，c代表对应值，d代表百分比
                        },
                        radius: "60%", //饼图半径
                        data: this.pieData
                    }
                ]
            },
            dataName: [],
        };
    },
    mounted() {
        this.initEcharts();
        bus.on('province', this.updateScorePie)   // listen
        //bus.off('foo', onFoo)  // unlisten
    },
    methods: {
        initEcharts() {
            // 饼图
            const option = {

                legend: 
                {
                    data: this.dataName,
                    right: "10%",
                    top: "30%",
                    orient: "vertical"
                },

                title: 
                {
                    text: "评级占比",
                    top: "10%",
                    left: "center"
                },

                series: [
                    {
                        type: "pie",
                        label: 
                        {
                            show: true,
                            formatter: "{b} : {c} ({d}%)" // b代表名称，c代表对应值，d代表百分比
                        },
                        radius: "60%", //饼图半径
                        data: this.pieData
                    }
                ]
            };
            this.ScorePie = echarts.init(document.getElementById("ScorePie"));
            this.ScorePie.setOption(option , true);
            window.addEventListener("resize", () => {
                this.ScorePie.resize();
            });
        },
        updateScorePie (provinceAndlibData)
        {
            console.log("ScorepPie Received" , provinceAndlibData.province.data , provinceAndlibData.libData);

            var scoreData = [
                {
                    value : 0,
                    name : "1"
                },
                {
                    value : 0,
                    name : "2"
                },
                {
                    value : 0,
                    name : "3"
                },
                {
                    value : 0,
                    name : "4"
                },
                {
                    value : 0,
                    name : "5"
                }
            ]

            // console.log(Object.keys(provinceAndlibData.libData).length);
            for (let key in provinceAndlibData.libData) {
                scoreData[provinceAndlibData.libData[key].score - 1].value++;
            }
            //有数据
            //this.option.series[0].data =scoreData;
            //this.ScorePie.setOption(this.option , true);
        }
    }
};
</script>

