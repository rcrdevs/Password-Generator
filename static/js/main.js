(function () {
    const lengthInput = document.getElementById("length");
    const generateBtn = document.getElementById("generate-btn");
    const outputWrap = document.getElementById("output-wrap");
    const passwordOutput = document.getElementById("password-output");
    const copyBtn = document.getElementById("copy-btn");
    const copyFeedback = document.getElementById("copy-feedback");
    const errorFeedback = document.getElementById("error-feedback");

    let currentPassword = "";

    function showError(msg) {
        errorFeedback.textContent = "erro: " + msg;
        errorFeedback.hidden = false;
        outputWrap.hidden = true;
        copyBtn.hidden = true;
    }

    async function generate() {
        errorFeedback.hidden = true;
        copyFeedback.hidden = true;
        const length = lengthInput.value;
        try {
            const res = await fetch(`/generate?length=${encodeURIComponent(length)}`);
            const data = await res.json();
            if (!res.ok) {
                showError(data.error || "não foi possível gerar a senha.");
                return;
            }
            currentPassword = data.password;
            passwordOutput.textContent = currentPassword;
            outputWrap.hidden = false;
            copyBtn.hidden = false;
        } catch (e) {
            showError("falha ao conectar com o servidor.");
        }
    }

    async function copyPassword() {
        if (!currentPassword) return;
        try {
            await navigator.clipboard.writeText(currentPassword);
            copyFeedback.hidden = false;
            setTimeout(() => { copyFeedback.hidden = true; }, 2000);
        } catch (e) {
            showError("não foi possível copiar (permissão do navegador).");
        }
    }

    generateBtn.addEventListener("click", generate);
    copyBtn.addEventListener("click", copyPassword);
    lengthInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") generate();
    });
})();
