// List of stations and their corresponding JSON files
const stations = [
    { id: "circlek", file: "circlek_prices.json" },
    { id: "f24", file: "f24_prices.json" },
    { id: "ingo", file: "ingo_prices.json" },
    { id: "ok", file: "ok_prices.json" },
    { id: "q8", file: "q8_prices.json" }
];

// Assuming 'stations' is an array of station data
stations.forEach(station => {
    // Select the station prices div
    let stationPrices = document.getElementById(`station-${station.id}-prices`);

    // Fetch and display prices for the station
    fetch(`stations/${station.file}`)
        .then(response => response.json())
        .then(prices => {
            prices.forEach(price => {
                // Create and append the price entry
                const priceEntry = document.createElement('div');
                priceEntry.classList.add('price-entry');
                priceEntry.innerHTML = `
                    <span class="price-label">${price['Fuel Type']}</span>
                    <span class="price-value">${price['Price']}</span>
                `;
                // Append the price entry to the correct station prices div
                stationPrices.appendChild(priceEntry);
            });
        });
});

function toggleStationPrices(stationId) {
    const pricesDiv = document.getElementById(`station-${stationId}-prices`);
    pricesDiv.classList.toggle('show');
}
