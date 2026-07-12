export default function TextArea(props) {
    return (
      <textarea
        {...props}
        className="
        w-full
        rounded-2xl
        bg-slate-900
        border
        border-slate-700
        p-6
        text-lg
        text-white
        placeholder:text-slate-500
        outline-none
        resize-none
        focus:border-violet-500
        transition-all
        duration-300"
      />
    );
  }