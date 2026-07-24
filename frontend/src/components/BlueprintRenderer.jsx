export default function BlueprintRenderer({ tab, data }) {

    if (tab === "planning") {
        return (
            <>
                {/* Product Summary */}

                {/* Features */}

                {/* User Stories */}
            </>
        );
    }

    return (
        <pre>
            {JSON.stringify(data, null, 2)}
        </pre>
    );
}