// frontend/script.js
document.getElementById('analyzeButton').addEventListener('click', async () => {
    const inputText = document.getElementById('inputText').value;
    if (!inputText) {
        alert('Please enter some text to analyze.');
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    });

    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});
