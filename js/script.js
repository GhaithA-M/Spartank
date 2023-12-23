// List of stations and their corresponding JSON files
const stations = [
    { id: "circlek", file: "circlek_prices.json" },
    { id: "f24", file: "f24_prices.json" },
    { id: "ingo", file: "ingo_prices.json" },
    { id: "ok", file: "ok_prices.json" },
    { id: "q8", file: "q8_prices.json" }
];

// Function to load and display prices for each station
stations.forEach(station => {
    fetch(`stations/${station.file}`)
        .then(response => response.json())
        .then(prices => {
            const pricesDiv = document.querySelector(`#station-${station.id}-prices`);
            pricesDiv.innerHTML = ''; // Clear existing content
            prices.forEach(price => {
                // Create and append the price entry
                const priceEntry = document.createElement('div');
                priceEntry.classList.add('price-entry');
                priceEntry.innerHTML = `
                    <span class="price-label">${price['Fuel Type']}</span>
                    <span class="price-value">${price['Price']}</span>
                `;
                pricesDiv.appendChild(priceEntry);
            });
        })
        .catch(error => {
            console.error('Error loading station prices:', error);
        });
});

function toggleStationPrices(stationId) {
    const pricesDiv = document.getElementById(`station-${stationId}-prices`);
    pricesDiv.classList.toggle('show');
}
