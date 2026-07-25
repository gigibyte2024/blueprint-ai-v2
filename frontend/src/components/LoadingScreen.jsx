import { useEffect, useState } from "react";
import { Sparkles } from "lucide-react";

const steps = [
  "🧠 Understanding your idea...",
  "📋 Writing Product Requirements...",
  "🏗️ Designing Technical Architecture...",
  "🔌 Generating API Endpoints...",
  "🗄️ Building Database Schema...",
  "🛣️ Planning Development Roadmap...",
  "🎨 Designing User Interface...",
  "✨ Finalizing Blueprint...",
];

export default function LoadingScreen() {
  const [step, setStep] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setStep((prev) => {
        if (prev < steps.length - 1) {
          return prev + 1;
        }
        return prev;
      });
    }, 1200);

    return () => clearInterval(interval);
  }, []);

  const progress = ((step + 1) / steps.length) * 100;

  return (
    <div className="fixed inset-0 bg-slate-950 flex flex-col items-center justify-center z-50 px-6">
      <Sparkles size={72} className="text-violet-500 animate-pulse mb-8" />

      <h1 className="text-5xl font-bold text-white mb-3">Blueprint AI</h1>

      <p className="text-slate-400 mb-10 text-lg text-center">
        Building your complete software blueprint...
      </p>

      <div className="w-full max-w-md">
        <div className="flex justify-between text-sm text-slate-500 mb-3">
          <span>{steps[step]}</span>
          <span>{Math.round(progress)}%</span>
        </div>

        <div className="h-3 bg-slate-800 rounded-full overflow-hidden">
          <div
            className="h-full bg-gradient-to-r from-violet-500 via-fuchsia-500 to-cyan-400 transition-all duration-700 rounded-full"
            style={{
              width: `${progress}%`,
            }}
          />
        </div>
      </div>

      <p className="text-slate-500 text-sm mt-8">
        This usually takes around 15–30 seconds.
      </p>
    </div>
  );
}
