document.querySelector('.btn').addEventListener('click', () => {
    alert('Button clicked!');
});


/*
document.addEventListener("DOMContentLoaded", () => {
    const handler = new ConversationHandler();

    async function someAsyncFunction() {
    try {
        const jsonResponse = await handler.respond();
        console.log("Received JSON:", jsonResponse);
        document.getElementById("content").innerText = JSON.stringify(jsonResponse.result);
        // Do something with the JSON data here
    } catch (error) {
        console.error("Error:", error);
    }
    }

    someAsyncFunction();

    async function anotherAsyncFunction() {

        const jsonResponse = await fetch("/api/list_models", {
            method: "GET",
        })
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                return json;
            });
    }
    anotherAsyncFunction()
});

*/