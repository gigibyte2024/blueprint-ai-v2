import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import Card from "../components/Card";
import Button from "../components/Button";

export default function DashboardPage() {
  const navigate = useNavigate();

  const [blueprint, setBlueprint] = useState(null);

  useEffect(() => {
    const data = sessionStorage.getItem("blueprint");

    if (!data) {
      navigate("/workspace");
      return;
    }

    setBlueprint(JSON.parse(data));
  }, [navigate]);

  if (!blueprint) {
    return (
      <div className="min-h-screen bg-slate-950 text-white flex items-center justify-center">
        <h2 className="text-2xl font-semibold">Loading Blueprint...</h2>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Navbar />

      <div className="max-w-6xl mx-auto px-8 py-12">

        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold">
            🚀 Your Product Blueprint
          </h1>

          <p className="text-slate-400 mt-4">
            Generated using Blueprint AI
          </p>
        </div>

        {/* Planning */}

        <Card>

          <h2 className="text-3xl font-bold mb-6">
            📋 Planning
          </h2>

          <h3 className="text-xl font-semibold mb-2">
            Product Summary
          </h3>

          <p className="text-slate-300 mb-6">
            {blueprint.planning.product_summary}
          </p>

          <h3 className="text-xl font-semibold mb-2">
            Features
          </h3>

          <ul className="list-disc pl-6 space-y-2 mb-6">
            {blueprint.planning.features.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3 className="text-xl font-semibold mb-2">
            User Stories
          </h3>

          <ul className="list-disc pl-6 space-y-2">
            {blueprint.planning.user_stories.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

        </Card>

        <div className="h-8" />

        {/* Technical */}

        <Card>

          <h2 className="text-3xl font-bold mb-6">
            ⚙️ Technical
          </h2>

          <h3 className="text-xl font-semibold mb-2">
            Tech Stack
          </h3>

          <pre className="bg-slate-900 p-4 rounded-xl overflow-auto mb-6">
            {JSON.stringify(blueprint.technical.tech_stack, null, 2)}
          </pre>

          <h3 className="text-xl font-semibold mb-2">
            API Endpoints
          </h3>

          <ul className="list-disc pl-6 space-y-2">
            {blueprint.technical.api_endpoints.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

        </Card>

        <div className="h-8" />

        {/* UI */}

        <Card>

          <h2 className="text-3xl font-bold mb-6">
            🎨 UI Design
          </h2>

          <h3 className="text-xl font-semibold mb-2">
            Screens
          </h3>

          <ul className="list-disc pl-6 space-y-2 mb-6">
            {blueprint.ui.screens.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3 className="text-xl font-semibold mb-2">
            Design Prompt
          </h3>

          <p className="text-slate-300">
            {blueprint.ui.ui_prompt}
          </p>

        </Card>

        <div className="mt-12 text-center">

          <Button onClick={() => navigate("/workspace")}>
            Generate Another Blueprint
          </Button>

        </div>

      </div>
    </div>
  );
}