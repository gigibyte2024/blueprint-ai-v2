import api from "./api";

export async function generateBlueprint(
  idea,
  requestedModules = [
    "planning",
    "prd",
    "technical",
    "api",
    "database",
    "roadmap",
    "ui",
    "reflection",
  ]
) {
  const response = await api.post("/generate-blueprint", {
    idea,
    answers: [
      "General audience",
      "Web application",
      "Yes",
      "AI powered",
      "MVP",
    ],
    requested_modules: requestedModules,
  });

  console.log(response.data);

  return response.data;
}

export async function streamBlueprint(
  idea,
  requestedModules = [
    "planning",
    "prd",
    "technical",
    "api",
    "database",
    "roadmap",
    "ui",
    "reflection",
  ],
  onProgress,
  onComplete
) {
  const response = await fetch(
    "http://127.0.0.1:8000/generate-blueprint-stream",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        idea,
        answers: [
          "General audience",
          "Web application",
          "Yes",
          "AI powered",
          "MVP",
        ],
        requested_modules: requestedModules,
      }),
    }
  );

  if (!response.ok) {
    throw new Error("Failed to start blueprint generation");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  let buffer = "";

  while (true) {
    const { value, done } = await reader.read();

    if (done) break;

    buffer += decoder.decode(value, {
      stream: true,
    });

    const events = buffer.split("\n\n");

    buffer = events.pop() || "";

    for (const event of events) {
      if (!event.startsWith("data:")) {
        continue;
      }

      const jsonData = event
        .replace("data:", "")
        .trim();

      if (!jsonData) {
        continue;
      }

      const data = JSON.parse(jsonData);

      if (data.stage === "Complete") {
        onComplete(data);
      } else {
        onProgress(data);
      }
    }
  }
}