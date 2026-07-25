import { useNavigate } from "react-router-dom";
import { ArrowRight } from "lucide-react";
import Navbar from "../components/Navbar";
import Button from "../components/Button";

export default function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-slate-950">
      <Navbar />

      <section className="max-w-6xl mx-auto px-8 py-24">
        <div className="text-center">
          <p className="inline-block bg-violet-600/20 text-violet-400 px-4 py-2 rounded-full text-sm mb-6">
            ✨ AI Powered Product Blueprint Generator
          </p>

          <h1 className="text-6xl md:text-7xl font-extrabold text-white leading-tight">
            Turn Any Startup Idea
            <br />
            Into a<span className="text-violet-500"> Complete Blueprint</span>
          </h1>

          <p className="text-slate-400 text-xl mt-8 max-w-3xl mx-auto leading-9">
            Generate product planning, technical architecture, database schema,
            APIs and UI design in seconds using AI.
          </p>

          <div className="mt-12 flex justify-center">
            <Button onClick={() => navigate("/workspace")}>
              <div className="flex items-center gap-2">
                Get Started
                <ArrowRight size={20} />
              </div>
            </Button>
          </div>
        </div>
      </section>
    </div>
  );
}
