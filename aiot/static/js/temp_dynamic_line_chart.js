option_temp = {
    title: {
        text: title_name
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            animation: false
        },
        // formatter: ((para) => {
        //     console.log('formatter:')
        //     console.log(para[0].data.name);
        //     const now_datetime = new Date(para[0].data.name);
        //     // console.log(typeof(now_datetime))
        //     return [now_datetime.getFullYear(), now_datetime.getMonth() + 1 , now_datetime.getDate()].join('/') + ' ' +
        //     [now_datetime.getHours(), now_datetime.getMinutes(), now_datetime.getSeconds()].join(':')
        // })
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
        min:10,
        max:40,
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
        data: temp_data1,
        connectNulls: true,
    },
    {
        name: 'AVNET2',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: temp_data2,
        connectNulls: true,
    },
    {
        name: 'AVNET3',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: temp_data3,
        connectNulls: true,
    },
    {
        name: 'AVNET4',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: temp_data3,
        connectNulls: true,
    },
    {
        name: 'AVNET5',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: temp_data3,
        connectNulls: true,
    }
]
};

option_temp && tempDyLineChart.setOption(option_temp);
