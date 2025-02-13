const ctx1 = document.getElementById('lineChart').getContext('2d');
new Chart(ctx1, {
    type: 'line',
    data: {
        labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        datasets: [{ 
            data: [20, 60, 40, 80],
            borderColor: 'orange',
            fill: false
        }]
    }
});

const ctx2 = document.getElementById('pieChart').getContext('2d');
new Chart(ctx2, {
    type: 'pie',
    data: {
        labels: ['Male', 'Female', 'Out Of'],
        datasets: [{
            data: [60, 30, 10],
            backgroundColor: ['orange', 'purple', 'blue']
        }]
    }
});