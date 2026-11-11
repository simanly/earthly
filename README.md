# 🌍 Earthly --- Field Shift

### Adapting Farms with NASA Data

**Earthly** is a multidisciplinary team participating in the **NASA
International Space Apps Challenge 2026**. Our project, **Field Shift**,
explores how NASA Earth observation data, environmental information,
GIS, and artificial intelligence can support more informed agricultural
decisions.

Our goal is to help farmers understand the conditions of their land,
compare agricultural regions, explore suitable crops, and become more
prepared for environmental risks.

> **Project focus:** Turning Earth observation data into practical
> insights for more resilient and sustainable agriculture.

------------------------------------------------------------------------

## 🌱 The Challenge

Farmers face changing temperatures, shifting rainfall patterns, water
shortages, extreme weather, and declining soil health. These conditions
make it difficult to choose crops and plan agricultural activities with
confidence.

Field Shift addresses this challenge by bringing together environmental
data, regional information, and decision-support tools in one platform.
It is designed to help users explore how local conditions affect
agricultural potential and what risks may need attention.

## 💡 Our Solution

Field Shift is an agriculture-focused decision-support platform with an
initial focus on Azerbaijan.

The platform is designed to:

-   Explore environmental conditions across agricultural regions.
-   Present weather and soil-related indicators.
-   Compare regions and crop suitability.
-   Show historical environmental patterns and future projections when
    data is available.
-   Highlight potential agricultural risks.
-   Provide understandable recommendations to support farmers'
    decisions.

Field Shift is intended to support decision-making. It does not replace
local agricultural expertise, field measurements, or professional
agronomic advice.

------------------------------------------------------------------------

## ✨ Key Features

### 🗺️ Interactive Regional Map

Explore Azerbaijan on an interactive map, select regions, and view
available regional indicators. Map markers in the current prototype
represent approximate city locations; they should not be interpreted as
precise field boundaries.

### 🌦️ Weather and Environmental Overview

View available weather information and environmental indicators such as
temperature, precipitation, and soil moisture.

### 🌾 Crop Suitability

Explore a ranked list of potentially suitable crops based on available
environmental inputs. The current prototype includes a **demo
recommendation engine**; its scores are illustrative and are not
validated agricultural predictions.

### 📊 Regional Comparison and Statistics

The planned analytics experience allows users to compare regions, crops,
productivity indicators, and environmental conditions.

### ⚠️ Risk Monitoring

The platform is designed to highlight potential environmental risks and
provide practical guidance. Live risk alerts require reliable data feeds
and validated detection logic.

### 🛰️ Earth Observation Data

Field Shift is designed around NASA Earth science and Earth observation
resources. NASA POWER data is available live where the service responds;
other satellite-data integrations are part of the planned development.

### 👩‍🌾 Farmer-focused Tools

Planned features include individual farmer accounts, field management,
notifications, an AI agricultural assistant, and a farmer community with
ratings and reviews.

------------------------------------------------------------------------

## 🛰️ Data Sources

Field Shift is designed to work with open Earth observation and
environmental datasets, including:

  ----------------------------------------------------------------------------
  Data source                                   Intended use
  --------------------------------------------- ------------------------------
  [NASA POWER](https://power.larc.nasa.gov/)    Meteorological and solar data

  [NASA SMAP](https://smap.jpl.nasa.gov/)       Soil moisture observations

  [MODIS](https://modis.gsfc.nasa.gov/)         Vegetation and land-surface
                                                observations

  [Landsat](https://landsat.gsfc.nasa.gov/)     Land observation and satellite
                                                imagery

  [NASA                                         Discovery and access to NASA
  Earthdata](https://www.earthdata.nasa.gov/)   Earth science data
  ----------------------------------------------------------------------------

**Data transparency:** Not every source listed above is necessarily
connected in the current prototype. The interface should distinguish
live data, cached data, historical observations, forecasts, and demo or
simulated values. Data source and observation dates should be shown
wherever possible.

------------------------------------------------------------------------

## 🧠 How It Works

1.  **Select a region** --- explore an agricultural area on the map.
2.  **Review available conditions** --- inspect weather and
    environmental indicators.
3.  **Analyze crop suitability** --- compare potential crops using the
    available inputs.
4.  **Compare regions** --- explore differences in environmental
    conditions and agricultural indicators.
5.  **Monitor risks** --- review potential threats and recommendations
    as monitoring capabilities become available.

------------------------------------------------------------------------

## 🧰 Technology

The project is being developed as a web-based application. The intended
technical direction includes:

-   **Frontend:** React, TypeScript, Vite, Tailwind CSS
-   **Mapping / GIS:** Leaflet, React Leaflet, PostGIS
-   **Backend:** Python, FastAPI
-   **Data processing:** Pandas, NumPy
-   **Machine Learning:** Scikit-learn, Random Forest, XGBoost (subject
    to suitable training data and validation)
-   **Database:** PostgreSQL
-   **Visualization:** Recharts
-   **Data integration:** NASA open-data services and APIs

The exact technologies and integrations available in a particular
release should be confirmed in the source code and project
configuration.

------------------------------------------------------------------------

## 🚧 Development Status

Field Shift is under active development. The current prototype
demonstrates the core concept through a regional map, regional
environmental indicators, NASA POWER data where available, and a demo
crop-suitability engine.

The following capabilities are part of the development roadmap and
should not be considered complete until implemented and tested:

-   User registration, login, and personal accounts
-   PostgreSQL/PostGIS persistence and database migrations
-   Farmer field management
-   Full historical analytics and forecast pages
-   Regional rankings and detailed comparisons
-   Farmer profiles, community features, and reviews
-   SMS notifications through a configured provider
-   SMAP, MODIS, and Landsat data integrations
-   Validated machine-learning crop recommendations
-   AI agricultural assistant
-   Automated risk monitoring and alert delivery

We aim to implement these capabilities incrementally and clearly label
demo functionality until it is backed by verified data and working
integrations.

------------------------------------------------------------------------

## ▶️ Running the Project

The exact setup commands depend on the current repository
implementation.

1.  Clone the repository:

    ``` bash
    git clone https://github.com/<YOUR-GITHUB-USERNAME>/earthly.git
    cd earthly
    ```

2.  Review the project files and the relevant setup instructions in the
    frontend and backend directories.

3.  Configure environment variables using the provided `.env.example`,
    if available.

4.  Install the dependencies listed by the project.

5.  Start the backend and frontend using the commands documented in
    their respective directories.

> **Note:** Do not commit `.env` files, passwords, API keys, access
> tokens, or other secrets to GitHub. Use environment variables and keep
> `.env.example` limited to placeholder values.

------------------------------------------------------------------------

## 👥 Team Earthly

We are a multidisciplinary team combining environmental engineering,
computer science, and process automation. We bring together science,
technology, and creativity to explore new possibilities, use data to
solve problems, and transform ideas into meaningful projects for a
healthier Earth and a better future for humanity.

  ----------------------------------------------------------------------------------
  Team member                 GitHub / Space Apps handle
  --------------------------- ------------------------------------------------------
  Omar Davudov                [@davudoff](https://github.com/davudoff)

  Orkhan Ragimov              [@orkhan_ragimov](https://github.com/orkhan_ragimov)

  Abdulla Abdullazade         [@abdullaxows](https://github.com/abdullaxows)

  Nijat Hatamli               [@nijathatamli](https://github.com/nijathatamli)

  Safiyya Imanli              [@sofa_imanly](https://github.com/sofa_imanly)

  Fatima Talibova             [@fatimatalibova](https://github.com/fatimatalibova)
  ----------------------------------------------------------------------------------

**Local event:** Baku, Azerbaijan\
**Challenge:** Field Shift --- Adapting Farms with NASA Data

------------------------------------------------------------------------

## 🌍 Our Mission

We believe that accessible Earth observation data can help communities
better understand environmental change and make more informed decisions.

With Field Shift, we want to connect satellite intelligence with the
everyday needs of farmers --- making agricultural information easier to
explore, compare, and act upon.

**Explore the Earth. Understand the land. Help farms adapt.**

------------------------------------------------------------------------

## 📄 Acknowledgements

We acknowledge NASA and the providers of open Earth observation datasets
for making scientific data accessible to innovators, researchers, and
communities.

This project was created as part of the **NASA International Space Apps
Challenge 2026**.

Field Shift is an independent participant project and is not an official
NASA product. NASA's name and data are referenced to identify data
sources and the challenge context; this project is not endorsed by NASA.
