import { Bot } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="w-full flex items-center justify-between px-10 py-5 border-b border-slate-800 bg-slate-950">
      <div className="flex items-center gap-3">
        <div className="bg-violet-600 rounded-xl p-3">
          <Bot className="text-white" size={22} />
        </div>

        <div>
          <h1 className="text-white text-xl font-bold">
            Blueprint AI
          </h1>

          <p className="text-slate-400 text-sm">
            AI Product Architect
          </p>
        </div>
      </div>

      <a
        href="https://github.com/gigibyte2024/blueprint-ai-v2"
        target="_blank"
        rel="noreferrer"
        className="bg-slate-900 hover:bg-slate-800 px-5 py-3 rounded-xl transition text-white"
      >
        GitHub
      </a>
    </nav>
  );
}