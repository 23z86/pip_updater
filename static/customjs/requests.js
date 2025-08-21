async function loadOutdated() {
    const loader = document.getElementById('loading');
    loader.style.display = 'block';

    const response = await fetch("/api/get_outdated_modules");

    const data = await response.json();

    if (!data || data.length === 0) {
        loader.style.display = 'none';
        outdatedData = [{
            latest_filetype: "No Data!",
            latest_version: "No Data!",
            name: "No Data!",
            version: "No Data!"
        }];
        await fillTable(outdatedData);
        return;
    }

    outdatedData = data;

    await fillTable(outdatedData);
    loader.style.display = 'none';
}

async function fillTable(data) {
    const tbody = document.querySelector("table tbody");
    const module_data = data.data;
    tbody.innerHTML = "";

    if (module_data.length === 0) {
        const row = document.createElement("tr");
        row.className = "center aligned";

        row.innerHTML = `
            <td colspan="4">No outdated packages found 🎉</td>           
        `;
        tbody.appendChild(row);
        return;
    }


    module_data.forEach(module => {
        const row = document.createElement("tr");
        row.className = "center aligned";

        row.innerHTML = `
            <td class="outdated"><a href="https://pypi.org/project/${module.name}"><b>${module.name}</b></a></td>
            <td>${module.version}</td>
            <td>${module.latest_version}</td>
            <td><button class="positive ui button" onClick="runUpdate('${module.name}', this)">Update</button></td>
            
        `;
        tbody.appendChild(row);
    });
}

function runUpdate(moduleName, button) {
    button.className = "ui loading button";

    fetch("/api/update", {
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
    });
}