document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('download-form');
    const statusMessage = document.getElementById('status-message');
    const statusIcon = document.querySelector('.status-icon');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(form);
        
        statusIcon.innerHTML = `
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <path d="M12 6v6M12 16h.01"/>
            </svg>
        `;
        statusIcon.classList.add('downloading');
        statusMessage.textContent = "Download em andamento...";

        try {
            const response = await fetch('/download_playlist/', {
                method: 'POST',
                body: formData,
            });
            const result = await response.json();
            
            statusIcon.classList.remove('downloading');
            statusIcon.classList.add('complete');
            statusIcon.innerHTML = `
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                    <path d="M20 6L9 17l-5-5"/>
                </svg>
            `;
            statusMessage.textContent = result.detail;
        } catch (error) {
            statusIcon.classList.remove('downloading');
            statusMessage.textContent = "Erro ao iniciar o download. Tente novamente.";
        }
    });
});