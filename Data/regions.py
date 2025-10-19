# --- African States ---
african_states = [
    "Algeria", "Eswatini", "Namibia", "Angola", "Ethiopia", "Niger",
    "Benin", "Gabon", "Nigeria", "Botswana", "Gambia", "Rwanda",
    "Burkina Faso", "Ghana", "Sao Tome and Principe", "Burundi", "Guinea", "Senegal",
    "Cabo Verde", "Guinea-Bissau", "Seychelles", "Cameroon", "Kenya", "Sierra Leone",
    "Central African Republic", "Lesotho", "Somalia", "Chad", "Liberia", "South Africa",
    "Comoros", "Libya", "South Sudan", "Congo", "Madagascar", "Sudan",
    "Côte d'Ivoire", "Malawi", "Togo", "Democratic Republic of the Congo", "Mali", "Tunisia",
    "Djibouti", "Mauritania", "Uganda", "Egypt", "Mauritius", "United Republic of Tanzania",
    "Equatorial Guinea", "Morocco", "Zambia", "Eritrea", "Mozambique", "Zimbabwe", "Réunion", 
    "Mayotte", "Saint Helena", "Western Sahara"
]

# --- Asia-Pacific States ---
asia_pacific = [
    "Afghanistan", "Kyrgyzstan", "Samoa", "Bahrain", "Lao People's Democratic Republic", "Saudi Arabia",
    "Bangladesh", "Lebanon", "Singapore", "Bhutan", "Malaysia", "Solomon Islands",
    "Brunei Darussalam", "Maldives", "Sri Lanka", "Cambodia", "Marshall Islands", "Syrian Arab Republic",
    "China", "Micronesia (Federated States of)", "Tajikistan", "Cyprus", "Mongolia", "Thailand",
    "Democratic People's Republic of Korea", "Myanmar", "Timor-Leste", "Fiji", "Nauru", "Tonga",
    "India", "Nepal", "Türkiye", "Indonesia", "Oman", "Turkmenistan", "Iran (Islamic Republic of)",
    "Pakistan", "Tuvalu", "Iraq", "Palau", "United Arab Emirates", "Japan", "Papua New Guinea",
    "Uzbekistan", "Jordan", "Philippines", "Vanuatu", "Kazakhstan", "Qatar", "Viet Nam",
    "Kiribati", "Republic of Korea", "Yemen", "Kuwait", "American Samoa", "Guam", "Northern Mariana Islands", 
    "Cook Islands", "Tokelau", "Niue", "Wallis and Futuna Islands", "New Caledonia", "French Polynesia", 
    "Micronesia (Fed. States of)", "Micronesia", "Palau", "Nauru", "Kiribati", "Tuvalu", "Vanuatu", "China, Hong Kong SAR", "China, Macao SAR",
    "China, Taiwan Province of China", "Dem. People's Republic of Korea",
     "State of Palestine"
]

# --- Eastern European States ---
eastern_europe = [
    "Albania", "Estonia", "Republic of Moldova", "Armenia", "Georgia", "Romania",
    "Azerbaijan", "Hungary", "Russian Federation", "Belarus", "Latvia", "Serbia",
    "Bosnia and Herzegovina", "Lithuania", "Slovakia", "Bulgaria", "Montenegro", "Slovenia",
    "Croatia", "North Macedonia", "Ukraine", "Czechia", "Poland"
]

# --- Latin American and Caribbean States ---
latin_america_caribbean = [
    "Antigua and Barbuda", "Dominica", "Nicaragua", "Argentina", "Dominican Republic", "Panama",
    "Bahamas (The)", "Ecuador", "Paraguay", "Barbados", "El Salvador", "Peru",
    "Belize", "Grenada", "Saint Kitts and Nevis", "Bolivia",
    "Guatemala", "Saint Lucia", "Brazil", "Guyana", "Saint Vincent and the Grenadines",
    "Chile", "Haiti", "Suriname", "Colombia", "Honduras", "Trinidad and Tobago",
    "Costa Rica", "Jamaica", "Uruguay", "Cuba", "Mexico", "Venezuela (Bolivarian Republic of)", 
    "Aruba", "Bonaire, Sint Eustatius and Saba", "Curaçao", "Sint Maarten (Dutch part)", "Anguilla", 
    "Montserrat", "British Virgin Islands", "Turks and Caicos Islands", "Cayman Islands",
      "Puerto Rico", "United States Virgin Islands", "Guadeloupe", "Martinique", "French Guiana", "Bahamas", "Venezuela"
]

# --- Western European and Other States ---
western_europe = [
    "Andorra", "Iceland", "Norway", "Australia", "Ireland", "Portugal", "Austria", "Israel",
    "San Marino", "Belgium", "Italy", "Spain", "Liechtenstein", "Sweden", "Denmark",
    "Luxembourg", "Switzerland", "Finland", "Malta", "Türkiye", "France", "Monaco",
    "United Kingdom of Great Britain and Northern Ireland", "Germany", "Netherlands", "Greece", "New Zealand", 
    "Vatican City State", "United Kingdom" ,"Holy See", "Isle of Man", "Channel Islands", "Saint Pierre and Miquelon", 
    "Gibraltar", "Falkland Islands (Malvinas)", "Faroe Islands"
]

# --- North America ---

north_america = [
    "Canada", "United States of America","Greenland", "Bermuda", "Saint Pierre and Miquelon","Antartica"]


# --- Aggregates ---
aggregates = [
    # --- broad global aggregates ---
    "World",
    "AFRICA", "Africa",
    "ASIA", "Asia",
    "EUROPE", "Europe",
    "OCEANIA", "Oceania",
    "NORTHERN AMERICA", "Northern America",
    "LATIN AMERICA AND THE CARIBBEAN", "Latin America and the Caribbean",
    "Europe and Northern America",
    
    # --- UN regional groupings ---
    "Sub-Saharan Africa", "Northern Africa", "Eastern Africa", "Middle Africa",
    "Southern Africa", "Western Africa",
    "Central Asia", "Eastern Asia", "South-Eastern Asia", "Southern Asia", "Western Asia",
    "Northern Africa and Western Asia",
    "Central and Southern Asia",
    "Eastern and South-Eastern Asia",
    "Australia/New Zealand",
    "Oceania (excluding Australia and New Zealand)",
    "Caribbean", "Central America", "South America",
    "Western Europe", "Southern Europe", "Northern Europe", "Eastern Europe",

    # --- Income / development groups ---
    "Developed regions", "Developing regions",
    "Least developed countries", "Less developed regions", "More developed regions",
    "Less developed regions, excluding China",
    "Less developed regions, excluding least developed countries",
    "Low-income countries", "Lower-middle-income countries",
    "Middle-income countries", "Upper-middle-income countries",
    "Low-and-Lower-middle-income countries", "Low-and-middle-income countries",
    "High-income countries", "High-and-upper-middle-income countries",
    "No income group available",
    "Land-locked Developing Countries (LLDC)",
    "Small Island Developing States (SIDS)",

    # --- Meta/placeholder categories ---
    "Others", "Other", "No data",
    "Melanesia", "Polynesia"
]

# --- Subregiones LAC (ONU M49) — Estados soberanos ---
central_america = [
    "Belize", "Costa Rica", "El Salvador", "Guatemala",
    "Honduras", "Nicaragua", "Panama", "Mexico", "Brazil"
]

caribbean = ['Anguilla','Antigua and Barbuda','Aruba','Bahamas','Barbados','Bonaire, Sint Eustatius and Saba',
             'British Virgin Islands','Cayman Islands','Cuba','Curaçao','Dominica','Dominican Republic','Grenada',
             'Guadeloupe','Haiti','Jamaica','Martinique','Montserrat','Puerto Rico','Saint Barthélemy',
             'Saint Kitts and Nevis','Saint Lucia','Saint Martin (French Part)','Saint Vincent and the Grenadines',
             'Sint Maarten (Dutch part)','Trinidad and Tobago','Turks and Caicos Islands','United States Virgin Islands',
]

south_america = [
    "Argentina", "Bolivia", "Bouvet Island" "Brazil", "Chile",
    "Colombia", "Ecuador","Falkland Islands (Malvinas)", "French Guiana","Guyana", "Paraguay", "Peru",
    "Suriname", "South Georgia and the South Sandwich Islands","Uruguay", "Venezuela"
]

