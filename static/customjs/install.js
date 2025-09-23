import { getTranslations } from "./translation.js";
const translation = await getTranslations()

document.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        searchForPackage();
    }
});

document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        closePopUp();
    }
});

document.getElementById('install').addEventListener("load", setPopUp());

function setPopUp() {
    const install_div = document.getElementById('install');

    const reset_html = `
  <div class="ui icon input">
                    <input type="text" id="packageToSearch" placeholder="${translation["placeHolderSearch"]}">
                    <i class="inverted circular search link icon" onclick="searchForPackage()"></i>
                </div>
                <button id="download_button" onclick="runInstaller(this)" class="ui disabled button">
                    <i class="download icon"></i>
                    ${translation["install"]}
                </button>
                <button id="close" onclick="closePopUp()" class="ui inverted red button">
                    <i class="close icon"></i>
                </button>`;
    install_div.innerHTML = '';
    install_div.innerHTML = reset_html;
}

async function showInstallPopup() {
    const install_div = document.getElementById('install');
    install_div.style.display = 'block';

}

async function closePopUp() {
    const install_div = await document.getElementById('install');

    const reset_html = `
                <div class="ui icon input">
                    <input type="text" id="packageToSearch" placeholder="${translation["placeHolderSearch"]}">
                    <i class="inverted circular search link icon" onclick="searchForPackage()"></i>
                </div>
                <button id="download_button" onclick="runInstaller(this)" class="ui disabled button">
                    <i class="download icon"></i>
                    ${translation["install"]}
                </button>
                <button id="close" onclick="closePopUp()" class="ui inverted red button">
                    <i class="close icon"></i>
                </button>`;
    install_div.innerHTML = reset_html;
    install_div.style.display = 'none';


}

async function searchForPackage() {
    const downloadButton = document.getElementById('download_button');
    downloadButton.className = "ui loading button";
    downloadButton.disabled = "";
    var packageToSearch = await document.getElementById('packageToSearch').value;


    fetch(`/api/search_package?name=${packageToSearch}`, {
        method: "GET"

    }).then(response => response.json())
        .then(data => {
            if (data.status_code === 100) {
                downloadButton.className = "ui positive button";
                downloadButton.enabled = "";
            } else {
                console.warn(data.message);
                downloadButton.className = "ui disabled button";

            }
        })
        .catch(err => {
            console.error(err);
            downloadButton.className = "ui disabled button";

        });
}

async function runInstaller(button) {
    var packageToSearch = document.getElementById('packageToSearch').value;

    button.className = "ui loading button";
    button.disabled = "";


    await fetch("/api/install", {
        method: "POST",
        headers: { "Content-Type": "text/plain" },
        body: packageToSearch
    }).then(response => response.json())
        .then(data => {
            if (data.status_code === 100) {
                button.className = "ui positive button";
                button.enabled = "";

                showSuccessPopup();
            } else {
                console.warn(data.message);

            }
        })
        .catch(err => {
            console.warn(err);
        });
}

async function showSuccessPopup() {
    const successPopup = await document.getElementById('success_popup');

    const successPopupMessage = `
                <div class="ui icon input">
                    <p><b>${translation["installSuccess"]}</b></p>
                </div>
               `;

    successPopup.innerHTML = successPopupMessage;
    successPopup.style.display = 'flex';

    setTimeout(() => {
        successPopup.style.display = 'none';
    }, 2000);

}

(window).showInstallPopup = showInstallPopup;
(window).closePopUp = closePopUp;
(window).searchForPackage = searchForPackage;
(window).runInstaller = runInstaller;
