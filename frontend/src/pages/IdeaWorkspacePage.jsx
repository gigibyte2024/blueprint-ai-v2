import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Sparkles } from "lucide-react";
import { toast } from "sonner";
import Navbar from "../components/Navbar";
import Card from "../components/Card";
import Button from "../components/Button";
import TextArea from "../components/TextArea";
import Feature from "../components/Feature";
import LoadingScreen from "../components/LoadingScreen";

import { streamBlueprint } from "../services/blueprintService";

export default function IdeaWorkspacePage() {
  const navigate = useNavigate();

  const [idea, setIdea] = useState("");
  const [loading, setLoading] = useState(false);
  const [selectedModules, setSelectedModules] = useState([
    "planning",
    "prd",
    "technical",
    "api",
    "database",
    "roadmap",
    "ui",
    "reflection",
  ]);
  async function handleGenerate() {
    if (!idea.trim()) {
      toast.error("Please enter your startup idea.");
      return;
    }
  
    try {
      setLoading(true);
  
      const requestedModules = [
        "planning",
        "prd",
        "technical",
        "api",
        "database",
        "roadmap",
        "ui",
        "reflection",
      ];
  
      await streamBlueprint(
        idea,
        requestedModules,
  
        (progress) => {
          console.log("Blueprint progress:", progress);
        },
  
        (result) => {
          sessionStorage.setItem(
            "blueprint",
            JSON.stringify(result.blueprint)
          );
  
          sessionStorage.setItem(
            "startupIdea",
            idea
          );
  
          toast.success("Blueprint generated successfully!");
  
          navigate("/dashboard");
        }
      );
    } catch (err) {
      console.error(err);
      toast.error("Failed to generate blueprint.");
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return <LoadingScreen />;
  }

  return (
    <div className="min-h-screen bg-slate-950">
      <Navbar />

      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-white">Blueprint AI</h1>

          <p className="text-slate-400 mt-4 text-lg max-w-3xl mx-auto">
            Transform your startup idea into a complete software blueprint
            powered by AI. Generate planning, PRD, architecture, APIs, database
            schema, roadmap and UI recommendations in minutes.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-8">
          {/* Left Card */}

          <Card>
            <div className="text-center mb-8">
              <Sparkles className="mx-auto mb-4 text-violet-500" size={42} />

              <h2 className="text-3xl font-bold text-white">
                Describe your Product Idea
              </h2>

              <p className="text-slate-400 mt-3">
                The more details you provide, the more accurate and detailed
                your AI-generated blueprint will be.
              </p>
            </div>

            <TextArea
              rows={10}
              placeholder="Example: Build an AI platform that helps college students prepare for placements with personalized learning roadmaps, resume reviews, mock interviews and skill tracking."
              value={idea}
              onChange={(e) => setIdea(e.target.value)}
            />

            <div className="mt-8">
            <h3 className="text-white font-semibold mb-4">
              Select Modules
            </h3>

              <div className="grid grid-cols-2 gap-3">

    {[
      "planning",
      "prd",
      "technical",
      "api",
      "database",
      "roadmap",
      "ui",
      "reflection",
    ].map((module) => (

      <label
        key={module}
        className="flex items-center gap-2 text-slate-300"
      >
        <input
          type="checkbox"
          checked={selectedModules.includes(module)}
          onChange={(e) => {

            if (e.target.checked) {
              setSelectedModules([
                ...selectedModules,
                module,
              ]);
            } else {
              setSelectedModules(
                selectedModules.filter(
                  (m) => m !== module
                )
              );
            }

          }}
        />

        {module}

      </label>

    ))}

  </div>
</div>

            <div className="mt-8">

              <Button onClick={handleGenerate} className="w-full py-4">
                ✨ Generate Blueprint
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
                description="Goals, target audience, problem statement and core product features."
              />

              <Feature
                title="Product Requirements Document"
                description="Detailed functional and non-functional requirements with project scope."
              />

              <Feature
                title="Technical Architecture"
                description="Recommended technology stack, system architecture and folder structure."
              />

              <Feature
                title="API Design"
                description="REST API endpoints with request and response formats."
              />

              <Feature
                title="Database Schema"
                description="Entities, relationships and scalable database design."
              />

              <Feature
                title="Development Roadmap"
                description="Implementation phases, milestones and development timeline."
              />

              <Feature
                title="UI Recommendations"
                description="Suggested screens, layouts and design ideas for your product."
              />
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
