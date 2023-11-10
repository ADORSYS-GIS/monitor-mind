function createResourceChart(canvasId, chartLabel, chartData, chartType = 'bar') {
    document.querySelector(`#${canvasId}`).innerHTML = `<canvas id="${canvasId}-chart"></canvas>`;
    const ctx = document.getElementById(`${canvasId}-chart`).getContext('2d');
    return new Chart(ctx, {
        type: chartType,
        data: {
            labels: chartData.labels,
            datasets: [{
                label: chartLabel,
                data: chartData.values,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function updateCPUHistoryCharts() {
    // Function to fetch and update charts with historical data
    fetch('/api/cpu')
        .then(response => response.json())
        .then(data => {
            // Update the CPU history chart with 'data.cpu_usage_history'
            const timestamps = data.timestamps;
            const cpu_usage = data.cpu_usage;
            createResourceChart('cpu-data', 'CPU Usage', { labels: timestamps, values: cpu_usage });
        });
    // Repeat for other resources
}

// function updateMemoryHistoryCharts() {
//     // Function to fetch and update charts with historical data
//     fetch('/api/memory')
//         .then(response => response.json())
//         .then(data => {
//             // Update the CPU history chart with 'data.cpu_usage_history'
//             const ram_timestamps = data.ram_timestamps;
//             const ram_usage = data.ram_cpu_usage;
//             createResourceChart('memory-data', 'RAM Usage', { labels: ram_timestamps, values: ram_usage });

//             const swap_timestamps = data.swap_timestamps;
//             const swap_usage = data.swap_cpu_usage;
//             createResourceChart('swap-data', 'Swap Usage', { labels: swap_timestamps, values: swap_usage });
//         });
//     // Repeat for other resources
// }

function updateMemoryHistoryCharts() {
    // Function to fetch and update charts with historical data
    fetch('/api/memory')
        .then(response => response.json())
        .then(data => {
            // Update the RAM history chart with 'data.ram_usage_history'
            const ram_timestamps = data.timestamps;
            const ram_usage = data.ram_usage;
            createResourceChart('memory-data', 'RAM Usage', { labels: ram_timestamps, values: ram_usage });

            // Update the Swap history chart with 'data.swap_usage_history'
            const swap_timestamps = data.timestamps;
            const swap_usage = data.swap_usage;
            createResourceChart('swap-data', 'Swap Usage', { labels: swap_timestamps, values: swap_usage });
        });
    // Repeat for other resources
}

function updateNetworkHistoryCharts() {
    // Function to fetch and update charts with historical data
    fetch('/api/network')
        .then(response => response.json())
        .then(data => {
            // Update the Network history chart with 'data.cpu_usage_history'
            const network_timestamps = data.network_timestamps;
            const network_usage = data.network_cpu_usage;
            createResourceChart('network-data', 'Network Usage', { labels: network_timestamps, values: network_usage });
        });
    // Repeat for other resources
}

// Path: static/js/polling.js
function afterLoad() {
    updateCPUHistoryCharts();
    updateMemoryHistoryCharts();
    updateNetworkHistoryCharts();
}

window.onload = () => {
    afterLoad();

    // Call this function at regular intervals
    setInterval(afterLoad, 15_000); // Example: Update every 15 seconds
}




