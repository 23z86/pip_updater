import { getTranslations } from "./translation.js";

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
    const translation = await getTranslations();

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
            <td><button class="positive ui button" onClick="runUpdate('${pip_package.name}', this)">Update</button></td>
            
        `;
        tbody.appendChild(row);
    });
}

function runUpdate(pip_packageName, button) {
    button.className = "ui loading button";

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
                        const row = cell.closest('tr');
                        if (row) row.remove();
                    }
                });
            } else {
                console.warn("Update failed:", data.message);
            }

            refreshTable();
        })
        .catch(err => {
            console.error("Fetch error:", err);
            alert("Network or server error during update.");
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
