let intervalId = null;

const updateListeningText = () => {
    fetch("/static/data/dummy_data.txt") // Adjust the path as needed
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.text();
      })
      .then(text => {
        document.getElementById('listening').innerText = text;
      })
      .catch(error => {
        console.error('There was a problem with your fetch operation:', error);
      });
}

updateListeningText();
intervalId = setInterval(updateListeningText, 5000);

document.getElementById('startButton').addEventListener('click', () => {
    if (intervalId === null) {
      updateListeningText();
      intervalId = setInterval(updateListeningText, 5000);
    }
});

document.getElementById('stopButton').addEventListener('click', () => {
    if (intervalId !== null) {
      clearInterval(intervalId);
      intervalId = null;
      document.getElementById('listening').innerText = "";
    }
});

