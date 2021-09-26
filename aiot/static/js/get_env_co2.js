var co2_data1 = [];
var co2_data2 = [];
var co2_data3 = [];
var co2_data4 = [];
var co2_data5 = [];

const PushCO2 = (data) => {
    CO2 = data;
    return {
        name: now_datetime.toString(),
        value: [now_datetime, CO2]

    };
}
// AVNET1
const getCO21Data = async() =>{
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
const getCO22Data = async() =>{
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
const getCO23Data = async() =>{
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
const getCO24Data = async() =>{
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
const getCO25Data = async() =>{
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

//refresh all AVNET co2 
const refreshCO2 = async() =>{
    setInterval(async () => {
        var data_json1 = await getCO21Data();
        var data_json2 = await getCO22Data();
        var data_json3 = await getCO23Data();
        var data_json4 = await getCO24Data();
        var data_json5 = await getCO25Data();
        
        co2_data1.push(PushCO2(data_json1.co2));
        co2_data2.push(PushCO2(data_json2.co2));
        co2_data3.push(PushCO2(data_json3.co2));
        co2_data4.push(PushCO2(data_json4.co2));
        co2_data5.push(PushCO2(data_json5.co2));

        await CO2DyLineChart.setOption({
            series: [{
                name : 'AVNET1',
                data: co2_data1
            },
            {
                name : 'AVNET2',
                data: co2_data2
            },
            {
                name : 'AVNET3',
                data: co2_data3
            },
            {
                name : 'AVNET4',
                data: co2_data4
            },
            {
                name : 'AVNET5',
                data: co2_data5
            }
        ]
        });
        
    }, 5 * 1000);
}

