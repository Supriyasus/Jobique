document.addEventListener("DOMContentLoaded", function () {
    const generateBtn = document.getElementById("generateBtn");
    const btnText = document.getElementById("btnText");
    const loadingIcon = document.getElementById("loadingIcon");
    const coldEmailOutput = document.getElementById("cold-email-output");
    const coverLetterOutput = document.getElementById("cover-letter-output");

    if (generateBtn) {
        generateBtn.addEventListener("click", function () {
            generateBtn.disabled = true;
            btnText.textContent = "Generating...";
            loadingIcon.classList.remove("hidden");

            // Get form data
            const jobLink = document.getElementById("jobLink").value;
            const resumeInput = document.getElementById("resumeInput");
            const additionalInfo = document.getElementById("additionalInfo").value;

            // Create form data
            const formData = new FormData();
            formData.append("job_link", jobLink);
            formData.append("additional_info", additionalInfo);
            
            // Add resume file if selected
            if (resumeInput.files.length > 0) {
                formData.append("resume", resumeInput.files[0]);
            }

            // Send request to backend
            fetch("/generate-email", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Check if generate-email.html page is open
                if (coldEmailOutput && coverLetterOutput) {
                    coldEmailOutput.textContent = data.cold_email;
                    coverLetterOutput.textContent = data.cover_letter;
                } else {
                    // If not on generate-email page, redirect and store data
                    sessionStorage.setItem('coldEmail', data.cold_email);
                    sessionStorage.setItem('coverLetter', data.cover_letter);
                    window.location.href = "generate-email.html";
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Failed to generate email and cover letter");
            })
            .finally(() => {
                generateBtn.disabled = false;
                btnText.textContent = "Generate";
                loadingIcon.classList.add("hidden");
            });
        });
    }

    // Check if on generate-email page and retrieve stored data
    if (document.getElementById("cold-email-output")) {
        const storedColdEmail = sessionStorage.getItem('coldEmail');
        const storedCoverLetter = sessionStorage.getItem('coverLetter');

        if (storedColdEmail) {
            document.getElementById("cold-email-output").textContent = storedColdEmail;
            sessionStorage.removeItem('coldEmail');
        }

        if (storedCoverLetter) {
            document.getElementById("cover-letter-output").textContent = storedCoverLetter;
            sessionStorage.removeItem('coverLetter');
        }
    }
});