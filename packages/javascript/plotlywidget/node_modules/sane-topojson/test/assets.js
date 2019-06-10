var ITEM_WITH_NO_SUBUNITS = [
  'africa_110m', 'africa_50m',
  'asia_110m', 'asia_50m',
  'europe_110m', 'europe_50m',
  'south-america_110m'
]

var GEOMETRY_COUNT = {
  'world_110m': {
    'coastlines': 134,
    'land': 127,
    'ocean': 2,
    'lakes': 25,
    'rivers': 13,
    'countries': 177,
    'subunits': 51
  },
  'world_50m': {
    'coastlines': 1428,
    'land': 1420,
    'ocean': 1,
    'lakes': 275,
    'rivers': 461,
    'countries': 241,
    'subunits': 100
  },
  'africa_110m': {
    'coastlines': 11,
    'land': 2,
    'ocean': 2,
    'lakes': 4,
    'rivers': 3,
    'countries': 51,
    'subunits': 0
  },
  'africa_50m': {
    'coastlines': 147,
    'land': 36,
    'ocean': 1,
    'lakes': 20,
    'rivers': 127,
    'countries': 54,
    'subunits': 0
  },
  'asia_110m': {
    'coastlines': 65,
    'land': 28,
    'ocean': 2,
    'lakes': 2,
    'rivers': 9,
    'countries': 47,
    'subunits': 0
  },
  'asia_50m': {
    'coastlines': 729,
    'land': 331,
    'ocean': 1,
    'lakes': 58,
    'rivers': 255,
    'countries': 53,
    'subunits': 0
  },
  'europe_110m': {
    'coastlines': 19,
    'land': 14,
    'ocean': 2,
    'lakes': 3,
    'rivers': 3,
    'countries': 39,
    'subunits': 0
  },
  'europe_50m': {
    'coastlines': 263,
    'land': 210,
    'ocean': 1,
    'lakes': 45,
    'rivers': 138,
    'countries': 50,
    'subunits': 0
  },
  'north-america_110m': {
    'coastlines': 53,
    'land': 47,
    'ocean': 1,
    'lakes': 14,
    'rivers': 3,
    'countries': 18,
    'subunits': 51
  },
  'north-america_50m': {
    'coastlines': 375,
    'land': 346,
    'ocean': 1,
    'lakes': 123,
    'rivers': 129,
    'countries': 38,
    'subunits': 64
  },
  'south-america_110m': {
    'coastlines': 14,
    'land': 3,
    'ocean': 1,
    'lakes': 1,
    'rivers': 2,
    'countries': 13,
    'subunits': 0
  },
  'south-america_50m': {
    'coastlines': 174,
    'land': 67,
    'ocean': 1,
    'lakes': 8,
    'rivers': 53,
    'countries': 13,
    'subunits': 27
  },
  'usa_110m': {
    'coastlines': 53,
    'land': 9,
    'ocean': 1,
    'lakes': 7,
    'rivers': 1,
    'countries': 1,
    'subunits': 51
  },
  'usa_50m': {
    'coastlines': 372,
    'land': 120,
    'ocean': 1,
    'lakes': 55,
    'rivers': 66,
    'countries': 1,
    'subunits': 58
  }
}

var COUNTRY_LIST = {
  'world_110m': ['AFG', 'AGO', 'ALB', 'ARE', 'ARG', 'ARM', 'ATA', 'ATF', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BOL', 'BRA', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COL', 'CRI', 'CUB', 'CYP', 'CZE', 'DEU', 'DJI', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESH', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FLK', 'FRA', 'GAB', 'GBR', 'GEO', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRL', 'GTM', 'GUY', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LKA', 'LSO', 'LTU', 'LUX', 'LVA', 'MAR', 'MDA', 'MDG', 'MEX', 'MKD', 'MLI', 'MMR', 'MNE', 'MNG', 'MOZ', 'MRT', 'MWI', 'MYS', 'NAM', 'NCL', 'NER', 'NGA', 'NIC', 'NLD', 'NOR', 'NPL', 'NZL', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PNG', 'POL', 'PRI', 'PRK', 'PRT', 'PRY', 'PSE', 'QAT', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SLB', 'SLE', 'SLV', 'SOM', 'SRB', 'SSD', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SYR', 'TCD', 'TGO', 'THA', 'TJK', 'TKM', 'TLS', 'TTO', 'TUN', 'TUR', 'TWN', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VEN', 'VNM', 'VUT', 'YEM', 'ZAF', 'ZMB', 'ZWE'],
  'world_50m': ['ABW', 'AFG', 'AGO', 'AIA', 'ALA', 'ALB', 'AND', 'ARE', 'ARG', 'ARM', 'ASM', 'ATA', 'ATF', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLM', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESH', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FLK', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GGY', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM', 'GUM', 'GUY', 'HKG', 'HMD', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IMN', 'IND', 'IOT', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JEY', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LIE', 'LKA', 'LSO', 'LTU', 'LUX', 'LVA', 'MAC', 'MAF', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR', 'MUS', 'MWI', 'MYS', 'NAM', 'NCL', 'NER', 'NFK', 'NGA', 'NIC', 'NIU', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRI', 'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SGS', 'SHN', 'SLB', 'SLE', 'SLV', 'SMR', 'SOM', 'SPM', 'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SXM', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TWN', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VAT', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WLF', 'WSM', 'YEM', 'ZAF', 'ZMB', 'ZWE'],
  'africa_110m': ['AGO', 'BDI', 'BEN', 'BFA', 'BWA', 'CAF', 'CIV', 'CMR', 'COD', 'COG', 'DJI', 'DZA', 'EGY', 'ERI', 'ESH', 'ETH', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'KEN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG', 'MLI', 'MOZ', 'MRT', 'MWI', 'NAM', 'NER', 'NGA', 'RWA', 'SDN', 'SEN', 'SLE', 'SOM', 'SSD', 'SWZ', 'TCD', 'TGO', 'TUN', 'TZA', 'UGA', 'ZAF', 'ZMB', 'ZWE'],
  'africa_50m': ['AGO', 'BDI', 'BEN', 'BFA', 'BWA', 'CAF', 'CIV', 'CMR', 'COD', 'COG', 'COM', 'CPV', 'DJI', 'DZA', 'EGY', 'ERI', 'ESH', 'ETH', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'KEN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG', 'MLI', 'MOZ', 'MRT', 'MWI', 'NAM', 'NER', 'NGA', 'RWA', 'SDN', 'SEN', 'SLE', 'SOM', 'SSD', 'STP', 'SWZ', 'TCD', 'TGO', 'TUN', 'TZA', 'UGA', 'ZAF', 'ZMB', 'ZWE'],
  'asia_110m': ['AFG', 'ARE', 'ARM', 'AZE', 'BGD', 'BRN', 'BTN', 'CHN', 'CYP', 'GEO', 'IDN', 'IND', 'IRN', 'IRQ', 'ISR', 'JOR', 'JPN', 'KAZ', 'KGZ', 'KHM', 'KOR', 'KWT', 'LAO', 'LBN', 'LKA', 'MMR', 'MNG', 'MYS', 'NPL', 'OMN', 'PAK', 'PHL', 'PRK', 'PSE', 'QAT', 'SAU', 'SYR', 'THA', 'TJK', 'TKM', 'TLS', 'TUR', 'TWN', 'UZB', 'VNM', 'YEM'],
  'asia_50m': ['AFG', 'ARE', 'ARM', 'AZE', 'BGD', 'BHR', 'BRN', 'BTN', 'CHN', 'CYP', 'GEO', 'HKG', 'IDN', 'IND', 'IRN', 'IRQ', 'ISR', 'JOR', 'JPN', 'KAZ', 'KGZ', 'KHM', 'KOR', 'KWT', 'LAO', 'LBN', 'LKA', 'MAC', 'MMR', 'MNG', 'MYS', 'NPL', 'OMN', 'PAK', 'PHL', 'PRK', 'PSE', 'QAT', 'SAU', 'SGP', 'SYR', 'THA', 'TJK', 'TKM', 'TLS', 'TUR', 'TWN', 'UZB', 'VNM', 'YEM'],
  'europe_110m': ['ALB', 'AUT', 'BEL', 'BGR', 'BIH', 'BLR', 'CHE', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HRV', 'HUN', 'IRL', 'ISL', 'ITA', 'LTU', 'LUX', 'LVA', 'MDA', 'MKD', 'MNE', 'NLD', 'NOR', 'POL', 'PRT', 'ROU', 'RUS', 'SRB', 'SVK', 'SVN', 'SWE', 'UKR'],
  'europe_50m': ['ALA', 'ALB', 'AND', 'AUT', 'BEL', 'BGR', 'BIH', 'BLR', 'CHE', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'FRO', 'GBR', 'GGY', 'GRC', 'HRV', 'HUN', 'IMN', 'IRL', 'ISL', 'ITA', 'JEY', 'LIE', 'LTU', 'LUX', 'LVA', 'MCO', 'MDA', 'MKD', 'MLT', 'MNE', 'NLD', 'NOR', 'POL', 'PRT', 'ROU', 'RUS', 'SMR', 'SRB', 'SVK', 'SVN', 'SWE', 'UKR', 'VAT'],
  // N.B. north-america scopes do not trim out Caribbean countries
  'north-america_110m': ['BHS', 'BLZ', 'CAN', 'CRI', 'CUB', 'DOM', 'GRL', 'GTM', 'HND', 'HTI', 'JAM', 'MEX', 'NIC', 'PAN', 'PRI', 'SLV', 'TTO', 'USA'],
  'north-america_50m': ['ABW', 'AIA', 'ATG', 'BHS', 'BLM', 'BLZ', 'BMU', 'BRB', 'CAN', 'CRI', 'CUB', 'CUW', 'CYM', 'DMA', 'DOM', 'GRD', 'GRL', 'GTM', 'HND', 'HTI', 'JAM', 'KNA', 'LCA', 'MAF', 'MEX', 'MSR', 'NIC', 'PAN', 'PRI', 'SLV', 'SPM', 'SXM', 'TCA', 'TTO', 'USA', 'VCT', 'VGB', 'VIR'],
  'south-america_110m': ['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'ECU', 'FLK', 'GUY', 'PER', 'PRY', 'SUR', 'URY', 'VEN'],
  'south-america_50m': ['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'ECU', 'FLK', 'GUY', 'PER', 'PRY', 'SUR', 'URY', 'VEN'],
  'usa_110m': ['USA'],
  'usa_50m': ['USA']
}

var COUNTRIES_CNT = {}
for (let k in COUNTRY_LIST) {
  COUNTRIES_CNT[k] = COUNTRY_LIST[k].length
}

var SUBUNITS_LIST = {
  'world_110m': ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
  // states/provinces from US, Canada, Australia, Brazil
  'world_50m': ['AB', 'AK', 'AL', 'AL', 'AM', 'AP', 'AR', 'AZ', 'BA', 'BC', 'CA', 'CE', 'CO', 'CT', 'CT', 'DC', 'DE', 'DF', 'ES', 'FL', 'GA', 'GO', 'HI', 'IA', 'ID', 'IL', 'IN', 'JB', 'KS', 'KY', 'LA', 'MA', 'MA', 'MB', 'MD', 'ME', 'MG', 'MI', 'MN', 'MO', 'MS', 'MS', 'MT', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NS', 'NT', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PA', 'PB', 'PE', 'PE', 'PI', 'PR', 'QC', 'QL', 'RO', 'AC', 'RI', 'RJ', 'RN', 'RR', 'RS', 'SA', 'SC', 'SC', 'SD', 'SE', 'SK', 'SP', 'TN', 'TO', 'TS', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WA', 'WI', 'WV', 'WY', 'YT'].sort(),
  'africa_110m': [],
  'africa_50m': [],
  'asia_110m': [],
  'asia_50m': [],
  'europe_110m': [],
  'europe_50m': [],
  'north-america_110m': ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
  'north-america_50m': ['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT'],
  'south-america_110m': [],
  'south-america_50m': ['AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RO', 'AC', 'RJ', 'RN', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'].sort(),
  'usa_110m': ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
  // ['BC', 'MB', 'NB', 'ON', 'QC', 'SK', 'YT'] show up here for some reason
  'usa_50m': ['AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']
}

var SUBUNITS_CNT = {}
for (let k in SUBUNITS_LIST) {
  SUBUNITS_CNT[k] = SUBUNITS_LIST[k].length
}

module.exports = {
  ITEM_WITH_NO_SUBUNITS: ITEM_WITH_NO_SUBUNITS,
  GEOMETRY_COUNT: GEOMETRY_COUNT,
  COUNTRIES_CNT: COUNTRIES_CNT,
  SUBUNITS_CNT: SUBUNITS_CNT,
  COUNTRY_LIST: COUNTRY_LIST,
  SUBUNITS_LIST: SUBUNITS_LIST
}
