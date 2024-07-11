## Business case
Client: European Union

The European Union wants to evaluate their ambitious goal for energy production from renewable energies to make up 42% of the consumption by 2030.
They want to know what are the current status of renewable energy production in EU.
With this input, they want to evaluate what kinds of policy or actions they need to do to improve the renewable energy production in some countries, especially for countries which are left behind.

### Hypothesis 1: Renewable Energy Adoption Correlates with GDP per Capita
Hypothesis: Countries with higher GDP per capita tend to have higher adoption rates of renewable energy sources.
Rationale: Wealthier nations may have more resources to invest in renewable energy infrastructure and technologies.

### Hypothesis 2: Geographic and Climate Influences on Renewable Energy
Hypothesis: Countries with more favorable geographic and climate conditions (e.g., sunlight for solar, wind patterns for wind energy) have higher proportions of renewable energy production.
Rationale: Natural resources play a significant role in the feasibility and profitability of renewable energy projects.

### Hypothesis 3: Technological Innovation and Renewable Energy Growth
Hypothesis: Countries that invest more in research and development (R&D) in renewable energy technologies demonstrate faster growth in renewable energy production.
Rationale: Innovation in technology can lead to more efficient and cost-effective renewable energy solutions.


## Data

* Global Electricity Production: [Kaggle](https://www.kaggle.com/datasets/sazidthe1/global-electricity-production) (121k rows, 6 columns)
* Area of EU Countries: [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/reg_area3__custom_11352231/bookmark/table?lang=en&bookmarkId=fabcfca6-4abb-4a84-ac1c-7bb335af436a)
* Population of EU Countries: [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/DEMO_GIND__custom_7127262/default/table)
* GDP per Capita of EU Countries: [Word Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)
* R&D investments of EU Countries: [Internationl Energy Agency](https://www.iea.org/data-and-statistics/data-tools/energy-technology-rdd-budgets-data-explorer)
* Average Annual Solar Radiation: [Article by M. Uyan & O.L. Dogmus](https://www.researchgate.net/figure/Average-annual-global-solar-radiation-in-Europe-20_fig2_366202104)



## Hypothesis 2
Countries with more favorable geographic and climate conditions (e.g., sunlight for solar, wind patterns for wind energy) have higher proportions of renewable energy production. Due to limited time resources, we reduced the scope to solar electricity production and its correlation to the countries' solar radiation exposure.

#### Country Solar Radiation Categorization
In order to visualize the Country Solar Radiation Categorization, a map is created, which depicts all considered countries in a color depending on their respective category. The colors are defined in a way, so that green represents countries with low solar radiation, and red represents countries with high solar radiation. The categorization itself is defined further above. In subsequent charts, the countries' categories are indicated by applying the colormap to the color of the bars.

![Country Solar Categorization](/img/country_categorization_by_solar_radiation.png)

#### Average Annual Solar Net Electricity Production per Category
In order to verify the hypothesis, the average annual electricity production exploiting solar radiation per squarekilometer is calculated for each country in the EU. The figure below displays the data aggregated per radiation category.

Countries categorized for higher radiation tend to have higher solar electricity production rates. Countries in the category "low", however, on average have a higher solar electricity production rate than countries in the categories "medium" or "high".

![Solar Production per Area by Category](/img/solar_production_per_country_radiation_categories_aggregated.png)

#### Average Annual Solar Net Electricity Production per Country
In order to investigate the above findings further, the figure bwloe shows the same data, but without category aggregation and separately for each country instead.

It can be seen, that the "low"-radiation countries' solar electricity production rates are dominated by three countries: Netherlands, Belgium and Germany. Each one of these show a higher rate than the "very high"-radiation countries Spain and Cyprus. In the "very low"-radiation category, Denmark shows a solar rate comparable to the ones of "medium"-radiation. The country with the highest solar rate per area by far is the "very high"-radiation country Malta. 

![Solar Production per Area by Category](/img/solar_production_per_area.png)
