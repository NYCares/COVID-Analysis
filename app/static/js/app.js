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
    
    console.log(raceKey)
    console.log(raceValue)

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