document.addEventListener('DOMContentLoaded', (event) => {
    fetch('stations/circlek_prices.json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("Fetched data:", data);
        const date = data.find(item => item["Fuel Type"] === "miles95");
        let lastUpdatedDate = date["Last Updated"];
        let dateObj = new Date(lastUpdatedDate);
        lastUpdatedDate = `${dateObj.getDate().toString().padStart(2, '0')}/${(dateObj.getMonth() + 1).toString().padStart(2, '0')}/${dateObj.getFullYear()}`;
        const dateEntry = document.createElement('h4');
        dateEntry.textContent = `Priser sidst opdateret: ${lastUpdatedDate}`;
        document.querySelector('.last-update-date').appendChild(dateEntry);
    })
    .catch(error => console.error('Error:', error));
});
