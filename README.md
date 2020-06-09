# NYCares
### A deep dive analysis into the impact COVID-19 has had on different counties within New York.
<hr>

**Team:** Karl Ramsay (Project Manager - Back-End), Swati Dontamsetti (Front-End), Firzana Razak (Front-End), Amber Martin (Back-End), Oswaldo Moreno (Back-End), Anthony Brown (Back-End)
<hr>

## Overview
With a potential plateau in COVID-19 cases in NY, but no definite decrease as of yet, we are interested into seeing what the impact has been on the different counties of NY. We look into the demographic and socio-economic breakdown of each county, while keeping in mind how the impact has varied from county to county.

*Hypothesis: Harder hit counties are poorer and more racially diverse.*

We also wanted to see what the correlation is between Wall St and Main St. We know that the stock market crashed pretty severely but is picking back up again, which is disconnected from the way every day people are dealing with COVID-19 since cases have yet to decrease.

*Hypothesis: The stimulus has a stabilizing effect on the market, even though cases are still rising.*

### Instructions
1. Open app/module folder in terminal or Git Bash.
2. Run **python load_mongo_db.py**. 
3. Open app folder.
4. Run **python app.py**. 
5. Open browser window and type http://127.0.0.1:5000/

### Some Considerations
All of the data was collected on May 22nd, and was analyzed for that date.

## The analysis was done using the ETL model.
![approach.png](app/static/img/approach.png)

## Extract
We downloaded our data from different sources. We use Census data from the <a href="https://www.labor.ny.gov/stats/nys/statewide-population-data.shtm">NY Dept of Labor</a>, the Dow Jones Index from <a href="https://finance.yahoo.com/quote/%5EDJI/history?p=%5EDJI">Yahoo Finance</a>, COVID cases and deaths from <a href="https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/">USA Facts</a>, Free and Reduced-price Lunch data from <a href="https://www.nyskwic.org/get_data/indicator_data.cfm">NY State KWIC</a>, NY County Median Income by Race from the <a href="https://www.census.gov/topics/income-poverty/income/data/tables.html">Census Bureau</a>,and the GeoJSON for NY Counties from <a href="https://github.com/johan/world.geo.json/tree/master/countries/USA/NY">Github</a>.

## Transform
1. We used `VBA` to do a basic clean
2. We loaded everything into `Postgres DB` for more extensive cleaning and combining of data sources.
3. Then in `Jupyter Notebook` we used `Pandas` and the `OS` module to import our CSVs and do a final cleaning of column names, once we finalized the datasets we needed.
4. And then we performed a final a merge of all the columns into one master dataset.
5. Lastly, we used `pymongo` and `MongoClient` to create dictionaries of all our records and then load it into `Mongo DB`.

## Load
The final data was stored in a `Mongo` database, which was pulled from to obtain our demogrpahic and socio-economic results.

We used the micro-framework `Flask` inside of `Python` to create our website that would showcase our data. `Leaflet JS` and `Mapbox API` were used in `HTML` to create the map of our counties with the COVID case data used for coloring. Both the `Bootstrap`, and `ChartJS` libraries were used to beautify our website and create dynamic graphs.

![map.png](app/static/img/map.png)

![charts.png](app/static/img/charts.png)

## Final Results & Analysis
In general, our hypothesis is correct: as harder hit counties are more racially diverse and economically poor.

In the graphs presented here we'll compare Queens (the worst-hit county) with Hamilton (the least-hit county):

### Demographics
Queens is a lot **more** racially diverse compared to the state statistics.
![demoQ.png](app/static/img/demoQ.png)
Hamilton is a lot **less** racially diverse compared to the state statistics.
![demoH.png](app/static/img/demoH.png)

### Cases/Deaths & Poverty Levels
Queens had **60,236** COVID cases and has almost **double** the poverty level of the state.
![povQ.png](app/static/img/povQ.png)
Hamilton had **5** COVID cases and has almost **half** the poverty level of the state.
![povH.png](app/static/img/povH.png)

