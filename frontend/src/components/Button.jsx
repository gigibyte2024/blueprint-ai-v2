export default function Button({ children, onClick, disabled = false }) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className="
        bg-violet-600
        hover:bg-violet-500
        active:scale-95
        transition-all
        duration-200
        disabled:opacity-60
        px-8
        py-4
        rounded-2xl
        text-white
        font-semibold
        text-lg
        shadow-lg
        shadow-violet-900/40"
    >
      {children}
    </button>
  );
}
