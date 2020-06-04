var jsonData = "static/data/clean/covid_ny_county.json"

var newJson = []

d3.json(jsonData, function(data) {
    var json = [data]

    for (var key in json) {
        if (json.hasOwnProperty(key)) {
            newJson.push(json[key]["Albany County"],
            json[key]["Allegany County"],
            json[key]["Bronx County"],
            json[key]["Broome County"],
            json[key]["Cattaraugus County"],
            json[key]["Cayuga County"],
            json[key]["Chautauqua County"],
            json[key]["Chemung County"],
            json[key]["Chenango County"],
            json[key]["Clinton County"],
            json[key]["Columbia County"],
            json[key]["Cortland County"],
            json[key]["Delaware County"],
            json[key]["Dutchess County"],
            json[key]["Erie County"],
            json[key]["Essex County"],
            json[key]["Franklin County"],
            json[key]["Fulton County"],
            json[key]["Genesee County"],
            json[key]["Greene County"],
            json[key]["Hamilton County"],
            json[key]["Herkimer County"],
            json[key]["Jefferson County"],
            json[key]["Kings County"],
            json[key]["Lewis County"],
            json[key]["Livingston County"],
            json[key]["Madison County"],
            json[key]["Monroe County"],
            json[key]["Montgomery County"],
            json[key]["Nassau County"],
            json[key]["New York County"],
            json[key]["Niagara County"],
            json[key]["Oneida County"],
            json[key]["Onondaga County"],
            json[key]["Ontario County"],
            json[key]["Orange County"],
            json[key]["Orleans County"],
            json[key]["Oswego County"],
            json[key]["Otsego County"],
            json[key]["Putnam County"],
            json[key]["Queens County"],
            json[key]["Rensselaer County"],
            json[key]["Richmond County"],
            json[key]["Rockland County"],
            json[key]["Saratoga County"],
            json[key]["Schenectady County"],
            json[key]["Schoharie County"],
            json[key]["Schuyler County"],
            json[key]["Seneca County"],
            json[key]["St. Lawrence County"],
            json[key]["Steuben County"],
            json[key]["Suffolk County"],
            json[key]["Sullivan County"],
            json[key]["Tioga County"],
            json[key]["Tompkins County"],
            json[key]["Ulster County"],
            json[key]["Warren County"],
            json[key]["Washington County"],
            json[key]["Wayne County"],
            json[key]["Westchester County"],
            json[key]["Wyoming County"],
            json[key]["Yates County"])
        }
    }

    var percent = newJson.map(function(county) {
        return county["Cases"]
    })

    console.log(percent)
    
    // percent.forEach((i) => console.log(i))

    var countyLink = "static/data/source/ny.geojson"
    
    d3.json(countyLink, function(data){
        data.features.forEach(function(item, index){
            item.properties.percent = percent.forEach((i) => i)
            // console.log(item.properties, index)
        })
        
    var blob = new Blob([JSON.stringify(data)], {type: "text/plain;charset=utf-8"});
    saveAs(blob, "ny_color.geojson")
})
})