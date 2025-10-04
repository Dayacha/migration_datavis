# Daniela Ayala Chavez 

## Geographic Hotspot Identification for migration factors

## Description
This project will explore how visualization and spatial analytics can reveal geographic “hotspots” of migration risk using open data. The core idea is to combine multiple socioeconomic and environmental indicators — such as poverty, unemployment, education levels, remittances, and climate risk — into a composite migration-risk score for each region.

## Data Sources

### World Development Indicators
- URL: [https://databank.worldbank.org/source/world-development-indicators](https://databank.worldbank.org/source/world-development-indicators)
- Size: ~1,400 indicators across 200+ countries, time series (1960–2024)
- Includes socioeconomic indicators (GDP per capita, unemployment rate, remittances, education, health) that can be used to identify structural vulnerabilities influencing migration.

### International Organization for Migration (IOM) – Migration Data Portal
- URL: [https://migrationdataportal.org/](https://lac.iom.int/en/data-and-resources)
- Size: Country-level migration flows and stock estimates (2010–2023)
- Provides migration inflows/outflows, remittances, and return migration data across countries and subregions, useful for establishing baseline migration trends.

## Questions

1. How can the interactive dashboard allow users to dynamically weight indicators (e.g., economic vs. environmental) and immediately visualize changes in hotspot classification?
2. What normalization and feature-scaling strategies ensure comparability of indicators across countries and time periods?
3. How difficult would it be to integrate national statistical data from each country to achieve municipality-level granularity, and what preprocessing or alignment steps would be required to harmonize those datasets?
4. Is it feasible to map municipalities directly for each country, or would this require obtaining and joining administrative boundary shapefiles (e.g., from GADM or GeoBoundaries) with each dataset’s geographic identifiers?
