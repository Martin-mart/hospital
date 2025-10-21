fetch("/patients/api/profiles/")
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("patients-list");
    data.forEach(patient => {
      const div = document.createElement("div");
      div.className = "patient-card";
      div.innerHTML = `<h3>${patient.name}</h3><p>Age: ${patient.age}</p>`;
      container.appendChild(div);
    });
  });
