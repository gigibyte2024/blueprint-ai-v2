import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import {
  Rocket,
  LayoutDashboard,
  FileText,
  Cpu,
  Database,
  Route,
  Palette,
  Plug,
  CheckCircle2,
  CalendarDays,
} from "lucide-react";

import Navbar from "../components/Navbar";
import Card from "../components/Card";
import Button from "../components/Button";
import BlueprintRenderer from "../components/BlueprintRenderer";
import ExportButtons from "../components/ExportButtons";

export default function DashboardPage() {
  const navigate = useNavigate();

  const [blueprint, setBlueprint] = useState(null);
  const [activeTab, setActiveTab] = useState("planning");

  const exportRef = useRef(null);
  const generatedDate = new Date().toLocaleDateString();
  useEffect(() => {
    const data = sessionStorage.getItem("blueprint");

    if (!data) {
      navigate("/workspace");
      return;
    }

    setBlueprint(JSON.parse(data));
  }, [navigate]);

  const tabs = useMemo(
    () => [
      {
        key: "planning",
        label: "Planning",
        icon: <LayoutDashboard size={18} />,
      },
      {
        key: "prd",
        label: "PRD",
        icon: <FileText size={18} />,
      },
      {
        key: "technical",
        label: "Technical",
        icon: <Cpu size={18} />,
      },
      {
        key: "api",
        label: "API",
        icon: <Plug size={18} />,
      },
      {
        key: "database",
        label: "Database",
        icon: <Database size={18} />,
      },
      {
        key: "roadmap",
        label: "Roadmap",
        icon: <Route size={18} />,
      },
      {
        key: "ui",
        label: "UI",
        icon: <Palette size={18} />,
      },
    ],
    []
  );

  if (!blueprint) {
    return (
      <div className="min-h-screen bg-slate-950 flex flex-col items-center justify-center text-center px-6">
  
        <div className="w-24 h-24 rounded-full bg-violet-600/20 flex items-center justify-center mb-6">
          🚀
        </div>
  
        <h1 className="text-4xl font-bold text-white">
          No Blueprint Found
        </h1>
  
        <p className="text-slate-400 mt-4 max-w-md">
          Generate your first AI-powered product blueprint to see it here.
        </p>
  
        <button
          onClick={() => navigate("/workspace")}
          className="mt-8 px-6 py-3 rounded-xl bg-violet-600 hover:bg-violet-500 transition"
        >
          Generate Blueprint
        </button>
  
      </div>
    );
  }

  return (
    <motion.div
  className="min-h-screen bg-slate-950 text-white"
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ duration: 0.35 }}
>
      <Navbar />

      <div className="max-w-[1700px] mx-auto px-8 py-10">
        {/* Header */}

        <div className="mb-10 rounded-3xl border border-slate-800 bg-gradient-to-r from-slate-900 via-slate-900 to-violet-950 p-8">

          <div className="flex flex-col lg:flex-row justify-between gap-8">

            <div>

              <div className="flex items-center gap-3 mb-4">

                <Rocket className="text-violet-400" />

                <span className="text-violet-400 font-semibold uppercase tracking-widest text-sm">
                  Blueprint AI
                </span>

              </div>

              <h1 className="text-5xl font-bold">
              {sessionStorage.getItem("startupIdea") || "Product Blueprint"}
              </h1>

              <p className="text-slate-400 mt-4 max-w-2xl">
                Your complete AI-generated product documentation including
                planning, architecture, APIs, database, roadmap and UI.
              </p>

            </div>

            <div className="grid grid-cols-3 gap-4">

              <div className="rounded-2xl bg-slate-900 border border-slate-800 p-5">
                <CheckCircle2 className="text-emerald-400 mb-3" />
                <p className="text-3xl font-bold">7</p>
                <p className="text-slate-400 text-sm">
                  Sections
                </p>
              </div>

              <div className="rounded-2xl bg-slate-900 border border-slate-800 p-5">
                <Rocket className="text-violet-400 mb-3" />
                <p className="text-3xl font-bold">Ready</p>
                <p className="text-slate-400 text-sm">
                  Status
                </p>
              </div>

              <div className="rounded-2xl bg-slate-900 border border-slate-800 p-5">
                <CalendarDays className="text-cyan-400 mb-3" />
                <p className="text-lg font-semibold">
                {generatedDate}
                </p>
                <p className="text-slate-400 text-sm">
                  Generated
                </p>
              </div>

            </div>

          </div>

        </div>

        {/* Main */}

        <div className="grid lg:grid-cols-[300px_1fr] gap-8">

          {/* Sidebar */}

          <div className="rounded-3xl bg-slate-900 border border-slate-800 p-6 h-fit sticky top-24">

            <h2 className="font-bold text-xl mb-6">
              Blueprint
            </h2>

            <div className="space-y-3">

              {tabs.map((tab) => (

                <button
                  key={tab.key}
                  onClick={() => setActiveTab(tab.key)}
                  className={`w-full flex items-center gap-3 rounded-xl px-4 py-3 transition-all duration-300 ${
                    activeTab === tab.key
                      ? "bg-violet-600 text-white shadow-lg shadow-violet-500/20"
                      : "text-slate-300 hover:bg-slate-800"
                  }`}
                >
                  {tab.icon}

                  {tab.label}

                </button>

              ))}

            </div>

          </div>

          {/* Content */}

          <div className="rounded-3xl bg-slate-900 border border-slate-800 p-8">

            <div className="flex flex-col lg:flex-row justify-between gap-5 mb-8">

              <div>

                <p className="text-violet-400 uppercase tracking-widest text-sm">
                  Current Section
                </p>

                <h2 className="text-4xl font-bold capitalize mt-2">
                  {activeTab}
                </h2>

              </div>

              <div className="flex gap-3 flex-wrap">

  <Button
    onClick={() => navigate("/workspace")}
    className="px-5 py-2"
  >
    ← Back
  </Button>

  <ExportButtons
    title="Complete Blueprint"
    data={blueprint}
    targetRef={exportRef}
  />

</div>

            </div>

      <motion.div
      key={activeTab}
      ref={exportRef}
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.25 }}
      className="rounded-2xl bg-slate-950 border border-slate-800 p-8 max-h-[720px] overflow-auto"
      >
              <BlueprintRenderer
                tab={activeTab}
                data={blueprint[activeTab]}
              />
            </motion.div>

          </div>

        </div>

        <div className="mt-12 flex justify-center">

        <Button
  onClick={() => {
    sessionStorage.removeItem("blueprint");
    sessionStorage.removeItem("startupIdea");
    navigate("/workspace");
  }}
  className="px-10 py-4"
>
  🚀 Generate Another Blueprint
</Button>

        </div>

      
      </div>
      </motion.div>
  );
}