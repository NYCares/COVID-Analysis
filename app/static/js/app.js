// NY Doughnut Chart
new Chart(document.getElementById('NYDoughnutChart'), {
    type: 'doughnut',
    data: {
        datasets: [
            {
                data: [1420244,3073800,3416922,193781,1441563,8766,12740974],
                backgroundColor: ['pink', 'lightblue',"coral",'red', 'teal', 'purple','lightgreen'],
            },
        ],
        legend: {
            position: 'left',
        },
        animation: {
            animateRotate: false,
            animateScale: true,
        },
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: ["asian","black","hispanic","native american","other","pacific islander","white"]
    },
})

d3.csv("../static/data/processed/dji_avg.csv", function(data) {
    var dji_data = []

    data.forEach(function(element) {
        dji_data.push(parseFloat(element["Adj Close"]))
    })

    var new_dji = dji_data.slice(13, 135)

    d3.csv("../static/data/processed/covid_confirmed.csv", function(covidData) {
        var keys = Object.keys(covidData[64])
        var values = Object.values(covidData[64])

        var dates = keys.slice(4, 126)
        var covid_data = values.slice(4, 126)

        new Chart(document.getElementById('multipleLineChart'), {
            // The type of chart we want to create
            type: 'line',

            // The data for our dataset
            data: {
                labels: dates,
                datasets: [{
                    data: new_dji,
                    label: 'Dow Jones Index',
                    fill: false,
                    borderColor: 'rgb(144, 238, 144)',
                    backgroundColor: 'rgb(144, 238, 144, 0.25)',
                    yAxisID: 'DJI'
                },
                {
                    data: covid_data,
                    label: 'COVID New Cases',
                    fill: true,
                    borderColor: 'rgb(255, 99, 132)',
                    backgroundColor: 'rgb(255, 99, 132, 0.25)',
                    yAxisID: 'Covid'
                }]
            },
        
            // Configuration options go here
            options: {
                scales: {
                    yAxes: [{
                        id: 'DJI',
                        type: 'linear',
                        position: 'left'
                    },
                    {
                        id: 'Covid',
                        type: 'linear',
                        position: 'right'
                    }]
                }
            }
        })
    })
})
