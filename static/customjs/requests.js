import { getTranslations } from "./translation.js";
const translation = await getTranslations()

async function loadOutdated() {
    const loader = document.getElementById('loading');
    loader.style.display = 'block';

    const response = await fetch("/api/get_outdated_packages");
    const data = await response.json();

    const outdatedData = data;

    await fillTable(outdatedData);
    loader.style.display = 'none';
}

async function fillTable(data) {
    const tbody = document.querySelector("table tbody");
    const pip_package_data = data.data;
    tbody.innerHTML = "";

    if (pip_package_data.length === 0) {
        const row = document.createElement("tr");
        row.className = "center aligned";

        row.innerHTML = `
            <td colspan="4">${translation["noOutdatedPackages"]}</td>           
        `;
        tbody.appendChild(row);
        return;
    }


    pip_package_data.forEach(pip_package => {
        const row = document.createElement("tr");
        row.className = "center aligned";

        row.innerHTML = `
            <td class="outdated"><a href="https://pypi.org/project/${pip_package.name}"><b>${pip_package.name}</b></a></td>
            <td>${pip_package.version}</td>
            <td>${pip_package.latest_version}</td>
            <td><button class="positive ui button fixed-button" onClick="runUpdate('${pip_package.name}', this)">${translation["updateButtonText"]}</button></td>
            
        `;
        tbody.appendChild(row);
    });
}

function runUpdate(pip_packageName, button) {
    button.className = "ui loading fixed-button button";

    fetch("/api/update", {
        method: "POST",
        headers: { "Content-Type": "text/plain" },
        body: pip_packageName
    }).then(response => response.json())
        .then(data => {
            if (data.status_code === 100) {
                const outdatedRow = document.getElementsByClassName("outdated");
                Array.from(outdatedRow).forEach(cell => {
                    if (cell.innerText.includes(pip_packageName)) {
                        button.className = "ui inverted green fixed-button button";
                        button.innerText = "Up-to-date";
                        button.disabled = "disabled";
                    }
                });
            } else {
                console.warn(translation["errorUpdateFailed"], data.message);
                button.className = "ui inverted red fixed-button button";
                button.innerText = translation['buttonTextFailed'];
                button.disabled = "disabled";

            }

            refreshTable();
        })
        .catch(err => {
            console.warn(translation["errorUpdateFailed"], err);
            button.className = "ui inverted red fixed-button button";
            button.innerText = translation['buttonTextFailed'];
            button.disabled = "disabled";

        });
}

function refreshTable() {
    const tbody = document.querySelector("table tbody");
    if (tbody?.rows.length === 0) {
        loadOutdated();
    }

}

(window).loadOutdated = loadOutdated;
(window).runUpdate = runUpdate;
