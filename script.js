async function fetchCandleData() {
    const response = await fetch("https://api.upbit.com/v1/candles/days?market=KRW-BTC&count=37");
    return await response.json();
}

function lppl(t, A, B, C, tc, m, omega, phi) {
    return A + B * Math.pow(tc - t, m) + C * Math.pow(tc - t, m) * Math.cos(omega * Math.log(tc - t) - phi);
}

function calculateLpplPoints(data, params) {
    const lpplPoints = [];
    for (let i = 0; i < 30; i++) {
        const t = i;
        const y = lppl(t, ...params);
        lpplPoints.push({
            x: new Date(data[i].candle_date_time_kst),
            y: y
        });
    }
    return lpplPoints;
}

function drawChart(data, params) {
    const actual = data.slice(0, 30).map(d => ({
        x: new Date(d.candle_date_time_kst),
        y: d.trade_price
    }));

    const predicted = calculateLpplPoints(data, params);

    const chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        title: { text: "비트코인 30일 종가 + LPPL 예측선" },
        axisY: { prefix: "₩" },
        data: [
            {
                type: "line",
                name: "실제 종가",
                dataPoints: actual,
                showInLegend: true
            },
            {
                type: "line",
                name: "LPPL 예측선",
                lineDashType: "dash",
                dataPoints: predicted,
                showInLegend: true
            }
        ]
    });
    chart.render();
}

async function init() {
    const candleData = await fetchCandleData();
    const params = [41230000.0, -5320000.0, 1310000.0, 35, 0.36, 8.3, 1.5]; // Python 출력 예시
    drawChart(candleData, params);
}

init();
