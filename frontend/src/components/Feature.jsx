import { CheckCircle2 } from "lucide-react";

export default function Feature({ title, description }) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-4">
      <div className="flex items-center gap-3 mb-1">
        <CheckCircle2 className="text-emerald-400" size={20} />

        <span className="font-semibold text-white">{title}</span>
      </div>

      <p className="text-sm text-slate-400 ml-8">{description}</p>
    </div>
  );
}
