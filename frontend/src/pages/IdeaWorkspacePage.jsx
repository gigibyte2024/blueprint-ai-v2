import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Sparkles } from "lucide-react";

import Navbar from "../components/Navbar";
import Card from "../components/Card";
import Button from "../components/Button";
import TextArea from "../components/TextArea";
import Feature from "../components/Feature";

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

      <div className="max-w-7xl mx-auto px-6 py-16">

        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-white">
            Blueprint AI
          </h1>

          <p className="text-slate-400 mt-4 text-lg">
            Transform your startup idea into a complete software blueprint in minutes.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-8">

          {/* Left Card */}

          <Card>
            <div className="text-center mb-8">
              <Sparkles
                className="mx-auto mb-4 text-violet-500"
                size={42}
              />

              <h2 className="text-3xl font-bold text-white">
                Describe your Product Idea
              </h2>

              <p className="text-slate-400 mt-3">
                The more details you provide, the better your AI-generated blueprint will be.
              </p>
            </div>

            <TextArea
              rows={10}
              placeholder="Example: Build an AI platform that helps college students prepare for placements by generating personalized roadmaps, mock interviews and resume reviews..."
              value={idea}
              onChange={(e) => setIdea(e.target.value)}
            />

            <div className="mt-8">
                  <Button
                      onClick={handleGenerate}
                      disabled={loading}
                      className="w-full py-4"
                  >
        {loading ? (
          <div className="flex items-center justify-center gap-2">
           <Sparkles className="animate-spin" size={18} />
            Generating Blueprint...
    </div>
  ) : (
    "✨ Generate Blueprint"
  )}
</Button>
            </div>
          </Card>

          {/* Right Card */}

          <Card>
            <h2 className="text-2xl font-bold text-white mb-6">
              Your Blueprint Includes
            </h2>

            <div className="space-y-4">
            <Feature
  title="Planning"
  description="Goals, users and core product features."
/>

<Feature
  title="Product Requirements Document"
  description="Complete PRD with functional requirements."
/>

<Feature
  title="Technical Architecture"
  description="Recommended tech stack and system design."
/>

<Feature
  title="API Design"
  description="REST endpoints and request/response structure."
/>

<Feature
  title="Database Schema"
  description="Entities, relationships and database design."
/>

<Feature
  title="Development Roadmap"
  description="Implementation phases and milestones."
/>

<Feature
  title="UI Recommendations"
  description="Screen ideas and design suggestions."
/>
            </div>
          </Card>

        </div>
      </div>
    </div>
  );
}