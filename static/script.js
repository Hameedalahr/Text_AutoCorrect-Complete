async function predictWords() {
    let inputText = document.getElementById("inputText").value;

    if (inputText.length < 2) {
        document.getElementById("suggestions").innerHTML = "";
        return;
    }

    let response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText })
    });

    let data = await response.json();
    let suggestionsDiv = document.getElementById("suggestions");
    suggestionsDiv.innerHTML = "";

    if (data.predictions) {
        data.predictions.forEach(word => {
            let div = document.createElement("div");
            div.className = "suggestion";
            div.innerText = word;
            div.onclick = () => {
                let inputField = document.getElementById("inputText");
                let cursorPos = inputField.selectionStart;  // Get cursor position
                let textBefore = inputField.value.substring(0, cursorPos);
                let textAfter = inputField.value.substring(cursorPos);

                inputField.value = textBefore + " " + word + textAfter;
                inputField.focus(); // Keep the cursor active
                inputField.selectionStart = inputField.selectionEnd = cursorPos + word.length + 1;

                suggestionsDiv.innerHTML = "";
            };
            suggestionsDiv.appendChild(div);
        });
    }
}

async function correctGrammar() {
    let inputText = document.getElementById("inputText").value;

    if (inputText.trim() === "") {
        alert("Please enter text to correct.");
        return;
    }

    let response = await fetch("/correct", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText })
    });

    let data = await response.json();
    let correctedOutput = document.getElementById("correctedOutput");
    correctedOutput.innerHTML = `<strong>Corrected Sentence:</strong> ${data.corrected_text}`;
}
