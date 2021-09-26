var temp_data1 = [];
var temp_data2 = [];
var temp_data3 = [];
var temp_data4 = [];
var temp_data5 = [];

const DefaultData = async() => {
    dateString =
    now_datetime.getFullYear() + "/" +
        ("0" + (now_datetime.getMonth()+1)).slice(-2) + "/" +
        ("0" + now_datetime.getDate()).slice(-2) + "_" +
        ("0" + (now_datetime.getHours() ) ).slice(-2) + ":" +
        ("0" + now_datetime.getMinutes()).slice(-2) + ":" +
        ("0" + (now_datetime.getSeconds()) ).slice(-2);
    // console.log(now_datetime)
    // console.log(dateString)

    for (i=0;i<5;i++){
        var data_json1 = await getTemp1Data();
        var data_json2 = await getTemp2Data();
        var data_json3 = await getTemp3Data();
        var data_json4 = await getTemp4Data();
        var data_json5 = await getTemp5Data();

        console.log(data_json1)
        console.log(data_json1.length)
        
        temp_data1.push(PushTemp(data_json1.temperature));
        temp_data2.push(PushTemp(data_json2.temperature));
        temp_data3.push(PushTemp(data_json3.temperature));
        temp_data4.push(PushTemp(data_json4.temperature));
        temp_data5.push(PushTemp(data_json5.temperature));

        now_datetime = new Date(+now_datetime + (60 * 1000))
                dateString =
                now_datetime.getFullYear() + "/" +
                    ("0" + (now_datetime.getMonth()+1)).slice(-2) + "/" +
                    ("0" + now_datetime.getDate()).slice(-2) + "_" +
                    ("0" + (now_datetime.getHours() ) ).slice(-2) + ":" +
                    ("0" + now_datetime.getMinutes()).slice(-2) + ":" +
                    ("0" + (now_datetime.getSeconds()) ).slice(-2);

    }
    await tempDyLineChart.setOption({
        series: [{
            name : 'AVNET1',
            data: temp_data1
        },
        {
            name : 'AVNET2',
            data: temp_data2
        },
        {
            name : 'AVNET3',
            data: temp_data3
        },
        {
            name : 'AVNET4',
            data: temp_data4
        },
        {
            name : 'AVNET5',
            data: temp_data5
        }
    ]
    });
    // await  getDatetime();
}

const PushTemp = (data) => {
    temp = data;
    console.log('data = ' + data);
    console.log('now_datetime =' + now_datetime.toString());
    console.log('datetime = ' +   [now_datetime.getFullYear(), now_datetime.getMonth() + 1 , now_datetime.getDate()].join('/') + 'T' +
    [now_datetime.getHours(), now_datetime.getMinutes(), now_datetime.getSeconds()].join(':'));

    return {
        name: now_datetime.toString(),
        value: [now_datetime, temp]

    };
}
// AVNET1
const getTemp1Data = async() =>{
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=1&time=' + dateString  , {
        // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=1&time=2019/12/31_23:59:00'   , {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}
// AVNET2
const getTemp2Data = async() =>{
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=2&time=' + dateString, {
        // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=2&time=2019/12/31_23:59:00' , {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}

// AVNET3
const getTemp3Data = async() =>{
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=3&time=' + dateString, {
        // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=3&time=2019/12/31_23:59:00', {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}

// AVNET4
const getTemp4Data = async() =>{
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=4&time=' + dateString, {
    // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=4&time=2019/12/31_23:59:00', {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}

// AVNET5
const getTemp5Data = async() =>{
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=5&time=' + dateString, {
    // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetENVData?env_id=5&time=2019/12/31_23:59:00', {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}

//refresh all AVNET temperature 
const refreshTemp = async() =>{
    setInterval(async () => {
        var data_json1 = await getTemp1Data();
        var data_json2 = await getTemp2Data();
        var data_json3 = await getTemp3Data();
        var data_json4 = await getTemp4Data();
        var data_json5 = await getTemp5Data();

        console.log(data_json1);
        console.log(temp_data1.length)
        
        temp_data1.push(PushTemp(data_json1.temperature));
        temp_data2.push(PushTemp(data_json2.temperature));
        temp_data3.push(PushTemp(data_json3.temperature));
        temp_data4.push(PushTemp(data_json4.temperature));
        temp_data5.push(PushTemp(data_json5.temperature));

        console.log('data111 = ' + temp_data1.length)
        console.log('data2 = ' + temp_data2.length)

        await tempDyLineChart.setOption({
            series: [{
                name : 'AVNET1',
                data: temp_data1
            },
            {
                name : 'AVNET2',
                data: temp_data2
            },
            {
                name : 'AVNET3',
                data: temp_data3
            },
            {
                name : 'AVNET4',
                data: temp_data4
            },
            {
                name : 'AVNET5',
                data: temp_data5
            }
        ]
        });
        
    }, 5 * 1000);
}

