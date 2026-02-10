(function () {
    const BOT_TOKEN = document.currentScript.getAttribute("data-bot-token");
    if (!BOT_TOKEN) {
        console.error("PlutoChat: Missing data-bot-token attribute");
        return;
    }

    const scriptSrc = document.currentScript.src;
    const BASE_URL = scriptSrc ? new URL(scriptSrc).origin : 'http://localhost:8000';

    let sessionId = localStorage.getItem("plutochat_session_id");
    if (!sessionId) {
        sessionId = "sess_" + Math.random().toString(36).substr(2, 9) + Date.now();
        localStorage.setItem("plutochat_session_id", sessionId);
    }

    const API_URL = `${BASE_URL}/chat/`;
    const CONFIG_URL = `${BASE_URL}/widget/config/${BOT_TOKEN}`;
    const TICKET_API_URL = `${BASE_URL}/tickets/create`;
    let isSending = false;
    let config = {
        primaryColor: "#4f46e5",
        textColor: "#ffffff",
        fontFamily: "Arial, sans-serif",
        position: "bottom-right",
        welcomeMessage: "Hi! How can I help you today?"
    };



    
    // Fetch widget configuration
    async function loadConfig() {
        try {
            const res = await fetch(CONFIG_URL);
            if (res.ok) {
                config = await res.json();
            }
        } catch (error) {
            console.warn("PlutoChat: Using default config");
        }
        initWidget();
    }

    function initWidget() {
        const isLeft = config.position === "bottom-left";
        const positionStyle = isLeft ? "left: 25px;" : "right: 25px;";

        // Create bubble
        const bubble = document.createElement("div");
        bubble.style.cssText = `
            position: fixed; bottom: 25px; ${positionStyle} width: 60px; height: 60px;
            background: ${config.primaryColor};
            border-radius: 50%; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            cursor: pointer; display: flex; align-items: center; justify-content: center;
            z-index: 999999; color: white; font-size: 30px;
        `;
        bubble.innerHTML = "💬";
        document.body.appendChild(bubble);

        // Create chat widget
        const widget = document.createElement("div");
        widget.style.cssText = `
            position: fixed; bottom: 100px; ${positionStyle} width: 360px; height: 500px;
            background: white; border-radius: 12px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
            display: none; z-index: 999999; font-family: ${config.fontFamily};
        `;
        
        widget.innerHTML = `
            <div style="height: 100%; display: flex; flex-direction: column;">
                <div style="padding: 15px; background: ${config.primaryColor}; color: ${config.textColor}; border-radius: 12px 12px 0 0;">
                    <h3 style="margin: 0; font-size: 16px;">Chat Support</h3>
                </div>
                <div id="messages" style="flex: 1; overflow-y: auto; padding: 15px; background: #fafafa;"></div>
                <div style="padding: 15px; border-top: 1px solid #eee;">
                    <div style="display: flex; gap: 8px;">
                        <input type="text" id="chat-input" placeholder="Type your message..." 
                               style="flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 6px; outline: none;">
                        <button id="send-btn" style="padding: 10px 20px; background: ${config.primaryColor}; color: ${config.textColor}; 
                                                      border: none; border-radius: 6px; cursor: pointer;">Send</button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(widget);

        const messagesDiv = widget.querySelector("#messages");
        const input = widget.querySelector("#chat-input");
        const sendBtn = widget.querySelector("#send-btn");

        // Add welcome message
        addMessage(config.welcomeMessage, "bot");

        function addMessage(text, type) {
            const msgContainer = document.createElement("div");
            msgContainer.style.cssText = `margin: 8px 0;`;
            
            const msg = document.createElement("div");
            msg.style.cssText = `
                padding: 10px; border-radius: 8px; max-width: 80%;
                ${type === 'user' ? `background: ${config.primaryColor}; color: ${config.textColor}; margin-left: auto; text-align: right;` : 'background: #f5f5f5; margin-right: auto;'}
            `;
            msg.textContent = text;
            msgContainer.appendChild(msg);
            
            // Check if bot message suggests ticket
            if (type === 'bot') {
                const lowerText = text.toLowerCase();
                if (lowerText.includes("raise a support ticket") || 
                    lowerText.includes("raise a ticket") ||
                    lowerText.includes("create a ticket") ||
                    lowerText.includes("support ticket") ||
                    lowerText.includes("click the button below")) {
                    
                    const ticketBtn = document.createElement("button");
                    ticketBtn.style.cssText = `
                        background: linear-gradient(135deg, #4f46e5 0%, #2ED0E6 100%);
                        color: white; border: none; padding: 10px 16px; border-radius: 8px;
                        cursor: pointer; font-size: 14px; font-weight: 600; margin-top: 8px;
                        max-width: 250px;
                    `;
                    ticketBtn.textContent = "🎫 Raise Support Ticket";
                    ticketBtn.onclick = () => showTicketForm();
                    msgContainer.appendChild(ticketBtn);
                }
            }
            
            messagesDiv.appendChild(msgContainer);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        function showTicketForm() {
            const formHTML = `
                <div style="background: white; padding: 16px; border-radius: 12px; border: 2px solid #4f46e5; margin: 12px 0;">
                    <h3 style="margin: 0 0 12px 0; color: #1e293b; font-size: 16px;">🎫 Raise Support Ticket</h3>
                    <input type="text" id="ticket-name" placeholder="Your Name *" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box;" />
                    <input type="email" id="ticket-email" placeholder="Your Email *" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box;" />
                    <input type="tel" id="ticket-phone" placeholder="Phone (optional)" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box;" />
                    <textarea id="ticket-issue" placeholder="Describe your issue... *" rows="4" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 6px; resize: vertical; box-sizing: border-box;"></textarea>
                    <div style="display: flex; gap: 8px;">
                        <button id="submit-ticket-btn" style="flex: 1; padding: 10px; background: #4f46e5; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Submit</button>
                        <button id="cancel-ticket-btn" style="flex: 1; padding: 10px; background: #e5e7eb; color: #374151; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Cancel</button>
                    </div>
                </div>
            `;
            
            const formContainer = document.createElement("div");
            formContainer.innerHTML = formHTML;
            messagesDiv.appendChild(formContainer);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
            
            document.getElementById("submit-ticket-btn").onclick = async () => {
                const name = document.getElementById("ticket-name").value.trim();
                const email = document.getElementById("ticket-email").value.trim();
                const phone = document.getElementById("ticket-phone").value.trim();
                const issue = document.getElementById("ticket-issue").value.trim();
                
                if (!name || !email || !issue) {
                    alert("Please fill in all required fields");
                    return;
                }
                
                formContainer.remove();
                addMessage("Submitting your ticket...", "bot");
                
                try {
                    const res = await fetch(TICKET_API_URL, {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({
                            bot_token: BOT_TOKEN,
                            session_id: sessionId,
                            name, email, phone: phone || null, issue
                        })
                    });
                    
                    const data = await res.json();
                    if (res.ok) {
                        addMessage(`✅ Ticket #${data.ticket_id} created! We'll contact you at ${email}.`, "bot");
                    } else {
                        addMessage("❌ Failed to create ticket. Please try again.", "bot");
                    }
                } catch (error) {
                    addMessage("❌ Error creating ticket. Please try again.", "bot");
                }
            };
            
            document.getElementById("cancel-ticket-btn").onclick = () => {
                formContainer.remove();
                addMessage("Ticket cancelled. How else can I help?", "bot");
            };
        }

        async function sendMessage() {
            if (isSending) return;
            const text = input.value.trim();
            if (!text) return;
            
            isSending = true;
            addMessage(text, "user");
            input.value = "";
            sendBtn.disabled = true;
            
            try {
                const res = await fetch(API_URL, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        bot_token: BOT_TOKEN,
                        session_id: sessionId,
                        message: text
                    })
                });
                
                if (res.ok) {
                    const data = await res.json();
                    addMessage(data.reply, "bot");
                } else {
                    addMessage("Sorry, something went wrong. Please try again.", "bot");
                }
            } catch (error) {
                addMessage("Sorry, something went wrong. Please try again.", "bot");
            } finally {
                isSending = false;
                sendBtn.disabled = false;
                input.focus();
            }
        }

        let isOpen = false;
        bubble.onclick = () => {
            isOpen = !isOpen;
            widget.style.display = isOpen ? "block" : "none";
            bubble.innerHTML = isOpen ? "✕" : "💬";
        };

        sendBtn.onclick = sendMessage;
        input.addEventListener("keypress", (e) => {
            if (e.key === "Enter") {
                e.preventDefault();
                sendMessage();
            }
        });

        console.log("PlutoChat widget loaded successfully");
    }

    // Load config and initialize
    loadConfig();
})();