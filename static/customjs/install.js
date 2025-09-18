import { getTranslations } from "./translation.js";
const translation = await getTranslations()

async function downloadNewPackage() {
    const loader = document.getElementById('install');
    loader.style.display = 'block';

}

function closePopUp() {
    const loader = document.getElementById('install');
    loader.style.display = 'none';
}   


(window).downloadNewPackage = downloadNewPackage;
(window).closePopUp = closePopUp;
