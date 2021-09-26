
const getACDefault = async() =>{
    for(i=1;i<5;i++){
        const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=' + i + '&time=2020/01/01_00:00:00' , {
            method: 'GET',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Credentials':'true'
            }
        });
        var data_json = await res.json();
        console.log(data_json);
        switch(i){
            case 1:
                option_guage1.series[0].data[0].value =  data_json.temperature;
                guageChart1.setOption(option_guage1, true);
                break;
            case 2:
                option_guage2.series[0].data[0].value =  data_json.temperature;
                guageChart2.setOption(option_guage2, true);
                break;
            case 3:
                option_guage3.series[0].data[0].value =  data_json.temperature;
                guageChart3.setOption(option_guage3, true);
                break;
            case 4:
                option_guage4.series[0].data[0].value =  data_json.temperature;
                guageChart4.setOption(option_guage4, true);
                break;
        }        
    }
}

const getAC1Data = async() =>{
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=1&time=' + dateString, {
    // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=1&time=2021/01/28_20:01:30', {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}
const refreshAC1 = () =>{
    setInterval(async () => {
        var data_json = await getAC1Data();
        console.log(data_json)
        option_guage1.series[0].data[0].value =  data_json.temperature;
        guageChart1.setOption(option_guage1, true);
    }, 5000);
    option_guage1 && guageChart1.setOption(option_guage1);
}

const getAC2Data = async() => {
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=2&time=' + dateString, {
    // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=2&time=2021/01/27_03:15:00', {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}      
const refreshAC2 = () => {
    setInterval(async() => {
        var data_json = await getAC2Data();
        option_guage2.series[0].data[0].value = data_json.temperature;
        guageChart2.setOption(option_guage2, true);
    }, 5000);

    option_guage2 && guageChart2.setOption(option_guage2);
}

const getAC3Data = async() => {
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=3&time=' + dateString, {
    // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=3&time=2021/01/27_03:15:00', {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}      
const refreshAC3 = () => {
    setInterval(async() => {
        var data_json = await getAC3Data();
        option_guage3.series[0].data[0].value = data_json.temperature;
        guageChart3.setOption(option_guage3, true);
    }, 5000);

    option_guage3 && guageChart3.setOption(option_guage3); 
}

const getAC4Data = async() => {
    const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=4&time=' + dateString, {
    // const res = await fetch('https://aiot-task-api.azurewebsites.net/api/GetACData?air_id=4&time=2021/01/27_03:15:00', {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials':'true'
        }
    });
    return await res.json();
}      
const refreshAC4 = () => {
    setInterval(async() => {
        var data_json = await getAC4Data();
        option_guage4.series[0].data[0].value = data_json.temperature;
        guageChart4.setOption(option_guage4, true);
    }, 5000);

    option_guage4 && guageChart4.setOption(option_guage4);
}