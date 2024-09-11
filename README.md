## Introduction

Sustainergy Advisory Firm has a mission to help EU countries to fasten renewable energy adoption, so, they can reach European Union's ambitious goal to make up 42% renewable energy by 2030. 

We aim to approach the right government in EU countries as our future client who is still left behind in reaching that target. In order to find the right client with right approach, we identify these problem statements and hypotheses:

**Problem 1**: The company is uncertain regarding the appropriate governmental entity to contact.<br>
**Hypothesis 1**: Countries with higher GDP are more likely to invest in renewable energy sources and tend to have a higher percentage of renewable energy production.

**Problem 2**: The company lacks clarity on the most suitable renewable energy source to recommend to our prospective client..<br>
**Hypothesis 2**: the best renewable energy source will be related to natural resources which depends on country's geographic and climate conditions.

**Problem 3**: The company seeks to understand if the limited adoption of renewable energy is related to low investment on innovation in technology.<br>
**Hypothesis 3**: Countries that invest more in research and development (R&D) in renewable energy technologies demonstrate faster growth in renewable energy production.

## Data

* Global Electricity Production: [Kaggle](https://www.kaggle.com/datasets/sazidthe1/global-electricity-production) (121k rows, 6 columns)
* Area of EU Countries: [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/reg_area3__custom_11352231/bookmark/table?lang=en&bookmarkId=fabcfca6-4abb-4a84-ac1c-7bb335af436a)
* Population of EU Countries: [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/DEMO_GIND__custom_7127262/default/table)
* GDP per Capita of EU Countries: [Word Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)
* R&D investments of EU Countries: [Internationl Energy Agency](https://www.iea.org/data-and-statistics/data-tools/energy-technology-rdd-budgets-data-explorer)
* Average Annual Solar Radiation: [Article by M. Uyan & O.L. Dogmus](https://www.researchgate.net/figure/Average-annual-global-solar-radiation-in-Europe-20_fig2_366202104)

## Hypothesis 1
The scatterplot visualizaton was performed to show the relationship between GDP and the percentage of renewable energy production for EU countries in 2010-2023. 
![Correlation GDP and % of renevable energy adoption](https://github.com/NGravereaux/project1_main/blob/master/img/Correlation%20between%20GDP%20per%20capita%20and%20%25%20of%20Renewable%20energy%20production.png)
The trendline indicates a positive correlation between GDP and the percentage of renewable energy. 
This means that, on average, countries with higher GDP tend to have a higher percentage of renewable energy production.
The positive trend suggests that economically developed countries are more likely to invest in renewable energy sources. 
This could be due to higher availability of funds for infrastructure, more advanced technology, and stronger policy frameworks supporting renewable energy.
Despite the positive trend, data varies. Countries with low GDP have a wide range of renewable energy percentages, from very low to very high. In countries with high GDP, the renewable energy percentages also vary, but less so.

## Hypothesis 2
Countries with more favorable geographic and climate conditions (e.g., sunlight for solar, wind patterns for wind energy) have higher proportions of renewable energy production. Due to limited time resources, we reduced the scope to solar electricity production and its correlation to the countries' solar radiation exposure.

#### Country Solar Radiation Categorization
Each considered country is categorized by its solar radiation exposure following data on the average annual GHI (Global Horizontal Irradiance) in the period between 1994 and 2016. The map below dsiplays the countries in a color depending on their respective category. Green represents countries with low solar radiation, and red represents countries with high solar radiation.

![Country Solar Categorization](/img/country_categorization_by_solar_radiation.png)

#### Average Annual Solar Net Electricity Production per Category
In order to verify the hypothesis, the average annual electricity production exploiting solar radiation per squarekilometer is calculated for each country in the EU. The figure below displays the data aggregated per radiation category.

Countries categorized for higher radiation tend to have higher solar electricity production rates. Countries in the category "low", however, on average have a higher solar electricity production rate than countries in the categories "medium" or "high".

![Solar Production per Area by Category](/img/solar_production_per_country_radiation_categories_aggregated.png)

#### Average Annual Solar Net Electricity Production per Country
In order to investigate the above findings further, the figure bwloe shows the same data, but without category aggregation and separately for each country instead.

It can be seen, that the "low"-radiation countries' solar electricity production rates are dominated by three countries: Netherlands, Belgium and Germany. Each one of these show a higher rate than the "very high"-radiation countries Spain and Cyprus. In the "very low"-radiation category, Denmark shows a solar rate comparable to the ones of "medium"-radiation. The country with the highest solar rate per area by far is the "very high"-radiation country Malta. 

![Solar Production per Area by Category](/img/solar_production_per_area.png)

## Hypothesis 3
In this section, we would like to understand whether the reason of low renewable energy adoption is related to low investment on innovation in technology.

We need three dataframes to prove Hypothesis 3 which consist of:
- dataframe of renewable energy production of the EU countries for the past 10 years.
- dataframe of R&D budget of the EU countries for the past 10 years.
- dataframe of EU population.

The figure below shows correlation between renewable energy production and R&D budget per capita in the past 10 years of some European countries. It is shown that there is positive correlation between them. 

![Correlation between RE Production and R&D Budget per Capita](/img/RE_production_vs_RnD_budget.png)

## Conclusion
1. Hypothesis 1: There is a positive correlation between GDP and the percentage of renewable energy production.
   - Insight: Countries with high GDP but low renewable energy adoption are ideal candidates for our advisory services. 

2. Hypothesis 2: Countries with high solar radiation exposure still have a significant potential for improvement in solar electricity production.
   - Insight:  Countries with high solar radiation exposure but low solar electricity production are good candidate to boost solar energy utilization.

3. Hypothesis 3: There is a positive correlation between renewable energy production and the R&D budget in renewable energy technology.
   - Insight: Increasing R&D funding in renewable energy technologies could enhance renewable energy adoption rates.
  
[Link to Presentation](https://www.canva.com/design/DAGKcPKatDE/zVbcXmfEA61tLzb1q8lX-Q/edit)
