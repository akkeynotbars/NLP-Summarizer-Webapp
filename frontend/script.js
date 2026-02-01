async function submitData() {
  const fileInput = document.getElementById("fileInput");
  const level = document.getElementById("summaryLevel").value;
  const button = document.getElementById("submitBtn");
  const loading = document.getElementById("loadingText");

  if (!fileInput.files.length) {
    alert("Upload file atau audio dulu!");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  formData.append("level", level);

  button.disabled = true;
  loading.classList.remove("hidden");

  try {
    const response = await fetch("http://localhost:8000/summarize", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    // Before
    document.getElementById("originalText").innerText =
      data.original_text || "-";

    // After (with entity highlight)
    document.getElementById("summaryText").innerHTML =
      highlightEntities(data.summary_text, data.entities);

    // Audio
    if (data.audio_url) {
      document.getElementById("summaryAudio").src = data.audio_url;
    }

    // Entity list
    renderEntities(data.entities);

  } catch (error) {
    alert("Gagal memproses data");
    console.error(error);
  }

  button.disabled = false;
  loading.classList.add("hidden");
}

function generate() {
  const btn = document.getElementById("generateBtn");
  btn.innerText = "Processing...";
  btn.disabled = true;

  setTimeout(() => {
    btn.innerText = "Generate";
    btn.disabled = false;
  }, 1000);

  // dummy data tetap jalan
}


// Render entity list
function renderEntities(entities) {
  const list = document.getElementById("entityList");
  list.innerHTML = "";

  if (!entities || entities.length === 0) {
    list.innerHTML = "<li>Tidak ada entity</li>";
    return;
  }

  entities.forEach(e => {
    const li = document.createElement("li");
    li.innerText = `${e.text} (${e.label})`;
    list.appendChild(li);
  });
}

// Highlight entity di summary
function highlightEntities(text, entities) {
  if (!entities || !text) return text;

  let result = text;

  let summaryText = "";


  entities.forEach(e => {
    const regex = new RegExp(`\\b${e.text}\\b`, "g");
    result = result.replace(regex, `<mark>${e.text}</mark>`);
  });

  return result;
}
