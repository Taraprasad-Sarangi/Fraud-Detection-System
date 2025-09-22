const API = "http://127.0.0.1:8000/predict";

document.getElementById("demo").onclick = async () => {
  // A random normal-ish sample (not real)
  const tx = { Time: 10000, Amount: 50 };
  for (let i = 1; i <= 28; i++) tx[`V${i}`] = 0.0;
  try {
    const res = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(tx),
    });
    const data = await res.json();
    document.getElementById("out").textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    document.getElementById("out").textContent = "Error: " + e;
  }
};
