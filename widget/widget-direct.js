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
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%); padding: 20px; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); margin: 12px 0; border: 1px solid #e2e8f0;">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 2px solid #e2e8f0;">
                        <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #4f46e5 0%, #2ED0E6 100%); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 20px;">🎫</div>
                        <div>
                            <h3 style="margin: 0; color: #1e293b; font-size: 17px; font-weight: 700;">Create Support Ticket</h3>
                            <p style="margin: 2px 0 0 0; color: #64748b; font-size: 12px;">We'll get back to you within 24 hours</p>
                        </div>
                    </div>
                    <div style="margin-bottom: 12px;">
                        <label style="display: block; color: #475569; font-size: 13px; font-weight: 600; margin-bottom: 6px;">Full Name <span style="color: #ef4444;">*</span></label>
                        <input type="text" id="ticket-name" placeholder="John Doe" style="width: 100%; padding: 11px 12px; border: 1.5px solid #e2e8f0; border-radius: 8px; box-sizing: border-box; font-size: 14px; transition: all 0.2s; outline: none;" onfocus="this.style.borderColor='#4f46e5'; this.style.boxShadow='0 0 0 3px rgba(79,70,229,0.1)';" onblur="this.style.borderColor='#e2e8f0'; this.style.boxShadow='none';" />
                    </div>
                    <div style="margin-bottom: 12px;">
                        <label style="display: block; color: #475569; font-size: 13px; font-weight: 600; margin-bottom: 6px;">Email Address <span style="color: #ef4444;">*</span></label>
                        <input type="email" id="ticket-email" placeholder="john@example.com" style="width: 100%; padding: 11px 12px; border: 1.5px solid #e2e8f0; border-radius: 8px; box-sizing: border-box; font-size: 14px; transition: all 0.2s; outline: none;" onfocus="this.style.borderColor='#4f46e5'; this.style.boxShadow='0 0 0 3px rgba(79,70,229,0.1)';" onblur="this.style.borderColor='#e2e8f0'; this.style.boxShadow='none';" />
                    </div>
                    <div style="margin-bottom: 12px;">
                        <label style="display: block; color: #475569; font-size: 13px; font-weight: 600; margin-bottom: 6px;">Phone Number <span style="color: #94a3b8; font-weight: 400;">(Optional)</span></label>
                        <input type="tel" id="ticket-phone" placeholder="+1 (555) 000-0000" style="width: 100%; padding: 11px 12px; border: 1.5px solid #e2e8f0; border-radius: 8px; box-sizing: border-box; font-size: 14px; transition: all 0.2s; outline: none;" onfocus="this.style.borderColor='#4f46e5'; this.style.boxShadow='0 0 0 3px rgba(79,70,229,0.1)';" onblur="this.style.borderColor='#e2e8f0'; this.style.boxShadow='none';" />
                    </div>
                    <div style="margin-bottom: 16px;">
                        <label style="display: block; color: #475569; font-size: 13px; font-weight: 600; margin-bottom: 6px;">Issue Description <span style="color: #ef4444;">*</span></label>
                        <textarea id="ticket-issue" placeholder="Please describe your issue in detail..." rows="4" style="width: 100%; padding: 11px 12px; border: 1.5px solid #e2e8f0; border-radius: 8px; resize: vertical; box-sizing: border-box; font-size: 14px; font-family: inherit; transition: all 0.2s; outline: none;" onfocus="this.style.borderColor='#4f46e5'; this.style.boxShadow='0 0 0 3px rgba(79,70,229,0.1)';" onblur="this.style.borderColor='#e2e8f0'; this.style.boxShadow='none';"></textarea>
                    </div>
                    <div style="display: flex; gap: 10px;">
                        <button id="submit-ticket-btn" style="flex: 1; padding: 12px; background: linear-gradient(135deg, #4f46e5 0%, #2ED0E6 100%); color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 14px; transition: all 0.2s; box-shadow: 0 2px 8px rgba(79,70,229,0.3);" onmouseover="this.style.transform='translateY(-1px)'; this.style.boxShadow='0 4px 12px rgba(79,70,229,0.4)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(79,70,229,0.3)';">Submit Ticket</button>
                        <button id="cancel-ticket-btn" style="flex: 1; padding: 12px; background: #f1f5f9; color: #475569; border: 1.5px solid #e2e8f0; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 14px; transition: all 0.2s;" onmouseover="this.style.background='#e2e8f0';" onmouseout="this.style.background='#f1f5f9';">Cancel</button>
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