let intervalId = null; // This will store the interval ID

function updateListeningText() {
    // Assuming 'listening.txt' is the text file you want to fetch.
    // Replace the URL with the actual path to your text file.
    fetch('dummy_data.txt')
      .then(response => {
        // Check if the request was successful
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.text();
      })
      .then(text => {
        // Update the content of the listening div with the fetched text
        document.getElementById('listening').innerText = text;
      })
      .catch(error => {
        console.error('There was a problem with your fetch operation:', error);
      });
  }

document.getElementById('startButton').addEventListener('click', () => {
if (intervalId === null) { // Start only if not already started
  updateListeningText(); // Update immediately then start interval
  intervalId = setInterval(updateListeningText, 5000);
}
});

document.getElementById('stopButton').addEventListener('click', () => {
if (intervalId !== null) {
  clearInterval(intervalId); // Stop the interval
  intervalId = null; // Reset the interval ID
  document.getElementById('listening').innerText = "";
}
 });
