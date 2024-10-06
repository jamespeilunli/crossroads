

document.addEventListener("DOMContentLoaded", async function () {
    document.getElementById('api-key-form')?.addEventListener('submit', async function (event) {
        event.preventDefault();
        var apiKey = document.getElementById('api-key').value;
        localStorage.setItem('openaiAPIKey', apiKey);

        const jsonResponse = await fetch("/api/send_key", {
            method: "POST",
            body: JSON.stringify({
                apiKey: apiKey
            }),
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then((response) => response.json())
            .then((json) => {
                console.log("/api/send_key success")
                return json;
            });
    });

    const handler = new ConversationHandler();

    try {
        const jsonResponse = await handler.respond();

        document.getElementById("content").innerHTML += `<p>Current Messages: ${JSON.stringify(jsonResponse.result)}</p>`;
    } catch (error) {
        console.error("Error:", error);
    }

    try {
        const jsonResponse = await fetch("/api/list_models", {
            method: "GET",
        })
            .then((response) => response.json())
            .then((json) => {
                console.log("/api/list_models Success", json);
                return json;
            });

        document.getElementById("content").innerHTML += `<p>Availiable Models: ${JSON.stringify(jsonResponse.result)}</p>`;
    } catch (error) {
        console.error("Error:", error);
    }
});
