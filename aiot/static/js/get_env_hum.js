var hum_data1 = [];
var hum_data2 = [];
var hum_data3 = [];
var hum_data4 = [];
var hum_data5 = [];

const PushHumid = (data) => {
    hum = data;
    return {
        name: now_datetime.toString(),
        value: [now_datetime, hum]

    };
}
// AVNET1
const getHumid1Data = async() =>{
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
const getHumid2Data = async() =>{
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
const getHumid3Data = async() =>{
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
const getHumid4Data = async() =>{
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
const getHumid5Data = async() =>{
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

//refresh all AVNET humidity 
const refreshHumid = async() =>{
    setInterval(async () => {
        var data_json1 = await getHumid1Data();
        var data_json2 = await getHumid2Data();
        var data_json3 = await getHumid3Data();
        var data_json4 = await getHumid4Data();
        var data_json5 = await getHumid5Data();
        
        hum_data1.push(PushHumid(data_json1.humidity));
        hum_data2.push(PushHumid(data_json2.humidity));
        hum_data3.push(PushHumid(data_json3.humidity));
        hum_data4.push(PushHumid(data_json4.humidity));
        hum_data5.push(PushHumid(data_json5.humidity));

        await humDyLineChart.setOption({
            series: [{
                name : 'AVNET1',
                data: hum_data1
            },
            {
                name : 'AVNET2',
                data: hum_data2
            },
            {
                name : 'AVNET3',
                data: hum_data3
            },
            {
                name : 'AVNET4',
                data: hum_data4
            },
            {
                name : 'AVNET5',
                data: hum_data5
            }
        ]
        });
        
    }, 5 * 1000);
}

