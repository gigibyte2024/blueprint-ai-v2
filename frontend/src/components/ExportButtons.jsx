import { jsPDF } from "jspdf";
import html2canvas from "html2canvas";
import { toast } from "sonner";

export default function ExportButtons({ title, data, targetRef }) {
  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(JSON.stringify(data, null, 2));

      toast.success("Copied to clipboard!");
    } catch (err) {
      toast.error("Failed to copy.");
    }
  };

  const downloadMarkdown = () => {
    const markdown = `# ${title}
      
      \`\`\`json
      ${JSON.stringify(data, null, 2)}
      \`\`\`
      `;

    const blob = new Blob([markdown], {
      type: "text/markdown",
    });

    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);
    link.download = `${title}.md`;

    link.click();

    URL.revokeObjectURL(link.href);

    toast.success("Markdown downloaded!");
  };

  const downloadPDF = async () => {
    if (!targetRef.current) return;

    try {
      const canvas = await html2canvas(targetRef.current, {
        scale: 2,
      });

      const imgData = canvas.toDataURL("image/png");

      const pdf = new jsPDF("p", "mm", "a4");

      const pageWidth = pdf.internal.pageSize.getWidth();

      const imgWidth = pageWidth - 20;

      const imgHeight = (canvas.height * imgWidth) / canvas.width;

      pdf.addImage(imgData, "PNG", 10, 10, imgWidth, imgHeight);

      pdf.save(`${title}.pdf`);

      toast.success("PDF downloaded!");
    } catch (err) {
      console.error(err);
      toast.error("Failed to generate PDF.");
    }
  };

  return (
    <div className="flex flex-wrap gap-3 mb-6">
      <button
        onClick={copyToClipboard}
        className="bg-slate-700 hover:bg-slate-600 px-4 py-2 rounded-lg transition"
      >
        📋 Copy
      </button>

      <button
        onClick={downloadMarkdown}
        className="bg-violet-600 hover:bg-violet-500 px-4 py-2 rounded-lg transition"
      >
        📝 Markdown
      </button>

      <button
        onClick={downloadPDF}
        className="bg-green-600 hover:bg-green-500 px-4 py-2 rounded-lg transition"
      >
        📄 PDF
      </button>
    </div>
  );
}
