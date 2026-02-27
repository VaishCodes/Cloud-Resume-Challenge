const apiUrl = 'https://qpoybfb6x8.execute-api.eu-west-1.amazonaws.com/prod/visitors';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    document.getElementById('visitor-count').textContent = data.count;
  })
  .catch(error => {
    console.error('Error fetching visitor count:', error);
    document.getElementById('visitor-count').textContent = 'N/A';
  });