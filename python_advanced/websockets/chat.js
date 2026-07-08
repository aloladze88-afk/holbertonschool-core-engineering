const socket = new WebSocket("ws://localhost:8000/ws");

const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("messages");
const statusText = document.getElementById("status");

function addMessage(text) {
    const message = document.createElement("div");

    message.className = "message";
    message.textContent = text;

    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
}

socket.onopen = function () {
    statusText.textContent = "Connected";
};

socket.onclose = function () {
    statusText.textContent = "Disconnected";
};

socket.onerror = function () {
    statusText.textContent = "Connection error";
};

socket.onmessage = function (event) {
    addMessage(event.data);
};

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const text = input.value.trim();

    if (text === "") {
        return;
    }

    socket.send(text);
    input.value = "";
});