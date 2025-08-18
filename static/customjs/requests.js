let outdatedData = null;

async function loadOutdated() {
    const loader = document.getElementById('loading');
    loader.style.display = 'block';
    if (!outdatedData) {

        const response = await fetch("/get_outdated_modules");
        outdatedData = await response.json();
    }
    await fillTable(outdatedData);
    loader.style.display = 'none';
}

async function fillTable(data) {
    const tbody = document.querySelector("table tbody");
    tbody.innerHTML = "";

    data.forEach(module => {
        const row = document.createElement("tr");
        row.className = "center aligned";

        row.innerHTML = `
            <td class="outdated"><a href="https://pypi.org/project/${module.name}"><b>${module.name}</b></a></td>
            <td>${module.version}</td>
            <td>${module.latest_version}</td>
            <td><button class="positive ui button" onClick="runUpdate('${module.name}')">Update</button></td>
            
        `;
        tbody.appendChild(row);
    });
}

function runUpdate(moduleName) {
    const loader = document.getElementById('loading');
    const loaderText = document.getElementById('loading_text');
    loaderText.textContent = "";
    loaderText.textContent = `Update für ${moduleName} läuft... Bitte warten!`;
    loader.style.display = 'block';

    fetch("/update", {
        method: "POST",
        headers: { "Content-Type": "text/plain" },
        body: moduleName
    }).then(() => {
        const outdatedRow = document.getElementsByClassName("outdated");
        Array.from(outdatedRow).forEach(cell => {
            if (cell.innerText.includes(moduleName)) {
                const row = cell.closest('tr');
                if (row) row.remove();
            }
        });

        loader.style.display = 'none';

    });
}