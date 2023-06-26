
var totalFollowers = {{ total_followers }};
var totalFollowing = {{ total_following }};
var totalLikes = {{ total_likes }};
var totalViews = {{ total_views }};

// Bar Chart
var barData = {
    labels: ['Followers', 'Following', 'Likes', 'Views'],
    datasets: [{
        label: 'Analytics',
        backgroundColor: 'rgba(75, 192, 192, 0.8)',
        borderColor: '#212121',
        borderWidth: 1,
        data: [totalFollowers, totalFollowing, totalLikes, totalViews]
    }]
};

var barOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        y: {
            beginAtZero: true
        }
    }
};

var barChart = new Chart(document.getElementById('barChart'), {
    type: 'bar',
    data: barData,
    options: barOptions
});

// Pie Chart
var pieData = {
    labels: ['Followers', 'Following', 'Likes', 'Views'],
    datasets: [{
        data: [totalFollowers, totalFollowing, totalLikes, totalViews],
        backgroundColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)'
        ],
        hoverBackgroundColor: [
            'rgba(255, 99, 132, 0.8)',
            'rgba(54, 162, 235, 0.8)',
            'rgba(255, 206, 86, 0.8)',
            'rgba(75, 192, 192, 0.8)'
        ]
    }]
};

var pieOptions = {
    responsive: true,
    maintainAspectRatio: false
};

var pieChart = new Chart(document.getElementById('pieChart'), {
    type: 'pie',
    data: pieData,
    options: pieOptions
});
