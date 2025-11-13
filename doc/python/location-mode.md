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

<table style="text-align: left;">
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">ISO Code</th>
</tr>
</thead>
<tbody>
<tr><td>Afghanistan</td><td>AFG</td></tr>
<tr><td>Aksai Chin</td><td>XAC</td></tr>
<tr><td>Åland Islands</td><td>ALA</td></tr>
<tr><td>Albania</td><td>ALB</td></tr>
<tr><td>Algeria</td><td>DZA</td></tr>
<tr><td>American Samoa</td><td>ASM</td></tr>
<tr><td>Andorra</td><td>AND</td></tr>
<tr><td>Angola</td><td>AGO</td></tr>
<tr><td>Anguilla</td><td>AIA</td></tr>
<tr><td>Antarctica</td><td>ATA</td></tr>
<tr><td>Antigua and Barbuda</td><td>ATG</td></tr>
<tr><td>Argentina</td><td>ARG</td></tr>
<tr><td>Armenia</td><td>ARM</td></tr>
<tr><td>Aruba</td><td>ABW</td></tr>
<tr><td>Arunachal Pradesh</td><td>XAP</td></tr>
<tr><td>Australia</td><td>AUS</td></tr>
<tr><td>Austria</td><td>AUT</td></tr>
<tr><td>Azerbaijan</td><td>AZE</td></tr>
<tr><td>Azores Islands</td><td>PRT</td></tr>
<tr><td>Bahamas</td><td>BHS</td></tr>
<tr><td>Bahrain</td><td>BHR</td></tr>
<tr><td>Bangladesh</td><td>BGD</td></tr>
<tr><td>Barbados</td><td>BRB</td></tr>
<tr><td>Belarus</td><td>BLR</td></tr>
<tr><td>Belgium</td><td>BEL</td></tr>
<tr><td>Belize</td><td>BLZ</td></tr>
<tr><td>Benin</td><td>BEN</td></tr>
<tr><td>Bermuda</td><td>BMU</td></tr>
<tr><td>Bhutan</td><td>BTN</td></tr>
<tr><td>Bir Tawil</td><td>XBT</td></tr>
<tr><td>Bolivia (Plurinational State of)</td><td>BOL</td></tr>
<tr><td>Bonaire</td><td>BES</td></tr>
<tr><td>Bosnia and Herzegovina</td><td>BIH</td></tr>
<tr><td>Botswana</td><td>BWA</td></tr>
<tr><td>Bouvet Island</td><td>BVT</td></tr>
<tr><td>Brazil</td><td>BRA</td></tr>
<tr><td>British Virgin Islands</td><td>VGB</td></tr>
<tr><td>Brunei Darussalam</td><td>BRN</td></tr>
<tr><td>Bulgaria</td><td>BGR</td></tr>
<tr><td>Burkina Faso</td><td>BFA</td></tr>
<tr><td>Burundi</td><td>BDI</td></tr>
<tr><td>Cabo Verde</td><td>CPV</td></tr>
<tr><td>Cambodia</td><td>KHM</td></tr>
<tr><td>Cameroon</td><td>CMR</td></tr>
<tr><td>Canada</td><td>CAN</td></tr>
<tr><td>Canary Islands</td><td>ESP</td></tr>
<tr><td>Cayman Islands</td><td>CYM</td></tr>
<tr><td>Central African Republic</td><td>CAF</td></tr>
<tr><td>Chad</td><td>TCD</td></tr>
<tr><td>Chagos Archipelago</td><td>MUS</td></tr>
<tr><td>Chile</td><td>CHL</td></tr>
<tr><td>China</td><td>CHN</td></tr>
<tr><td>Christmas Island</td><td>CXR</td></tr>
<tr><td>Cocos (Keeling) Islands</td><td>CCK</td></tr>
<tr><td>Colombia</td><td>COL</td></tr>
<tr><td>Comoros</td><td>COM</td></tr>
<tr><td>Congo</td><td>COG</td></tr>
<tr><td>Cook Islands</td><td>COK</td></tr>
<tr><td>Costa Rica</td><td>CRI</td></tr>
<tr><td>Côte d'Ivoire</td><td>CIV</td></tr>
<tr><td>Croatia</td><td>HRV</td></tr>
<tr><td>Cuba</td><td>CUB</td></tr>
<tr><td>Curaçao</td><td>CUW</td></tr>
<tr><td>Cyprus</td><td>CYP</td></tr>
<tr><td>Czechia</td><td>CZE</td></tr>
<tr><td>Democratic People's Republic of Korea</td><td>PRK</td></tr>
<tr><td>Democratic Republic of the Congo</td><td>COD</td></tr>
<tr><td>Denmark</td><td>DNK</td></tr>
<tr><td>Djibouti</td><td>DJI</td></tr>
<tr><td>Dominica</td><td>DMA</td></tr>
<tr><td>Dominican Republic</td><td>DOM</td></tr>
<tr><td>Ecuador</td><td>ECU</td></tr>
<tr><td>Egypt</td><td>EGY</td></tr>
<tr><td>El Salvador</td><td>SLV</td></tr>
<tr><td>Equatorial Guinea</td><td>GNQ</td></tr>
<tr><td>Eritrea</td><td>ERI</td></tr>
<tr><td>Estonia</td><td>EST</td></tr>
<tr><td>Eswatini</td><td>SWZ</td></tr>
<tr><td>Ethiopia</td><td>ETH</td></tr>
<tr><td>Falkland Islands (Malvinas)</td><td>FLK</td></tr>
<tr><td>Faroe Islands</td><td>FRO</td></tr>
<tr><td>Fiji</td><td>FJI</td></tr>
<tr><td>Finland</td><td>FIN</td></tr>
<tr><td>France</td><td>FRA</td></tr>
<tr><td>French Guiana</td><td>GUF</td></tr>
<tr><td>French Polynesia</td><td>PYF</td></tr>
<tr><td>French Southern Territories</td><td>ATF</td></tr>
<tr><td>Gabon</td><td>GAB</td></tr>
<tr><td>Galápagos Islands</td><td>ECU</td></tr>
<tr><td>Gambia</td><td>GMB</td></tr>
<tr><td>Gaza</td><td>PSE</td></tr>
<tr><td>Georgia</td><td>GEO</td></tr>
<tr><td>Germany</td><td>DEU</td></tr>
<tr><td>Ghana</td><td>GHA</td></tr>
<tr><td>Gibraltar</td><td>GIB</td></tr>
<tr><td>Greece</td><td>GRC</td></tr>
<tr><td>Greenland</td><td>GRL</td></tr>
<tr><td>Grenada</td><td>GRD</td></tr>
<tr><td>Guadeloupe</td><td>GLP</td></tr>
<tr><td>Guam</td><td>GUM</td></tr>
<tr><td>Guatemala</td><td>GTM</td></tr>
<tr><td>Guernsey</td><td>GGY</td></tr>
<tr><td>Guinea</td><td>GIN</td></tr>
<tr><td>Guinea-Bissau</td><td>GNB</td></tr>
<tr><td>Guyana</td><td>GUY</td></tr>
<tr><td>Haiti</td><td>HTI</td></tr>
<tr><td>Halaib Triangle</td><td>XHT</td></tr>
<tr><td>Heard Island and McDonald Islands</td><td>HMD</td></tr>
<tr><td>Honduras</td><td>HND</td></tr>
<tr><td>Hong Kong</td><td>HKG</td></tr>
<tr><td>Hungary</td><td>HUN</td></tr>
<tr><td>Iceland</td><td>ISL</td></tr>
<tr><td>Ilemi Triangle</td><td>XIT</td></tr>
<tr><td>India</td><td>IND</td></tr>
<tr><td>Indonesia</td><td>IDN</td></tr>
<tr><td>Iran (Islamic Republic of)</td><td>IRN</td></tr>
<tr><td>Iraq</td><td>IRQ</td></tr>
<tr><td>Ireland</td><td>IRL</td></tr>
<tr><td>Isle of Man</td><td>IMN</td></tr>
<tr><td>Israel</td><td>ISR</td></tr>
<tr><td>Italy</td><td>ITA</td></tr>
<tr><td>Jamaica</td><td>JAM</td></tr>
<tr><td>Jammu and Kashmir</td><td>XJK</td></tr>
<tr><td>Japan</td><td>JPN</td></tr>
<tr><td>Jersey</td><td>JEY</td></tr>
<tr><td>Jordan</td><td>JOR</td></tr>
<tr><td>Kazakhstan</td><td>KAZ</td></tr>
<tr><td>Kenya</td><td>KEN</td></tr>
<tr><td>Kingdom of the Netherlands</td><td>NLD</td></tr>
<tr><td>Kiribati</td><td>KIR</td></tr>
<tr><td>Kuwait</td><td>KWT</td></tr>
<tr><td>Kyrgyzstan</td><td>KGZ</td></tr>
<tr><td>Lao People's Democratic Republic</td><td>LAO</td></tr>
<tr><td>Latvia</td><td>LVA</td></tr>
<tr><td>Lebanon</td><td>LBN</td></tr>
<tr><td>Lesotho</td><td>LSO</td></tr>
<tr><td>Liberia</td><td>LBR</td></tr>
<tr><td>Libya</td><td>LBY</td></tr>
<tr><td>Liechtenstein</td><td>LIE</td></tr>
<tr><td>Lithuania</td><td>LTU</td></tr>
<tr><td>Luxembourg</td><td>LUX</td></tr>
<tr><td>Macao</td><td>MAC</td></tr>
<tr><td>Madagascar</td><td>MDG</td></tr>
<tr><td>Madeira Island</td><td>PRT</td></tr>
<tr><td>Malawi</td><td>MWI</td></tr>
<tr><td>Malaysia</td><td>MYS</td></tr>
<tr><td>Maldives</td><td>MDV</td></tr>
<tr><td>Mali</td><td>MLI</td></tr>
<tr><td>Malta</td><td>MLT</td></tr>
<tr><td>Marshall Islands</td><td>MHL</td></tr>
<tr><td>Martinique</td><td>MTQ</td></tr>
<tr><td>Mauritania</td><td>MRT</td></tr>
<tr><td>Mauritius</td><td>MUS</td></tr>
<tr><td>Mayotte</td><td>MYT</td></tr>
<tr><td>Mexico</td><td>MEX</td></tr>
<tr><td>Micronesia (Federated States of)</td><td>FSM</td></tr>
<tr><td>Monaco</td><td>MCO</td></tr>
<tr><td>Mongolia</td><td>MNG</td></tr>
<tr><td>Montenegro</td><td>MNE</td></tr>
<tr><td>Montserrat</td><td>MSR</td></tr>
<tr><td>Morocco</td><td>MAR</td></tr>
<tr><td>Mozambique</td><td>MOZ</td></tr>
<tr><td>Myanmar</td><td>MMR</td></tr>
<tr><td>Namibia</td><td>NAM</td></tr>
<tr><td>Nauru</td><td>NRU</td></tr>
<tr><td>Nepal</td><td>NPL</td></tr>
<tr><td>New Caledonia</td><td>NCL</td></tr>
<tr><td>New Zealand</td><td>NZL</td></tr>
<tr><td>Nicaragua</td><td>NIC</td></tr>
<tr><td>Niger</td><td>NER</td></tr>
<tr><td>Nigeria</td><td>NGA</td></tr>
<tr><td>Niue</td><td>NIU</td></tr>
<tr><td>Norfolk Island</td><td>NFK</td></tr>
<tr><td>North Macedonia</td><td>MKD</td></tr>
<tr><td>Northern Mariana Islands</td><td>MNP</td></tr>
<tr><td>Norway</td><td>NOR</td></tr>
<tr><td>Oman</td><td>OMN</td></tr>
<tr><td>Pakistan</td><td>PAK</td></tr>
<tr><td>Palau</td><td>PLW</td></tr>
<tr><td>Panama</td><td>PAN</td></tr>
<tr><td>Papua New Guinea</td><td>PNG</td></tr>
<tr><td>Paraguay</td><td>PRY</td></tr>
<tr><td>Peru</td><td>PER</td></tr>
<tr><td>Philippines</td><td>PHL</td></tr>
<tr><td>Pitcairn</td><td>PCN</td></tr>
<tr><td>Poland</td><td>POL</td></tr>
<tr><td>Portugal</td><td>PRT</td></tr>
<tr><td>Puerto Rico</td><td>PRI</td></tr>
<tr><td>Qatar</td><td>QAT</td></tr>
<tr><td>Republic of Korea</td><td>KOR</td></tr>
<tr><td>Republic of Moldova</td><td>MDA</td></tr>
<tr><td>Réunion</td><td>REU</td></tr>
<tr><td>Romania</td><td>ROU</td></tr>
<tr><td>Russian Federation</td><td>RUS</td></tr>
<tr><td>Rwanda</td><td>RWA</td></tr>
<tr><td>Saba</td><td>BES</td></tr>
<tr><td>Saint Barthélemy</td><td>BLM</td></tr>
<tr><td>Saint Helena</td><td>SHN</td></tr>
<tr><td>Saint Kitts and Nevis</td><td>KNA</td></tr>
<tr><td>Saint Lucia</td><td>LCA</td></tr>
<tr><td>Saint Martin</td><td>MAF</td></tr>
<tr><td>Saint Pierre and Miquelon</td><td>SPM</td></tr>
<tr><td>Saint Vincent and the Grenadines</td><td>VCT</td></tr>
<tr><td>Samoa</td><td>WSM</td></tr>
<tr><td>Sao Tome and Principe</td><td>STP</td></tr>
<tr><td>Saudi Arabia</td><td>SAU</td></tr>
<tr><td>Senegal</td><td>SEN</td></tr>
<tr><td>Serbia</td><td>SRB</td></tr>
<tr><td>Seychelles</td><td>SYC</td></tr>
<tr><td>Sierra Leone</td><td>SLE</td></tr>
<tr><td>Singapore</td><td>SGP</td></tr>
<tr><td>Sint Eustatius</td><td>BES</td></tr>
<tr><td>Sint Maarten</td><td>SXM</td></tr>
<tr><td>Slovakia</td><td>SVK</td></tr>
<tr><td>Slovenia</td><td>SVN</td></tr>
<tr><td>Solomon Islands</td><td>SLB</td></tr>
<tr><td>Somalia</td><td>SOM</td></tr>
<tr><td>South Africa</td><td>ZAF</td></tr>
<tr><td>South Georgia and the South Sandwich Islands</td><td>SGS</td></tr>
<tr><td>South Sudan</td><td>SSD</td></tr>
<tr><td>Spain</td><td>ESP</td></tr>
<tr><td>Sri Lanka</td><td>LKA</td></tr>
<tr><td>Sudan</td><td>SDN</td></tr>
<tr><td>Suriname</td><td>SUR</td></tr>
<tr><td>Svalbard and Jan Mayen Islands</td><td>SJM</td></tr>
<tr><td>Sweden</td><td>SWE</td></tr>
<tr><td>Switzerland</td><td>CHE</td></tr>
<tr><td>Syrian Arab Republic</td><td>SYR</td></tr>
<tr><td>Taiwan</td><td>TWN</td></tr>
<tr><td>Tajikistan</td><td>TJK</td></tr>
<tr><td>Thailand</td><td>THA</td></tr>
<tr><td>Timor-Leste</td><td>TLS</td></tr>
<tr><td>Togo</td><td>TGO</td></tr>
<tr><td>Tokelau</td><td>TKL</td></tr>
<tr><td>Tonga</td><td>TON</td></tr>
<tr><td>Trinidad and Tobago</td><td>TTO</td></tr>
<tr><td>Tunisia</td><td>TUN</td></tr>
<tr><td>Türkiye</td><td>TUR</td></tr>
<tr><td>Turkmenistan</td><td>TKM</td></tr>
<tr><td>Turks and Caicos Islands</td><td>TCA</td></tr>
<tr><td>Tuvalu</td><td>TUV</td></tr>
<tr><td>Uganda</td><td>UGA</td></tr>
<tr><td>Ukraine</td><td>UKR</td></tr>
<tr><td>United Arab Emirates</td><td>ARE</td></tr>
<tr><td>United Kingdom of Great Britain and Northern Ireland</td><td>GBR</td></tr>
<tr><td>United Republic of Tanzania</td><td>TZA</td></tr>
<tr><td>United States of America</td><td>USA</td></tr>
<tr><td>United States Virgin Islands</td><td>VIR</td></tr>
<tr><td>Uruguay</td><td>URY</td></tr>
<tr><td>Uzbekistan</td><td>UZB</td></tr>
<tr><td>Vanuatu</td><td>VUT</td></tr>
<tr><td>Venezuela (Bolivarian Republic of)</td><td>VEN</td></tr>
<tr><td>Viet Nam</td><td>VNM</td></tr>
<tr><td>West Bank</td><td>PSE</td></tr>
<tr><td>Western Sahara</td><td>ESH</td></tr>
<tr><td>Yemen</td><td>YEM</td></tr>
<tr><td>Zambia</td><td>ZMB</td></tr>
<tr><td>Zimbabwe</td><td>ZWE</td></tr>
</tbody>
</table>


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

<table style="text-align: left;">
<thead>
<tr>
<th style="text-align: left;">State</th>
<th style="text-align: left;">Code</th>
</tr>
</thead>
<tbody>
<tr><td>Alabama</td><td>AL</td></tr>
<tr><td>Alaska</td><td>AK</td></tr>
<tr><td>Arizona</td><td>AZ</td></tr>
<tr><td>Arkansas</td><td>AR</td></tr>
<tr><td>California</td><td>CA</td></tr>
<tr><td>Colorado</td><td>CO</td></tr>
<tr><td>Connecticut</td><td>CT</td></tr>
<tr><td>Delaware</td><td>DE</td></tr>
<tr><td>District of Columbia</td><td>DC</td></tr>
<tr><td>Florida</td><td>FL</td></tr>
<tr><td>Georgia</td><td>GA</td></tr>
<tr><td>Hawaii</td><td>HI</td></tr>
<tr><td>Idaho</td><td>ID</td></tr>
<tr><td>Illinois</td><td>IL</td></tr>
<tr><td>Indiana</td><td>IN</td></tr>
<tr><td>Iowa</td><td>IA</td></tr>
<tr><td>Kansas</td><td>KS</td></tr>
<tr><td>Kentucky</td><td>KY</td></tr>
<tr><td>Louisiana</td><td>LA</td></tr>
<tr><td>Maine</td><td>ME</td></tr>
<tr><td>Maryland</td><td>MD</td></tr>
<tr><td>Massachusetts</td><td>MA</td></tr>
<tr><td>Michigan</td><td>MI</td></tr>
<tr><td>Minnesota</td><td>MN</td></tr>
<tr><td>Mississippi</td><td>MS</td></tr>
<tr><td>Missouri</td><td>MO</td></tr>
<tr><td>Montana</td><td>MT</td></tr>
<tr><td>Nebraska</td><td>NE</td></tr>
<tr><td>Nevada</td><td>NV</td></tr>
<tr><td>New Hampshire</td><td>NH</td></tr>
<tr><td>New Jersey</td><td>NJ</td></tr>
<tr><td>New Mexico</td><td>NM</td></tr>
<tr><td>New York</td><td>NY</td></tr>
<tr><td>North Carolina</td><td>NC</td></tr>
<tr><td>North Dakota</td><td>ND</td></tr>
<tr><td>Ohio</td><td>OH</td></tr>
<tr><td>Oklahoma</td><td>OK</td></tr>
<tr><td>Oregon</td><td>OR</td></tr>
<tr><td>Pennsylvania</td><td>PA</td></tr>
<tr><td>Rhode Island</td><td>RI</td></tr>
<tr><td>South Carolina</td><td>SC</td></tr>
<tr><td>South Dakota</td><td>SD</td></tr>
<tr><td>Tennessee</td><td>TN</td></tr>
<tr><td>Texas</td><td>TX</td></tr>
<tr><td>Utah</td><td>UT</td></tr>
<tr><td>Vermont</td><td>VT</td></tr>
<tr><td>Virginia</td><td>VA</td></tr>
<tr><td>Washington</td><td>WA</td></tr>
<tr><td>West Virginia</td><td>WV</td></tr>
<tr><td>Wisconsin</td><td>WI</td></tr>
<tr><td>Wyoming</td><td>WY</td></tr>
</tbody>
</table>


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
