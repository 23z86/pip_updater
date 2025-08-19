let outdatedData = null;

async function loadOutdated() {
    const loader = document.getElementById('loading');
    loader.style.display = 'block';
    if (!outdatedData) {

        const response = await fetch("/get_outdated_modules");

        if (response.text.length === 0) {
            loader.style.display = 'none';
            const obj = {
                latest_filetype: "No Data!",
                latest_version: "No Data!",
                name: "No Data!",
                version: "No Data!"
            };

            outdatedData = [obj];
            await fillTable(outdatedData);
            return;
        }

        outdatedData = await response.json();
    }
    await fillTable(outdatedData);
    loader.style.display = 'none';
}

async function fillTable(data) {
    const tbody = document.querySelector("table tbody");
    tbody.innerHTML = "";

    if (data[0].name === "No Data!") {
        const row = document.createElement("tr");
        row.className = "center aligned";

        row.innerHTML = `
            <td>🎉</td>            
            <td>🎉</td>            
            <td>🎉</td>            
            <td>🎉</td>            
        `;
        tbody.appendChild(row);
        return;
    }


    data.forEach(module => {
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
    });
}