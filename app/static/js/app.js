// Load data from hours-of-tv-watched.csv
d3.csv("../static/data/processed/population_race_breakdown.csv", function(data, county) {
    var raceKey = []
    var raceValue = []
    
    county.forEach(function(element) {
        if (element.County == "Queens County") {
            for (var i = 3; i < 9; i++) {
                raceKey.push(Object.keys(element)[i])
                raceValue.push(Object.values(element)[i])
            }
        }
    });

    // Doughnut Chart
    var ctx = document.getElementById('myDoughnutChart')
    var myDoughnutChart = new Chart (ctx, {
        type: 'doughnut',
        data: {
            datasets: [
                {
                    data: raceValue,
                    backgroundColor: ['pink', 'lightblue','red', 'lightgrey', 'yellow','lightgreen'],
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
        labels: raceKey
        }})
})

// NY Doughnut Chart
var ctx = document.getElementById('NYDoughnutChart').getContext('2d');
var NYDoughnutChart = new Chart(ctx, {
type: 'doughnut',
data: {
    datasets: [
        {
            data: [12740974,3073800,0,1420244,8766,1441563],
            backgroundColor: ['pink', 'lightblue','red', 'lightgrey', 'yellow','lightgreen'],
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
labels: ["white","black","native_american","asian","pacific_islander","other"]
}})

d3.csv("../static/data/processed/dji_avg.csv", function(data) {
    var dji_data = []

    data.forEach(function(element) {
        dji_data.push(parseFloat(element["Adj Close"]))
    })

    var new_dji = dji_data.slice(13, 135)

    d3.csv("../static/data/processed/covid_confirmed.csv", function(covidData) {
        var keys = Object.keys(covidData[36])
        var values = Object.values(covidData[36])

        var dates = keys.slice(4, 126)
        var covid_data = values.slice(4, 126)

        var ctx = document.getElementById('multipleLineChart').getContext('2d')
        var chart = new Chart(ctx, {
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
                    yAxisID: 'DJI'
                },
                {
                    data: covid_data,
                    label: 'COVID New Cases',
                    fill: false,
                    borderColor: 'rgb(255, 99, 132)',
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
