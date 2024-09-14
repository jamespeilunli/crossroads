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
});
