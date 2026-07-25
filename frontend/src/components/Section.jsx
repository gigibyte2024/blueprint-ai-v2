export default function Section({ title, children }) {
  return (
    <div className="mb-8">
      <h3 className="text-xl font-semibold mb-4 text-violet-300">{title}</h3>

      <div className="bg-slate-800 rounded-xl p-5">{children}</div>
    </div>
  );
}
