export default function Card({ children }) {
    return (
      <div
        className="
        bg-slate-900/60
        backdrop-blur-xl
        rounded-3xl
        border
        border-slate-800
        p-8
        shadow-xl"
      >
        {children}
      </div>
    );
  }