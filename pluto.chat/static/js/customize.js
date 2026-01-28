const API_BASE = 'http://localhost:8000';

// Get elements
const primaryColorInput = document.getElementById('primaryColor');
const primaryColorText = document.getElementById('primaryColorText');
const textColorInput = document.getElementById('textColor');
const textColorText = document.getElementById('textColorText');
const fontFamilySelect = document.getElementById('fontFamily');
const positionRadios = document.querySelectorAll('input[name="position"]');
const welcomeMessageTextarea = document.getElementById('welcomeMessage');
const charCount = document.getElementById('charCount');
const saveBtn = document.getElementById('saveBtn');
const messageDiv = document.getElementById('message');

// Preview elements
const previewButton = document.getElementById('preview-button');
const previewHeader = document.getElementById('preview-header');
const previewWindow = document.getElementById('preview-window');
const previewWelcome = document.getElementById('preview-welcome');
const previewWidget = document.getElementById('preview-widget');
const previewMessages = document.querySelector('.preview-messages');
const previewInputArea = document.querySelector('.preview-input-area');

// Load current settings
async function loadSettings() {
    try {
        const token = localStorage.getItem('token');
        if (!token) {
            window.location.href = '/login.html';
            return;
        }

        const response = await fetch(`${API_BASE}/widget/settings`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            primaryColorInput.value = data.primaryColor;
            primaryColorText.value = data.primaryColor;
            textColorInput.value = data.textColor;
            textColorText.value = data.textColor;
            fontFamilySelect.value = data.fontFamily;
            welcomeMessageTextarea.value = data.welcomeMessage;
            
            positionRadios.forEach(radio => {
                if (radio.value === data.position) {
                    radio.checked = true;
                }
            });

            updatePreview();
            updateCharCount();
        }
    } catch (error) {
        console.error('Error loading settings:', error);
    }
}

// Update preview in real-time
function updatePreview() {
    const primaryColor = primaryColorInput.value;
    const textColor = textColorInput.value;
    const fontFamily = fontFamilySelect.value;
    const position = document.querySelector('input[name="position"]:checked').value;
    const welcomeMessage = welcomeMessageTextarea.value || 'Hi! How can I help you today?';

    // Update colors
    previewButton.style.background = primaryColor;
    previewHeader.style.background = primaryColor;
    previewHeader.style.color = textColor;
    previewInputArea.querySelector('button').style.background = primaryColor;

    // Update font
    previewWindow.style.fontFamily = fontFamily;

    // Update position
    if (position === 'bottom-left') {
        previewWidget.classList.add('left');
    } else {
        previewWidget.classList.remove('left');
    }

    // Update welcome message
    previewWelcome.textContent = welcomeMessage;
}

// Update character count
function updateCharCount() {
    const length = welcomeMessageTextarea.value.length;
    charCount.textContent = `${length} / 500 characters`;
}

// Save settings
async function saveSettings() {
    const primaryColor = primaryColorInput.value;
    const textColor = textColorInput.value;
    const fontFamily = fontFamilySelect.value;
    const position = document.querySelector('input[name="position"]:checked').value;
    const welcomeMessage = welcomeMessageTextarea.value || 'Hi! How can I help you today?';

    saveBtn.disabled = true;
    saveBtn.textContent = 'Saving...';
    messageDiv.className = 'message';
    messageDiv.style.display = 'none';

    try {
        const token = localStorage.getItem('token');
        const response = await fetch(`${API_BASE}/widget/customize`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': `Bearer ${token}`
            },
            body: new URLSearchParams({
                primary_color: primaryColor,
                text_color: textColor,
                font_family: fontFamily,
                position: position,
                welcome_message: welcomeMessage
            })
        });

        if (response.ok) {
            messageDiv.className = 'message success';
            messageDiv.textContent = '✓ Widget customization saved successfully!';
        } else {
            const error = await response.json();
            messageDiv.className = 'message error';
            messageDiv.textContent = `Error: ${error.detail || 'Failed to save settings'}`;
        }
    } catch (error) {
        messageDiv.className = 'message error';
        messageDiv.textContent = 'Error: Could not connect to server';
    } finally {
        saveBtn.disabled = false;
        saveBtn.textContent = 'Save Changes';
        
        setTimeout(() => {
            messageDiv.style.display = 'none';
        }, 5000);
    }
}

// Event listeners
primaryColorInput.addEventListener('input', (e) => {
    primaryColorText.value = e.target.value;
    updatePreview();
});

textColorInput.addEventListener('input', (e) => {
    textColorText.value = e.target.value;
    updatePreview();
});

fontFamilySelect.addEventListener('change', updatePreview);

positionRadios.forEach(radio => {
    radio.addEventListener('change', updatePreview);
});

welcomeMessageTextarea.addEventListener('input', () => {
    updateCharCount();
    updatePreview();
});

saveBtn.addEventListener('click', saveSettings);

// Preview button toggle
previewButton.addEventListener('click', () => {
    const isVisible = previewWindow.style.display === 'flex';
    previewWindow.style.display = isVisible ? 'none' : 'flex';
});

document.querySelector('.preview-close').addEventListener('click', () => {
    previewWindow.style.display = 'none';
});

// Initialize
loadSettings();
