async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;

    if (!message) return;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user">You: ${message}</div>`;
    input.value = "";

    const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    chatBox.innerHTML += `<div class="agent">Agent: ${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
