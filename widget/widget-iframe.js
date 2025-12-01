// This file should be included in the CLIENT's website via <script> tag
// It creates the chat bubble and iframe

(function () {
    const BOT_TOKEN = document.currentScript.getAttribute("data-bot-token");

    if (!BOT_TOKEN) {
        console.error("PlutoChat: Missing data-bot-token attribute");
        return;
    }

    // Create a unique session ID for this visitor
    let sessionId = localStorage.getItem("plutochat_session_id");
    if (!sessionId) {
        sessionId = "sess_" + Math.random().toString(36).substr(2, 9) + Date.now();
        localStorage.setItem("plutochat_session_id", sessionId);
    }

    // Create chat bubble
    const bubble = document.createElement("div");
    bubble.id = "plutochat-bubble";
    bubble.style.cssText = `
        position: fixed;
        bottom: 25px;
        right: 25px;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        border-radius: 50%;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999999;
        color: white;
        font-size: 30px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    `;
    bubble.innerHTML = "💬";
    bubble.onmouseenter = () => {
        bubble.style.transform = "scale(1.1)";
        bubble.style.boxShadow = "0 6px 20px rgba(79, 70, 229, 0.5)";
    };
    bubble.onmouseleave = () => {
        bubble.style.transform = "scale(1)";
        bubble.style.boxShadow = "0 4px 15px rgba(79, 70, 229, 0.4)";
    };
    document.body.appendChild(bubble);

    // Create iframe (hidden initially)
    const iframe = document.createElement("iframe");
    iframe.id = "plutochat-iframe";
    iframe.src = `http://127.0.0.1:8000/widget/iframe/widget.html?bot_token=${BOT_TOKEN}&session_id=${sessionId}`;
    iframe.style.cssText = `
        position: fixed;
        bottom: 100px;
        right: 25px;
        width: 360px;
        height: 500px;
        border-radius: 12px;
        border: none;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
        display: none;
        z-index: 999999;
        transition: opacity 0.3s ease;
    `;
    document.body.appendChild(iframe);

    // Toggle chat open/close
    let isOpen = false;
    bubble.onclick = () => {
        isOpen = !isOpen;
        iframe.style.display = isOpen ? "block" : "none";
        bubble.innerHTML = isOpen ? "✕" : "💬";
    };

    console.log("PlutoChat widget loaded successfully");
})();