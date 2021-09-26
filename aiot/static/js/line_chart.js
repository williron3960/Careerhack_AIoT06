option_line = {
    title: {
        text: title_name
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['AVNET1', 'AVNET2', 'AVNET3', 'AVNET4', 'AVNET5']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00']
    },
    yAxis: {
        min : 0,
        max : 2000,
        type: 'value'
    },
    series: [
        {
            name: 'AVNET1',
            type: 'line',
            stack: '濕度',
            data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
            name: 'AVNET2',
            type: 'line',
            stack: '濕度',
            data: [220, 182, 191, 234, 290, 330, 310]
        },
        {
            name: 'AVNET3',
            type: 'line',
            stack: '濕度',
            data: [150, 232, 201, 154, 190, 330, 410]
        },
        {
            name: 'AVNET4',
            type: 'line',
            stack: '濕度',
            data: [320, 332, 301, 334, 390, 330, 320]
        },
        {
            name: 'AVNET5',
            type: 'line',
            stack: '濕度',
            data: [820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};
setInterval(function () {
    for(i=0;i<5;i++){
        for(j=0;j<7;j++){
            option_line.series[i].data[j] = (Math.random() * 1000).toFixed(2) - 0;
        }   
    }
    lineChart.setOption(option_line, true);
}, 2000);

option_line && lineChart.setOption(option_line);
