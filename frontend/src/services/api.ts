export async function chatWithAgent(payload) {
    const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    if (!response.ok) {
        throw new Error("Backend error");


    }

    return response.json();



}

export async function uploadResume(file){
        
    const formData = new FormData();
    formData.append("file",file);

    const response = await fetch("http://localhost:8000/resume/upload", {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    throw new Error("Resume upload failed");
  }

  return response.json();
}

