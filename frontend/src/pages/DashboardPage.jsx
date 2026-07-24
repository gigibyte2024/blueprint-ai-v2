import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import Card from "../components/Card";
import Button from "../components/Button";
import BlueprintRenderer from "../components/BlueprintRenderer";
export default function DashboardPage() {
  const navigate = useNavigate();

  const [blueprint, setBlueprint] = useState(null);
  const [activeTab, setActiveTab] = useState("planning");

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
      <div className="min-h-screen bg-slate-950 flex items-center justify-center text-white">
        <h2 className="text-2xl font-semibold">
          Loading Blueprint...
        </h2>
      </div>
    );
  }

  const tabs = [
    { key: "planning", label: "📋 Planning" },
    { key: "prd", label: "📄 PRD" },
    { key: "technical", label: "🏗 Technical" },
    { key: "api", label: "🔌 API" },
    { key: "database", label: "🗄 Database" },
    { key: "roadmap", label: "🗺 Roadmap" },
    { key: "ui", label: "🎨 UI" },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Navbar />

      <div className="max-w-[1600px] mx-auto px-6 py-12">

        {/* Header */}

        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold">
            🚀 Your Product Blueprint
          </h1>

          <p className="text-slate-400 mt-4 text-lg">
            Generated using Blueprint AI
          </p>
        </div>

        {/* Main Layout */}

        <div className="grid lg:grid-cols-4 gap-8">

          {/* Sidebar */}

          <Card>

            <h2 className="text-xl font-bold mb-6">
              Blueprint Sections
            </h2>

            <div className="space-y-3">

              {tabs.map((tab) => (

                <button
                  key={tab.key}
                  onClick={() => setActiveTab(tab.key)}
                  className={`w-full rounded-xl px-4 py-3 text-left transition-all duration-300 ${
                    activeTab === tab.key
                      ? "bg-violet-600 text-white"
                      : "bg-slate-900 text-slate-300 hover:bg-slate-800"
                  }`}
                >
                  {tab.label}
                </button>

              ))}

            </div>

          </Card>

          {/* Content */}

          <div className="lg:col-span-3">

            <Card>

              <div className="flex justify-between items-center mb-6">

                <h2 className="text-3xl font-bold capitalize">
                  {activeTab}
                </h2>

              </div>

              <div className="bg-slate-900 rounded-xl p-6 overflow-auto max-h-[650px]">

              <BlueprintRenderer
  tab={activeTab}
  data={blueprint[activeTab]}
/>

              </div>

            </Card>

          </div>

        </div>

        {/* Bottom Button */}

        <div className="mt-12 text-center">

          <Button onClick={() => navigate("/workspace")}>
            ✨ Generate Another Blueprint
          </Button>

        </div>

      </div>
    </div>
  );
}