// Get URL parameters
const urlParams = new URLSearchParams(window.location.search);
const botToken = urlParams.get("bot_token");
const sessionId = urlParams.get("session_id");

const API_URL = "http://localhost:8000/chat/";
const TICKET_API_URL = "http://localhost:8000/tickets/create";

const messagesDiv = document.getElementById("messages");
const input = document.getElementById("chat-input");
const sendBtn = document.getElementById("send-btn");

// Simple message without ticket option
function addMessage(text, type) {
    const msg = document.createElement("div");
    msg.className = "message " + type + " message-appear";
    msg.textContent = text;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    return msg;
}

// Add typing indicator
function addTypingIndicator() {
    const indicator = document.createElement("div");
    indicator.className = "typing-indicator";
    indicator.id = "typing-indicator";
    indicator.textContent = "AI is typing";
    messagesDiv.appendChild(indicator);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    return indicator;
}

// Remove typing indicator
function removeTypingIndicator() {
    const indicator = document.getElementById("typing-indicator");
    if (indicator) {
        indicator.remove();
    }
}

// Stream message character by character
function streamMessage(text, type, onComplete) {
    const msgContainer = document.createElement("div");
    msgContainer.className = "message-container";
    
    const msg = document.createElement("div");
    msg.className = "message " + type + " streaming-msg message-appear";
    msg.textContent = "";
    
    msgContainer.appendChild(msg);
    messagesDiv.appendChild(msgContainer);
    
    let index = 0;
    const streamInterval = setInterval(() => {
        if (index < text.length) {
            msg.textContent += text[index];
            index++;
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        } else {
            clearInterval(streamInterval);
            msg.classList.remove("streaming-msg");
            
            // Check for ticket option after streaming is complete
            const lowerText = text.toLowerCase();
            if (lowerText.includes("support ticket") || 
                lowerText.includes("raise a ticket") ||
                lowerText.includes("raise ticket") ||
                lowerText.includes("create a ticket") ||
                lowerText.includes("create ticket")) {
                
                const ticketBtn = document.createElement("button");
                ticketBtn.className = "raise-ticket-btn";
                ticketBtn.textContent = "🎫 Raise Support Ticket";
                ticketBtn.onclick = () => showTicketForm();
                
                msgContainer.appendChild(ticketBtn);
            }
            
            if (onComplete) onComplete();
        }
    }, 20); // Adjust speed here (lower = faster)
    
    return msgContainer;
}

// Message with ticket button detection (non-streaming)
function addMessageWithTicketOption(text, type) {
    const msgContainer = document.createElement("div");
    msgContainer.className = "message-container";
    
    const msg = document.createElement("div");
    msg.className = "message " + type + " message-appear";
    msg.textContent = text;
    
    msgContainer.appendChild(msg);
    
    // Check if the response mentions support ticket
    const lowerText = text.toLowerCase();
    if (lowerText.includes("support ticket") || 
        lowerText.includes("raise a ticket") ||
        lowerText.includes("raise ticket") ||
        lowerText.includes("create a ticket") ||
        lowerText.includes("create ticket")) {
        
        const ticketBtn = document.createElement("button");
        ticketBtn.className = "raise-ticket-btn";
        ticketBtn.textContent = "🎫 Raise Support Ticket";
        ticketBtn.onclick = () => showTicketForm();
        
        msgContainer.appendChild(ticketBtn);
    }
    
    messagesDiv.appendChild(msgContainer);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Show ticket form
function showTicketForm() {
    // Remove any existing ticket form
    const existingForm = document.querySelector(".ticket-form-container");
    if (existingForm) existingForm.remove();
    
    const formContainer = document.createElement("div");
    formContainer.className = "ticket-form-container";
    
    formContainer.innerHTML = `
        <div class="ticket-form">
            <h3>🎫 Raise Support Ticket</h3>
            <input type="text" id="ticket-name" placeholder="Your Name *" required />
            <input type="email" id="ticket-email" placeholder="Your Email *" required />
            <input type="tel" id="ticket-phone" placeholder="Phone Number (optional)" />
            <textarea id="ticket-issue" placeholder="Describe your issue... *" rows="4" required></textarea>
            <div class="ticket-form-actions">
                <button class="submit-ticket-btn" onclick="submitTicket()">Submit Ticket</button>
                <button class="cancel-ticket-btn" onclick="cancelTicket()">Cancel</button>
            </div>
        </div>
    `;
    
    messagesDiv.appendChild(formContainer);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Submit ticket
async function submitTicket() {
    const name = document.getElementById("ticket-name")?.value.trim();
    const email = document.getElementById("ticket-email")?.value.trim();
    const phone = document.getElementById("ticket-phone")?.value.trim();
    const issue = document.getElementById("ticket-issue")?.value.trim();
    
    if (!name || !email || !issue) {
        alert("Please fill in all required fields (Name, Email, and Issue)");
        return;
    }
    
    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address");
        return;
    }
    
    // Remove the form
    const formContainer = document.querySelector(".ticket-form-container");
    if (formContainer) formContainer.remove();
    
    // Show loading message
    addMessage("Submitting your ticket...", "bot-msg");
    
    try {
        const res = await fetch(TICKET_API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                bot_token: botToken,
                session_id: sessionId,
                name: name,
                email: email,
                phone: phone || null,
                issue: issue
            })
        });
        
        const data = await res.json();
        
        if (res.ok) {
            streamMessage(`✅ Ticket created successfully! Your ticket ID is: ${data.ticket_id}. Our team will contact you soon at ${email}.`, "bot-msg");
        } else {
            streamMessage("❌ Failed to create ticket. Please try again or contact support directly.", "bot-msg");
        }
    } catch (error) {
        console.error("Error creating ticket:", error);
        streamMessage("❌ An error occurred while creating the ticket. Please try again later.", "bot-msg");
    }
}

// Cancel ticket form
function cancelTicket() {
    const formContainer = document.querySelector(".ticket-form-container");
    if (formContainer) formContainer.remove();
    streamMessage("Ticket creation cancelled. How else can I help you?", "bot-msg");
}

// Send chat message with streaming response
async function sendMessage() {
    const text = input.value.trim();
    if (!text) return;

    addMessage(text, "user-msg");

    input.value = "";
    sendBtn.disabled = true;

    // Add typing indicator
    const typingIndicator = addTypingIndicator();

    try {
        const res = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                bot_token: botToken,
                session_id: sessionId,
                message: text
            })
        });

        if (!res.ok) {
            throw new Error("Failed to get response from server");
        }

        const data = await res.json();

        // Remove typing indicator
        removeTypingIndicator();

        // Stream the response
        streamMessage(data.reply, "bot-msg", () => {
            sendBtn.disabled = false;
            input.focus();
        });

    } catch (error) {
        console.error("Error:", error);
        removeTypingIndicator();
        addMessage("Sorry, something went wrong. Please try again.", "bot-msg");
        sendBtn.disabled = false;
        input.focus();
    }
}

// Event listeners
sendBtn.onclick = sendMessage;

input.addEventListener("keypress", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// Make functions globally accessible for inline onclick handlers
window.submitTicket = submitTicket;
window.cancelTicket = cancelTicket;
window.showTicketForm = showTicketForm;

// Log initialization
console.log("Chat widget initialized");
console.log("Bot Token:", botToken);
console.log("Session ID:", sessionId);