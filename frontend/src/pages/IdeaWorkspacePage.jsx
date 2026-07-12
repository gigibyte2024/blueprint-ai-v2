import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Sparkles } from "lucide-react";

import Navbar from "../components/Navbar";
import Card from "../components/Card";
import Button from "../components/Button";
import TextArea from "../components/TextArea";

import { generateBlueprint } from "../services/blueprintService";

export default function IdeaWorkspacePage() {
  const navigate = useNavigate();

  const [idea, setIdea] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleGenerate() {
    if (!idea.trim()) {
      alert("Please enter your startup idea.");
      return;
    }

    try {
      setLoading(true);

      const response = await generateBlueprint(idea);

      sessionStorage.setItem(
        "blueprint",
        JSON.stringify(response.blueprint)
      );

      navigate("/dashboard");
    } catch (err) {
      console.error(err);
      alert("Generation failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-950">

      <Navbar />

      <div className="max-w-4xl mx-auto py-16 px-6">

        <Card>

          <div className="text-center mb-10">

            <Sparkles
              className="mx-auto mb-4 text-violet-500"
              size={42}
            />

            <h1 className="text-4xl font-bold text-white">
              Describe your Product Idea
            </h1>

            <p className="text-slate-400 mt-3">
              The more details you provide, the better your AI-generated
              blueprint will be.
            </p>

          </div>

          <TextArea
            rows={10}
            placeholder="Example: Build an AI platform that helps college students prepare for placements by generating personalized roadmaps, mock interviews and resume reviews..."
            value={idea}
            onChange={(e) => setIdea(e.target.value)}
          />

          <div className="mt-8 flex justify-center">

            <Button
              onClick={handleGenerate}
              disabled={loading}
            >
              {loading ? "Generating..." : "✨ Generate Blueprint"}
            </Button>

          </div>

        </Card>

      </div>

    </div>
  );
}