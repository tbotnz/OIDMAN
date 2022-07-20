
var charts = {
};

var payloads = [
];

function addData(chartd, label, data, title) {
    chartd.data.labels.push(label);
    chartd.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chartd.options.title.text = title;
    chartd.update();
}

var ws = new WebSocket("ws://" + window.location.host + "/ws");
ws.onmessage = function (event) {
    let data = JSON.parse(event.data)
    for (const n in data) {
        console.log("chart key " + data[n].chart_key);
        if ((data[n].chart_key in charts) == false) {
            let charte = newChart(data[n].chart_key);
        }
        let chartdata = charts[data[n].chart_key];
        addData(chartdata, data[n].timestamp, data[n].payload, data[n].chart_key)
    }
};

function newChart(chart_key) {



    let canvas = document.createElement("canvas");
    canvas.setAttribute("id", chart_key);
    canvas.setAttribute("height", "300px");

    let canvasContainer = document.createElement("div");
    canvasContainer.setAttribute("class", "row");
    canvasContainer.appendChild(canvas);

    let card = document.createElement("div");
    card.setAttribute("class", "card bg-dark text-white");

    let cardbody = document.createElement("div");
    cardbody.setAttribute("class", "card-body");
    cardbody.appendChild(canvasContainer);
    card.appendChild(cardbody);

    let row = document.createElement("div");
    row.setAttribute("class", "row");
    row.appendChild(card);

    document.getElementById("chartbox").prepend(row);

    var color = Math.floor(Math.random() * 16777215).toString(16);
    const chart = new Chart(document.getElementById(chart_key), {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                borderColor: `#${color}`
            }]
        },
        options: {
            title: {
                display: true,
                text: ''
            },
            responsive: true,
            legend: {
                labels: {
                    defaultFontColor: 'white'
                },
                display: false
            }
        }
    });
    charts[chart_key] = chart;
    return chart;
}

function sendMessage(event) {
    let chart_key = document.getElementById("oid").value + "-" + document.getElementById("host").value;
    let data = {
        "interval": document.getElementById("interval").value,
        "polls": document.getElementById("polls").value,
        "oid": document.getElementById("oid").value,
        "host": document.getElementById("host").value,
        "community": document.getElementById("community").value,
        "resolve_oid": document.getElementById("resolve_oid").checked
    }
    payloads.push(data);
    ws.send(JSON.stringify(payloads));
    data = "";
    event.preventDefault()
}