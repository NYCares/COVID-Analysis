var map = L.map("map", {
  center: [42.75, -75.5],
  zoom: 7
});
  
// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: 'mapbox/streets-v11',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: API_KEY
}).addTo(map);
  
// Link to local geojson
var link = "static/data/ny.geojson";

// Our style object
var mapStyle = {
  color: "darkblue",
  fillColor: "blue",
  fillOpacity: 0.5,
  weight: 1.5
};
  
// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  // Creating a GeoJSON layer with the retrieved data
  L.geoJson(data, {
    style: mapStyle,

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
            fillOpacity: 0.9
          })
          layer.openPopup()
          
        },
        mouseout: function(event) {
          layer = event.target
          layer.setStyle({
            fillOpacity: 0.5
          })
          layer.closePopup()
        }
      })
    }
  }).addTo(map);
});