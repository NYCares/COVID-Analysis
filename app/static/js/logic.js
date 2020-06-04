var map = L.map("map", {
  center: [42.75, -75.5],
  zoom: 7
});
  
// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: 'mapbox/light-v9',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: API_KEY
}).addTo(map);
  
// Link to local geojson
var countyLink = "../static/data/ny_color.geojson";

function getColor(d) {
  return d > 60000 ? '#800026' :
  d > 50000  ? '#BD0026' :
  d > 20000  ? '#E31A1C' :
  d > 10000  ? '#FC4E2A' :
  d > 5000   ? '#FD8D3C' :
  d > 2000   ? '#FEB24C' :
  d > 1000   ? '#FED976' :
             '#FFEDA0';
}

function style(feature) {
  return {
      fillColor: getColor(feature.properties.percent),
      weight: 2,
      opacity: 1,
      color: 'white',
      dashArray: '3',
      fillOpacity: 0.7
  };
}

// Grabbing our GeoJSON data..
d3.json(countyLink, function(data) {
  // Creating a GeoJSON layer with the retrieved data
  L.geoJson(data,{
    style: style,

    // called on each feature
    onEachFeature: function(feature, layer) {
      // identify county name
      label = feature.properties.name

      layer.bindPopup("<h1>" + label)

      // darken color on hover
      layer.on({
        mouseover: function(event) {
          layer = event.target
          layer.setStyle({
            fillOpacity: 1,
            weight: 5,
            color: '#666',
            dashArray: ''
          })
          if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
            layer.bringToFront();
          }
          info.update(layer.feature.properties)
          layer.openPopup()
          
        },
        mouseout: function(event) {
          layer = event.target
          layer.setStyle({
            fillOpacity: 0.7,
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3'
          })
          info.update()
          layer.closePopup()
        }
      })
    }
  }).addTo(map);

  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 1000, 2000, 5000, 10000, 20000, 50000, 60000],
        labels = [];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }

    return div;
  };
  legend.addTo(map);

  var info = L.control();

  info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
  };

  // method that we will use to update the control based on feature properties passed
  info.update = function (props) {
    this._div.innerHTML = '<h4>NY Covid Cases as of May 22</h4>' +  (props ?
        '<b>' + props.name + '</b><br />' + props.percent + ' people with COVID-19'
        : 'Hover over a county');
  };

  info.addTo(map);


});