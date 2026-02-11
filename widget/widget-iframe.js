(function () {
    const BOT_TOKEN = document.currentScript.getAttribute("data-bot-token");

    if (!BOT_TOKEN) {
        console.error("PlutoChat: Missing data-bot-token attribute");
        return;
    }

    let sessionId = localStorage.getItem("plutochat_session_id");
    if (!sessionId) {
        sessionId = "sess_" + Math.random().toString(36).substr(2, 9) + Date.now();
        localStorage.setItem("plutochat_session_id", sessionId);
    }

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
        transition: transform 0.3s ease;
    `;
    bubble.innerHTML = "💬";
    document.body.appendChild(bubble);

    const iframe = document.createElement("iframe");
    iframe.id = "plutochat-iframe";
    iframe.src = `https://backend.plutoo.chat/widget/iframe/widget.html?bot_token=${BOT_TOKEN}&session_id=${sessionId}`;
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
    `;
    document.body.appendChild(iframe);

    let isOpen = false;
    bubble.onclick = () => {
        isOpen = !isOpen;
        iframe.style.display = isOpen ? "block" : "none";
        bubble.innerHTML = isOpen ? "✕" : "💬";
    };

    console.log("PlutoChat widget loaded successfully");
})();