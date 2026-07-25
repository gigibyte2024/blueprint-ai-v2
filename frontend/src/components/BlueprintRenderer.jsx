import Section from "./Section";

export default function BlueprintRenderer({ tab, data }) {
  if (!data) return null;

  if (tab === "planning") {
    return (
      <div className="space-y-8">
        <Section title="📝 Product Summary">
          <p className="text-slate-300 leading-8">{data.product_summary}</p>
        </Section>

        <Section title="✨ Core Features">
          <ul className="space-y-3">
            {data.features.map((feature, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                ✅ {feature}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="👤 User Stories">
          <ul className="space-y-3">
            {data.user_stories.map((story, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                {story}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="⚙ Functional Requirements">
          <ul className="space-y-3">
            {data.functional_requirements.map((item, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                {item}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="🛡 Non Functional Requirements">
          <ul className="space-y-3">
            {data.non_functional_requirements.map((item, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                {item}
              </li>
            ))}
          </ul>
        </Section>
      </div>
    );
  }
  if (tab === "prd") {
    return (
      <div className="space-y-8">
        <Section title="📄 Executive Summary">
          <p className="text-slate-300 leading-8">{data.executive_summary}</p>
        </Section>

        <Section title="❗ Problem Statement">
          <p className="text-slate-300 leading-8">{data.problem_statement}</p>
        </Section>

        <Section title="🎯 Product Goals">
          <ul className="space-y-3">
            {data.product_goals.map((goal, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                🎯 {goal}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="👥 Target Users">
          <ul className="space-y-3">
            {data.target_users.map((user, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                👤 {user}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="⚙ Functional Requirements">
          <ul className="space-y-3">
            {data.functional_requirements.map((item, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                ✅ {item}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="🛡 Non-Functional Requirements">
          <ul className="space-y-3">
            {data.non_functional_requirements.map((item, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                🔒 {item}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="🔄 User Flow">
          <ol className="space-y-3 list-decimal list-inside">
            {data.user_flow.map((step, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                {step}
              </li>
            ))}
          </ol>
        </Section>

        <Section title="📊 Success Metrics">
          <ul className="space-y-3">
            {data.success_metrics.map((metric, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                📈 {metric}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="⚠ Constraints">
          <ul className="space-y-3">
            {data.constraints.map((constraint, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                ⚠ {constraint}
              </li>
            ))}
          </ul>
        </Section>

        <Section title="🚀 Future Scope">
          <ul className="space-y-3">
            {data.future_scope.map((item, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                🚀 {item}
              </li>
            ))}
          </ul>
        </Section>
      </div>
    );
  }
  if (tab === "technical") {
    return (
      <div className="space-y-8">
        <Section title="🛠 Tech Stack">
          <div className="grid md:grid-cols-2 gap-4">
            {Object.entries(data.tech_stack).map(([key, value]) => (
              <div key={key} className="bg-slate-700 rounded-xl p-4">
                <h4 className="text-violet-300 font-semibold capitalize mb-2">
                  {key}
                </h4>

                <p className="text-slate-300">{value}</p>
              </div>
            ))}
          </div>
        </Section>

        <Section title="🗄 Database Tables">
          <div className="space-y-5">
            {Object.entries(data.database_tables).map(([table, columns]) => (
              <div key={table} className="bg-slate-700 rounded-xl p-4">
                <h4 className="text-lg font-semibold text-violet-300 capitalize mb-3">
                  {table}
                </h4>

                <div className="flex flex-wrap gap-2">
                  {columns.map((column, index) => (
                    <span
                      key={index}
                      className="bg-slate-800 px-3 py-1 rounded-full text-sm"
                    >
                      {column}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </Section>

        <Section title="🔌 API Endpoints">
          <div className="space-y-3">
            {data.api_endpoints.map((endpoint, index) => (
              <div
                key={index}
                className="bg-slate-700 rounded-lg p-3 font-mono text-sm"
              >
                {endpoint}
              </div>
            ))}
          </div>
        </Section>

        <Section title="📂 Folder Structure">
          <pre className="bg-slate-700 rounded-xl p-4 overflow-x-auto text-sm whitespace-pre-wrap">
            {data.folder_structure}
          </pre>
        </Section>
      </div>
    );
  }
  if (tab === "api") {
    return (
      <div className="space-y-8">
        <Section title="🔐 Authentication">
          <div className="bg-slate-700 rounded-xl p-4">
            <span className="text-violet-300 font-semibold">
              Authentication Method
            </span>

            <p className="text-slate-300 mt-2">{data.authentication}</p>
          </div>
        </Section>

        <Section title="🌐 Base URL">
          <div className="bg-slate-700 rounded-xl p-4 font-mono text-sm break-all">
            {data.base_url}
          </div>
        </Section>

        <Section title="🔌 API Endpoints">
          <div className="space-y-5">
            {data.endpoints.map((endpoint, index) => (
              <div key={index} className="bg-slate-700 rounded-xl p-5">
                <div className="flex items-center justify-between mb-3">
                  <h4 className="text-lg font-semibold text-violet-300">
                    {endpoint.name}
                  </h4>

                  <span className="bg-violet-600 px-3 py-1 rounded-full text-xs font-semibold">
                    {endpoint.method}
                  </span>
                </div>

                <p className="text-slate-300 mb-3">{endpoint.description}</p>

                <div className="bg-slate-800 rounded-lg p-3 font-mono text-sm mb-4 break-all">
                  {endpoint.path}
                </div>

                {endpoint.request?.body && (
                  <>
                    <h5 className="font-semibold mb-2 text-slate-200">
                      Request Body
                    </h5>

                    <pre className="bg-slate-800 rounded-lg p-3 text-sm overflow-x-auto whitespace-pre-wrap">
                      {JSON.stringify(endpoint.request.body, null, 2)}
                    </pre>
                  </>
                )}

                {endpoint.response && (
                  <>
                    <h5 className="font-semibold mt-4 mb-2 text-slate-200">
                      Response
                    </h5>

                    <pre className="bg-slate-800 rounded-lg p-3 text-sm overflow-x-auto whitespace-pre-wrap">
                      {JSON.stringify(endpoint.response, null, 2)}
                    </pre>
                  </>
                )}
              </div>
            ))}
          </div>
        </Section>
      </div>
    );
  }
  if (tab === "database") {
    return (
      <div className="space-y-8">
        <Section title="🗄 Database Type">
          <div className="bg-slate-700 rounded-xl p-4">
            <span className="text-violet-300 font-semibold">
              {data.database_type.toUpperCase()}
            </span>
          </div>
        </Section>

        <Section title="📦 Entities">
          <div className="space-y-6">
            {data.entities.map((entity, index) => (
              <div key={index} className="bg-slate-700 rounded-xl p-5">
                <h3 className="text-xl font-bold text-violet-300">
                  {entity.name}
                </h3>

                <p className="text-slate-300 mt-2 mb-4">{entity.description}</p>

                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="border-b border-slate-600">
                        <th className="text-left py-2">Field</th>
                        <th className="text-left py-2">Type</th>
                        <th className="text-left py-2">PK</th>
                        <th className="text-left py-2">Unique</th>
                        <th className="text-left py-2">Nullable</th>
                      </tr>
                    </thead>

                    <tbody>
                      {entity.fields.map((field, idx) => (
                        <tr key={idx} className="border-b border-slate-800">
                          <td className="py-2">{field.name}</td>
                          <td className="py-2">{field.type}</td>
                          <td className="py-2">
                            {field.primary_key ? "✅" : "—"}
                          </td>
                          <td className="py-2">{field.unique ? "✅" : "—"}</td>
                          <td className="py-2">
                            {field.nullable ? "Yes" : "No"}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            ))}
          </div>
        </Section>

        <Section title="🔗 Relationships">
          <div className="space-y-3">
            {data.relationships.map((relation, index) => (
              <div key={index} className="bg-slate-700 rounded-lg p-4">
                <p>
                  <strong>{relation.entity1}</strong> ──
                  <span className="text-violet-300">{relation.type}</span>
                  ──► <strong>{relation.entity2}</strong>
                </p>

                <p className="text-slate-400 text-sm mt-2">
                  {relation.field1} → {relation.field2}
                </p>
              </div>
            ))}
          </div>
        </Section>

        <Section title="⚡ Indexes">
          <div className="space-y-3">
            {data.indexes.map((index, idx) => (
              <div key={idx} className="bg-slate-700 rounded-lg p-3">
                📌 {index.entity} → {index.field}
              </div>
            ))}
          </div>
        </Section>

        <Section title="📝 Notes">
          <ul className="space-y-3">
            {data.notes.map((note, index) => (
              <li key={index} className="bg-slate-700 rounded-lg p-3">
                💡 {note}
              </li>
            ))}
          </ul>
        </Section>
      </div>
    );
  }
  if (tab === "roadmap") {
    return (
      <div className="space-y-8">
        <Section title="🗓 Estimated Duration">
          <div className="bg-slate-700 rounded-xl p-4">
            <span className="text-xl font-semibold text-violet-300">
              {data.estimated_duration}
            </span>
          </div>
        </Section>

        <Section title="🚀 Development Phases">
          <div className="space-y-6">
            {data.phases.map((phase, index) => (
              <div key={index} className="bg-slate-700 rounded-xl p-5">
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-xl font-bold text-violet-300">
                    {phase.phase}
                  </h3>

                  <span className="bg-violet-600 px-3 py-1 rounded-full text-sm">
                    {phase.duration}
                  </span>
                </div>

                <h4 className="font-semibold mb-2">🎯 Goals</h4>

                <ul className="space-y-2 mb-5">
                  {phase.goals.map((goal, idx) => (
                    <li key={idx} className="bg-slate-800 rounded-lg p-3">
                      ✅ {goal}
                    </li>
                  ))}
                </ul>

                <h4 className="font-semibold mb-2">📦 Deliverables</h4>

                <ul className="space-y-2">
                  {phase.deliverables.map((item, idx) => (
                    <li key={idx} className="bg-slate-800 rounded-lg p-3">
                      📄 {item}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </Section>

        <Section title="🏁 Milestones">
          <div className="space-y-3">
            {data.milestones.map((milestone, index) => (
              <div key={index} className="bg-slate-700 rounded-lg p-3">
                🎯 {milestone}
              </div>
            ))}
          </div>
        </Section>

        <Section title="⚠ Risks">
          <div className="space-y-3">
            {data.risks.map((risk, index) => (
              <div key={index} className="bg-slate-700 rounded-lg p-3">
                ⚠ {risk}
              </div>
            ))}
          </div>
        </Section>

        <Section title="💡 Recommendations">
          <div className="space-y-3">
            {data.recommendations.map((recommendation, index) => (
              <div key={index} className="bg-slate-700 rounded-lg p-3">
                💡 {recommendation}
              </div>
            ))}
          </div>
        </Section>
      </div>
    );
  }
  if (tab === "ui") {
    return (
      <div className="space-y-8">
        <Section title="📱 Screens">
          <div className="grid md:grid-cols-2 gap-3">
            {data.screens.map((screen, index) => (
              <div key={index} className="bg-slate-700 rounded-lg p-3">
                📄 {screen}
              </div>
            ))}
          </div>
        </Section>

        <Section title="🔄 User Flow">
          <div className="space-y-3">
            {data.user_flow.map((flow, index) => (
              <div key={index} className="bg-slate-700 rounded-lg p-3">
                ➜ {flow}
              </div>
            ))}
          </div>
        </Section>

        <Section title="🎨 UI Prompt">
          <div className="bg-slate-700 rounded-xl p-5">
            <p className="text-slate-300 leading-8">{data.ui_prompt}</p>
          </div>
        </Section>

        <Section title="✨ Design System">
          <div className="flex flex-wrap gap-3">
            {data.design_system.map((item, index) => (
              <span
                key={index}
                className="bg-violet-600 px-4 py-2 rounded-full text-sm"
              >
                {item}
              </span>
            ))}
          </div>
        </Section>

        <Section title="🎨 Color Scheme">
          <div className="grid md:grid-cols-2 gap-4">
            {Object.entries(data.color_scheme).map(([key, value]) => (
              <div
                key={key}
                className="bg-slate-700 rounded-xl p-4 flex items-center justify-between"
              >
                <div>
                  <p className="capitalize font-semibold">{key}</p>

                  <p className="text-slate-300">{value}</p>
                </div>

                <div
                  className="w-10 h-10 rounded-full border border-slate-500"
                  style={{ backgroundColor: value }}
                />
              </div>
            ))}
          </div>
        </Section>

        <Section title="🔤 Typography">
          <div className="bg-slate-700 rounded-xl p-5 space-y-3">
            <p>
              <strong>Font:</strong> {data.typography.font_family}
            </p>

            {Object.entries(data.typography.font_sizes).map(([key, value]) => (
              <p key={key}>
                <strong className="capitalize">{key}:</strong> {value}
              </p>
            ))}
          </div>
        </Section>

        <Section title="🧩 Components">
          <pre className="bg-slate-700 rounded-xl p-4 overflow-x-auto text-sm whitespace-pre-wrap">
            {JSON.stringify(data.components, null, 2)}
          </pre>
        </Section>

        <Section title="🎞 Animations">
          <div className="space-y-3">
            {Object.entries(data.animations).map(([key, value]) => (
              <div
                key={key}
                className="bg-slate-700 rounded-lg p-3 flex justify-between"
              >
                <span className="capitalize">{key.replace(/_/g, " ")}</span>

                <span className="text-violet-300">{value}</span>
              </div>
            ))}
          </div>
        </Section>
      </div>
    );
  }

  return (
    <pre className="text-green-400 whitespace-pre-wrap">
      {JSON.stringify(data, null, 2)}
    </pre>
  );
}
