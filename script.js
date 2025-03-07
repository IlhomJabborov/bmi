document.addEventListener("DOMContentLoaded", function () {
    let editor = document.getElementById("editor");

    async function processText() {
        let text = editor.innerText.trim(); // Matnni olish
        if (!text) return; // Agar matn bo'sh bo'lsa, hech narsa qilmaymiz

        try {
            let response = await fetch("http://127.0.0.1:8000/process_text/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: text }) // JSON formatda yuborish
            });

            if (!response.ok) throw new Error("Serverdan noto‘g‘ri javob keldi!");

            let data = await response.json(); // JSON formatida natijani olish
            updateText(data); // Matnni yangilash
            console.log("Natija:", data);
        } catch (error) {
            console.error("Xatolik:", error);
        }
    }

    function updateText(data) {
        if (!data || !data.filtered_text || !data.removed_stopwords) {
            console.error("Xatolik: API javobi noto‘g‘ri formatda!");
            return;
        }

        let words = editor.innerText.split(/\s+/); // Hamma so‘zlarni olish
        let stopWords = Object.keys(data.removed_stopwords);
        let totalWords = words.length;
        let stopWordCount = data.total_stopwords;

        let highlightedText = words.map(word => {
            let cleanedWord = word.replace(/[^\w'`’-]/g, ""); // Punktuatsiyani olib tashlash
            if (stopWords.includes(cleanedWord)) {
                return `<span class="highlight">${word}</span>`; // Stop so‘zlarni belgilash
            }
            return word;
        }).join(" ");

        let percentage = totalWords > 0 ? ((stopWordCount / totalWords) * 100).toFixed(2) : 0;

        document.getElementById("totalWordsCount").innerText = totalWords;
        document.getElementById("stopWordsCount").innerText = stopWordCount;
        document.getElementById("stopWordsPercentage").innerText = percentage + "%";
        editor.innerHTML = highlightedText;
    }

    editor.addEventListener("input", function () {
        processText();
    });
});
