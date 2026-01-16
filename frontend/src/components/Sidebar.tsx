import { uploadResume } from "../services/api";

function Sidebar({ setMessages, setResumeId, setCompareResume }) {

  async function handleresumeupload(e) {
    const file = e.target.files[0];
    if (!file) return;

    try {
      const result = await uploadResume(file);
      setResumeId(result.resume_id);

      setMessages(prev => [
        ...prev,
        { role: "ai", text: "Primary resume uploaded successfully" }
      ]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { role: "ai", text: "Error occurred. Resume upload failed." }
      ]);
    }
  }

  async function handlecompareresume(e) {
    const file = e.target.files[0];
    if (!file) return;

    try {
      const result = await uploadResume(file);
      setCompareResume(result.resume_id);

      setMessages(prev => [
        ...prev,
        { role: "ai", text: "Comparison resume uploaded successfully" }
      ]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { role: "ai", text: "Comparison resume upload failed." }
      ]);
    }
  }

  return (
    <aside className="w-72 bg-white border-r h-[calc(100vh-4rem)] px-4 py-6 flex flex-col">

      {/* AUTO MODE */}
      <div className="mb-6">
        <h2 className="text-xs font-semibold text-gray-400 uppercase mb-2">
          Intelligence Mode
        </h2>

        <div className="rounded-xl border bg-gradient-to-br from-gray-50 to-gray-100 p-4">
          <div className="font-medium text-sm flex items-center gap-2">
            ⚡ Auto Agent Routing
          </div>
          <p className="text-xs text-gray-600 mt-1">
            The system automatically chooses the best agent based on your message.
          </p>
        </div>
      </div>

      {/* CAPABILITIES */}
      <div className="mb-6">
        <h2 className="text-xs font-semibold text-gray-400 uppercase mb-3">
          What Bharat AI Can Do
        </h2>

        <ul className="space-y-2 text-sm text-gray-700">
          <li className="flex items-start gap-2">📄 <span>Answer questions from uploaded resumes</span></li>
          <li className="flex items-start gap-2">✨ <span>Suggest resume improvements</span></li>
          <li className="flex items-start gap-2">📊 <span>Compare two resumes intelligently</span></li>
          <li className="flex items-start gap-2">🎤 <span>Conduct mock technical interviews</span></li>
          <li className="flex items-start gap-2">⭐ <span>Score resumes using ATS-style logic</span></li>

          <li className="flex-col items-start gap-2 justify-evenly bg-gray-50">
            <div className="space-y-6">

              {/* Primary Resume */}
              <div>
                <h3 className="text-sm font-semibold text-gray-700 mb-2">
                  Primary Resume
                </h3>

                <label className="flex items-center justify-center w-full px-4 py-6
                                  border-2 border-dashed rounded-lg cursor-pointer
                                  bg-gray-50 hover:bg-gray-100
                                  text-sm text-gray-600 transition">
                  <span>📄 Click to upload or drag & drop</span>
                  <input
                    type="file"
                    accept=".pdf"
                    className="hidden"
                    onChange={handleresumeupload}
                  />
                </label>
              </div>

              {/* Compare Resume */}
              <div>
                <h3 className="text-sm font-semibold text-gray-700 mb-2">
                  Compare With
                  <span className="ml-2 text-xs text-gray-400">(optional)</span>
                </h3>

                <label className="flex items-center justify-center w-full px-4 py-6
                                  border-2 border-dashed rounded-lg cursor-pointer
                                  bg-gray-50 hover:bg-gray-100
                                  text-sm text-gray-600 transition">
                  <span>📄 Upload second resume</span>
                  <input
                    type="file"
                    accept=".pdf"
                    className="hidden"
                    onChange={handlecompareresume}
                  />
                </label>
              </div>

            </div>
          </li>
        </ul>
      </div>

      {/* HINT */}
      <div className="mt-auto">
        <div className="rounded-lg bg-gray-50 border px-3 py-2 text-xs text-gray-600">
          💡 Tip: Upload one resume to ask questions. Upload two to compare.
        </div>
      </div>

    </aside>
  );
}

export default Sidebar;

