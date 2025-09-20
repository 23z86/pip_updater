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

async function downloadNewPackage() {
    const install_div = document.getElementById('install');
    install_div.style.display = 'block';

}

function closePopUp() {
    const install_div = document.getElementById('install');

    const reset_html = `
                <div class="ui icon input">
                    <input type="text" id="packageToSearch" placeholder="Search package...">
                    <i class="inverted circular search link icon" onclick="searchForPackage()"></i>
                </div>
                <button id="download_button" class="ui active button">
                    <i class="download icon"></i>
                    Install
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
        });
}

function runInstaller(button) {
    var packageToSearch = document.getElementById('packageToSearch').value;

    button.className = "ui loading button";
    button.disabled = "";

    fetch("/api/install", {
        method: "POST",
        headers: { "Content-Type": "text/plain" },
        body: packageToSearch
    }).then(response => response.json())
        .then(data => {
            if (data.status_code === 100) {
                console.log(data);
                button.className = "ui positive button";
                button.enabled = "";
            } else {
                console.warn(data.message);

            }
        })
        .catch(err => {
            console.warn(err);
        });
}

(window).downloadNewPackage = downloadNewPackage;
(window).closePopUp = closePopUp;
(window).searchForPackage = searchForPackage;
(window).runInstaller = runInstaller;
