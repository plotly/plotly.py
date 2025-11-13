---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.10.0
  plotly:
    description: How to specify country codes, names, and US states for outline-based
      maps
    display_as: maps
    language: python
    layout: base
    name: Locations for Outline-based Maps
    order: 15
    page_type: example_index
    permalink: python/outline-map-locations/
    thumbnail: thumbnail/choropleth.jpg
---

# Locations for Outline-based Maps

With outline-based maps, you can visualize data for specific regions using the `locations` and `locationmode` parameters.

The following map types in `plotly.express` and `plotly.graph_objects` support these parameters:

- `px.choropleth` - color regions based on data values
- `px.scatter_geo` - show markers at geographic locations
- `px.line_geo` - draw lines connecting geographic locations
- `go.Choropleth` - choropleth trace for coloring regions
- `go.Scattergeo` - geographic scatter/line trace for markers and lines

The `locations` parameter accepts region identifiers (such as `['CA', 'TX', 'NY']`, a pandas Series, or array-like), and the `locationmode` parameter controls how those identifiers are interpreted:

- `'ISO-3'` - three-letter ISO country codes (for example, `'USA'`, `'CAN'`, `'GBR'`)
- `'USA-states'` - two-letter US state abbreviations (for example, `'CA'`, `'TX'`, `'NY'`)
- `'country names'` - full country names (for example, `'United States'`)


## locationmode='ISO-3'

Set `locationmode='ISO-3'` to use three-letter ISO country codes in `locations`.

```python
import plotly.express as px

fig = px.choropleth(
    locations=['USA', 'CAN', 'MEX', 'BRA', 'RUS'],
    locationmode='ISO-3',
    color=[100, 85, 72, 95, 68],
    color_continuous_scale='Viridis',
    title='Choropleth with ISO-3 Country Codes'
)
fig.show()
```

## Supported ISO Codes

The following ISO codes are supported when `locationmode='ISO-3'`:

| Name | ISO Code |
|------|----------|
| Afghanistan | AFG |
| Aksai Chin | XAC |
| Åland Islands | ALA |
| Albania | ALB |
| Algeria | DZA |
| American Samoa | ASM |
| Andorra | AND |
| Angola | AGO |
| Anguilla | AIA |
| Antarctica | ATA |
| Antigua and Barbuda | ATG |
| Argentina | ARG |
| Armenia | ARM |
| Aruba | ABW |
| Arunachal Pradesh | XAP |
| Australia | AUS |
| Austria | AUT |
| Azerbaijan | AZE |
| Azores Islands | PRT |
| Bahamas | BHS |
| Bahrain | BHR |
| Bangladesh | BGD |
| Barbados | BRB |
| Belarus | BLR |
| Belgium | BEL |
| Belize | BLZ |
| Benin | BEN |
| Bermuda | BMU |
| Bhutan | BTN |
| Bir Tawil | XBT |
| Bolivia (Plurinational State of) | BOL |
| Bonaire | BES |
| Bosnia and Herzegovina | BIH |
| Botswana | BWA |
| Bouvet Island | BVT |
| Brazil | BRA |
| British Virgin Islands | VGB |
| Brunei Darussalam | BRN |
| Bulgaria | BGR |
| Burkina Faso | BFA |
| Burundi | BDI |
| Cabo Verde | CPV |
| Cambodia | KHM |
| Cameroon | CMR |
| Canada | CAN |
| Canary Islands | ESP |
| Cayman Islands | CYM |
| Central African Republic | CAF |
| Chad | TCD |
| Chagos Archipelago | MUS |
| Chile | CHL |
| China | CHN |
| Christmas Island | CXR |
| Cocos (Keeling) Islands | CCK |
| Colombia | COL |
| Comoros | COM |
| Congo | COG |
| Cook Islands | COK |
| Costa Rica | CRI |
| Côte d'Ivoire | CIV |
| Croatia | HRV |
| Cuba | CUB |
| Curaçao | CUW |
| Cyprus | CYP |
| Czechia | CZE |
| Democratic People's Republic of Korea | PRK |
| Democratic Republic of the Congo | COD |
| Denmark | DNK |
| Djibouti | DJI |
| Dominica | DMA |
| Dominican Republic | DOM |
| Ecuador | ECU |
| Egypt | EGY |
| El Salvador | SLV |
| Equatorial Guinea | GNQ |
| Eritrea | ERI |
| Estonia | EST |
| Eswatini | SWZ |
| Ethiopia | ETH |
| Falkland Islands (Malvinas) | FLK |
| Faroe Islands | FRO |
| Fiji | FJI |
| Finland | FIN |
| France | FRA |
| French Guiana | GUF |
| French Polynesia | PYF |
| French Southern Territories | ATF |
| Gabon | GAB |
| Galápagos Islands | ECU |
| Gambia | GMB |
| Gaza | PSE |
| Georgia | GEO |
| Germany | DEU |
| Ghana | GHA |
| Gibraltar | GIB |
| Greece | GRC |
| Greenland | GRL |
| Grenada | GRD |
| Guadeloupe | GLP |
| Guam | GUM |
| Guatemala | GTM |
| Guernsey | GGY |
| Guinea | GIN |
| Guinea-Bissau | GNB |
| Guyana | GUY |
| Haiti | HTI |
| Halaib Triangle | XHT |
| Heard Island and McDonald Islands | HMD |
| Honduras | HND |
| Hong Kong | HKG |
| Hungary | HUN |
| Iceland | ISL |
| Ilemi Triangle | XIT |
| India | IND |
| Indonesia | IDN |
| Iran (Islamic Republic of) | IRN |
| Iraq | IRQ |
| Ireland | IRL |
| Isle of Man | IMN |
| Israel | ISR |
| Italy | ITA |
| Jamaica | JAM |
| Jammu and Kashmir | XJK |
| Japan | JPN |
| Jersey | JEY |
| Jordan | JOR |
| Kazakhstan | KAZ |
| Kenya | KEN |
| Kingdom of the Netherlands | NLD |
| Kiribati | KIR |
| Kuwait | KWT |
| Kyrgyzstan | KGZ |
| Lao People's Democratic Republic | LAO |
| Latvia | LVA |
| Lebanon | LBN |
| Lesotho | LSO |
| Liberia | LBR |
| Libya | LBY |
| Liechtenstein | LIE |
| Lithuania | LTU |
| Luxembourg | LUX |
| Macao | MAC |
| Madagascar | MDG |
| Madeira Island | PRT |
| Malawi | MWI |
| Malaysia | MYS |
| Maldives | MDV |
| Mali | MLI |
| Malta | MLT |
| Marshall Islands | MHL |
| Martinique | MTQ |
| Mauritania | MRT |
| Mauritius | MUS |
| Mayotte | MYT |
| Mexico | MEX |
| Micronesia (Federated States of) | FSM |
| Monaco | MCO |
| Mongolia | MNG |
| Montenegro | MNE |
| Montserrat | MSR |
| Morocco | MAR |
| Mozambique | MOZ |
| Myanmar | MMR |
| Namibia | NAM |
| Nauru | NRU |
| Nepal | NPL |
| New Caledonia | NCL |
| New Zealand | NZL |
| Nicaragua | NIC |
| Niger | NER |
| Nigeria | NGA |
| Niue | NIU |
| Norfolk Island | NFK |
| North Macedonia | MKD |
| Northern Mariana Islands | MNP |
| Norway | NOR |
| Oman | OMN |
| Pakistan | PAK |
| Palau | PLW |
| Panama | PAN |
| Papua New Guinea | PNG |
| Paraguay | PRY |
| Peru | PER |
| Philippines | PHL |
| Pitcairn | PCN |
| Poland | POL |
| Portugal | PRT |
| Puerto Rico | PRI |
| Qatar | QAT |
| Republic of Korea | KOR |
| Republic of Moldova | MDA |
| Réunion | REU |
| Romania | ROU |
| Russian Federation | RUS |
| Rwanda | RWA |
| Saba | BES |
| Saint Barthélemy | BLM |
| Saint Helena | SHN |
| Saint Kitts and Nevis | KNA |
| Saint Lucia | LCA |
| Saint Martin | MAF |
| Saint Pierre and Miquelon | SPM |
| Saint Vincent and the Grenadines | VCT |
| Samoa | WSM |
| Sao Tome and Principe | STP |
| Saudi Arabia | SAU |
| Senegal | SEN |
| Serbia | SRB |
| Seychelles | SYC |
| Sierra Leone | SLE |
| Singapore | SGP |
| Sint Eustatius | BES |
| Sint Maarten | SXM |
| Slovakia | SVK |
| Slovenia | SVN |
| Solomon Islands | SLB |
| Somalia | SOM |
| South Africa | ZAF |
| South Georgia and the South Sandwich Islands | SGS |
| South Sudan | SSD |
| Spain | ESP |
| Sri Lanka | LKA |
| Sudan | SDN |
| Suriname | SUR |
| Svalbard and Jan Mayen Islands | SJM |
| Sweden | SWE |
| Switzerland | CHE |
| Syrian Arab Republic | SYR |
| Taiwan | TWN |
| Tajikistan | TJK |
| Thailand | THA |
| Timor-Leste | TLS |
| Togo | TGO |
| Tokelau | TKL |
| Tonga | TON |
| Trinidad and Tobago | TTO |
| Tunisia | TUN |
| Türkiye | TUR |
| Turkmenistan | TKM |
| Turks and Caicos Islands | TCA |
| Tuvalu | TUV |
| Uganda | UGA |
| Ukraine | UKR |
| United Arab Emirates | ARE |
| United Kingdom of Great Britain and Northern Ireland | GBR |
| United Republic of Tanzania | TZA |
| United States of America | USA |
| United States Virgin Islands | VIR |
| Uruguay | URY |
| Uzbekistan | UZB |
| Vanuatu | VUT |
| Venezuela (Bolivarian Republic of) | VEN |
| Viet Nam | VNM |
| West Bank | PSE |
| Western Sahara | ESH |
| Yemen | YEM |
| Zambia | ZMB |
| Zimbabwe | ZWE |


## locationmode='USA-states'

Set `locationmode='USA-states'` to use two-letter US state abbreviations in `locations`.

```python
import plotly.express as px

fig = px.choropleth(
    locations=['CA', 'TX', 'NY', 'FL', 'IL'],
    locationmode='USA-states',
    color=[95, 88, 92, 85, 78],
    scope='usa',
    color_continuous_scale='Reds',
    title='USA States Choropleth'
)
fig.show()
```

## Supported US State Codes

The following state codes are supported when `locationmode='USA-states'`:

| State | Code |
|-------|------|
| Alabama | AL |
| Alaska | AK |
| Arizona | AZ |
| Arkansas | AR |
| California | CA |
| Colorado | CO |
| Connecticut | CT |
| Delaware | DE |
| District of Columbia | DC |
| Florida | FL |
| Georgia | GA |
| Hawaii | HI |
| Idaho | ID |
| Illinois | IL |
| Indiana | IN |
| Iowa | IA |
| Kansas | KS |
| Kentucky | KY |
| Louisiana | LA |
| Maine | ME |
| Maryland | MD |
| Massachusetts | MA |
| Michigan | MI |
| Minnesota | MN |
| Mississippi | MS |
| Missouri | MO |
| Montana | MT |
| Nebraska | NE |
| Nevada | NV |
| New Hampshire | NH |
| New Jersey | NJ |
| New Mexico | NM |
| New York | NY |
| North Carolina | NC |
| North Dakota | ND |
| Ohio | OH |
| Oklahoma | OK |
| Oregon | OR |
| Pennsylvania | PA |
| Rhode Island | RI |
| South Carolina | SC |
| South Dakota | SD |
| Tennessee | TN |
| Texas | TX |
| Utah | UT |
| Vermont | VT |
| Virginia | VA |
| Washington | WA |
| West Virginia | WV |
| Wisconsin | WI |
| Wyoming | WY |


## locationmode='country names'

Set `locationmode='country names'` to use full country names in `locations`.

```python
import plotly.express as px

fig = px.choropleth(
    locations=['United States', 'Canada', 'United Kingdom'],
    locationmode='country names'
)
fig.show()
```

> How Plotly matches 'country names' will change in a future version. Matching will become stricter and some country names may no longer match. We recommend using `locationmode='ISO-3'` with ISO codes for `locations` to ensure consistent behavior across versions.

```python
import plotly.express as px

fig = px.choropleth(
    locations=['USA', 'CAN', 'GBR'],
    locationmode='ISO-3'
)
fig.show()
```

## Using Different Data Types with `locations`

Earlier examples demonstrated using the `locations` parameter with Python lists. The `locations` parameter also accepts column names from DataFrames, pandas Series, or other array-like objects.

Here's an example that uses a column from the gapminder dataset with `locations`:

```python
import plotly.express as px

df = px.data.gapminder().query("year == 2007")

fig = px.choropleth(
    df,
    locations='iso_alpha',
    locationmode='ISO-3',
    color='lifeExp',
    hover_name='country',
    color_continuous_scale='Viridis',
    title='Life Expectancy by Country (2007)'
)
fig.show()
```
