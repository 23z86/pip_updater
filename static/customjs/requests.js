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
            <td><a href="https://pypi.org/project/${module.name}"><b>${module.name}</b></a></td>
            <td>${module.version}</td>
            <td>${module.latest_version}</td>
            <td><button class="positive ui button">Update</button></td>
            
        `;
        tbody.appendChild(row);
    });
}