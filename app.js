const coins = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"];

async function updatePrices() {
    for (const coin of coins) {
        try {
            const response = await fetch(
                `https://fapi.binance.com/fapi/v1/ticker/price?symbol=${coin}`
            );

            const data = await response.json();

            const element = document.getElementById(coin);

            if (element) {
                element.innerText = "$" + Number(data.price).toLocaleString();
            }

        } catch (error) {
            console.log("Error:", coin, error);
        }
    }
}

updatePrices();

setInterval(updatePrices, 10000);
