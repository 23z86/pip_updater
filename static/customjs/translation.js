function translate(key) {
    return translations[currentLang][key] || key;
}

async function setLanguage(lang) {
    currentLang = lang;

    const request = await fetch(`/static/i18n/${lang}.json`);
    const i18n = await request.json();

    document.getElementById("loading_text").innerText = i18n["loading_text"];

}