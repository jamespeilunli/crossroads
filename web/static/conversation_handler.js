class ConversationHandler {
    constructor() {
        this.paths = [[{ "role": "system", "content": "You are a helpful assistant." }], [{ "role": "system", "content": "You are a helpful assistant that loves starting words with the letter 'b'." }]];
    }

    respond() {
        return fetch("/api/get_response", {
            method: "POST",
            body: JSON.stringify({
                messages: this.paths[0]
            }),
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then((response) => response.json())
            .then((json) => {
                console.log("/api/get_response Success", json);
                return json;
            });
    }
}
