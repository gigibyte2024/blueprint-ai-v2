import api from "./api";

export async function generateBlueprint(idea, requestedModules = [
  "planning",
  "prd",
  "technical",
  "api",
  "database",
  "roadmap",
  "ui",
  "reflection",
]) {

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