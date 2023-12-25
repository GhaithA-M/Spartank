document.addEventListener('DOMContentLoaded', (event) => {
    fetch('stations/circlek_prices.json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("Fetched data:", data);  // Log the fetched data

        // Find the object for "miles Diesel"
        const date = data.find(item => item["Fuel Type"] === "miles95");

        // Get the "Last Updated" date for "miles Diesel"
        const lastUpdatedDate = date["Last Updated"];

        const dateEntry = document.createElement('h4');
        dateEntry.textContent = `Pris sidst opdateret: ${lastUpdatedDate}`;
        document.querySelector('.last-update-date').appendChild(dateEntry);
    })
    .catch(error => console.error('Error:', error));
});
