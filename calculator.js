async function runCalculation() {
    const operation = document.getElementById("operation").value;
    const payload = {
        a: Number(document.getElementById("a").value),
        b: Number(document.getElementById("b").value)
    };

    const response = await fetch(`/${operation}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    const data = await response.json();
    const result = document.getElementById("result");
    result.textContent = response.ok ? `Result: ${data.result}` : data.error;
}

document.getElementById("calculate").addEventListener("click", runCalculation);
