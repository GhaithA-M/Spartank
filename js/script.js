// script.js

// Assume you have a JSON file `fuel-prices.json` with the structure:
// [
//   {
//     "station": "Uno X",
//     "logo": "path-to-unox-logo.png",
//     "prices": [
//       { "type": "92 Blyfri", "price": "9.92", "lastUpdated": "2023-12-21" },
//       { "type": "95 Blyfri", "price": "9.94", "lastUpdated": "2023-12-21" },
//       ...
//     ]
//   },
//   ...
// ]

document.addEventListener('DOMContentLoaded', function() {
    fetch('fuel-prices.json')
        .then(response => response.json())
        .then(stations => {
            stations.forEach(station => {
                const stationDiv = document.createElement('div');
                stationDiv.className = 'fuel-station';

                const headerDiv = document.createElement('div');
                headerDiv.className = 'station-header';

                const logoImg = document.createElement('img');
                logoImg.src = station.logo;
                logoImg.alt = `${station.station} Logo`;
                logoImg.className = 'station-logo';

                const nameH1 = document.createElement('h1');
                nameH1.textContent = station.station;
                nameH1.className = 'station-name';

                headerDiv.appendChild(logoImg);
                headerDiv.appendChild(nameH1);
                stationDiv.appendChild(headerDiv);

                const pricesDiv = document.createElement('div');
                pricesDiv.className = 'station-prices';

                station.prices.forEach(price => {
                    const priceEntryDiv = document.createElement('div');
                    priceEntryDiv.className = 'price-entry';

                    const labelSpan = document.createElement('span');
                    labelSpan.textContent = price.type;
                    labelSpan.className = 'price-label';

                    const valueSpan = document.createElement('span');
                    valueSpan.textContent = `${price.price}`;
                    valueSpan.className = 'price-value';

                    priceEntryDiv.appendChild(labelSpan);
                    priceEntryDiv.appendChild(valueSpan);
                    pricesDiv.appendChild(priceEntryDiv);
                });

                stationDiv.appendChild(pricesDiv);
                document.querySelector('.fuel-stations').appendChild(stationDiv);
            });
        });
});
