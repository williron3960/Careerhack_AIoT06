option_co2 = {
    title: {
        text: title_name
    },
    tooltip: {
        trigger: 'axis',
        // formatter: function (params) {
        //     params = params[0];
        //     var date = new Date(params.name);
        //     console.log(date);
        //     return date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds() + ':' + date.getMilliseconds() + ' - ' + params.value[1];
        // },
        axisPointer: {
            animation: false
        }
    },
    legend: {
        data: ['AVNET1', 'AVNET2', 'AVNET3', 'AVNET4', 'AVNET5']
    },
    xAxis: {
        type: 'time',
        splitLine: {
            show: false
        }
    },
    yAxis: {
        min:0,
        max:800,
        type: 'value',
        boundaryGap: [0, '100%'],
        splitLine: {
            show: false
        }
    },
    series: [{
        name: 'AVNET1',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: co2_data1,
        connectNulls: true,
    },
    {
        name: 'AVNET2',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: co2_data2,
        connectNulls: true,
    },
    {
        name: 'AVNET3',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: co2_data3,
        connectNulls: true,
    },
    {
        name: 'AVNET4',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: co2_data4,
        connectNulls: true,
    },
    {
        name: 'AVNET5',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: co2_data5,
        connectNulls: true,
    }]
};

option_co2 && CO2DyLineChart.setOption(option_co2);
