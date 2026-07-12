import api from "./api";

export async function generateBlueprint(idea) {
    const response = await api.post("/generate-blueprint", {
        idea,
        answers: [
            "General audience",
            "Web application",
            "Yes",
            "AI powered",
            "MVP"
        ]
    });

    console.log(response.data);

    return response.data;
}