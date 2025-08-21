export async function getTranslations() {
    const currentLang = navigator.language || "en";

    const request = await fetch(`/static/i18n/${currentLang}.json`);
    const i18n = await request.json();

    return i18n;
}

async function setFieldsByLanguage() {

    const i18n = await getTranslations();

    document.getElementById("loading_text").innerText = i18n["loading_text"];
    document.getElementById("th_package").innerText = i18n["package"];
    document.getElementById("th_version").innerText = i18n["version"];
    document.getElementById("th_current_version").innerText = i18n["currentVersion"];
    document.getElementById("th_action").innerText = i18n["action"];
    document.getElementById("td_packages").innerText = i18n["noOutdatedPackages"];

}

window.addEventListener("load", async () => {
    await setFieldsByLanguage();
});