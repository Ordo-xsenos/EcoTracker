// script.js
document.getElementById('calculate').addEventListener('click', () => {
  const distance = parseFloat(document.getElementById('distance').value) || 0;
  const meat = parseFloat(document.getElementById('meat').value) || 0;
  const electricity = parseFloat(document.getElementById('electricity').value) || 0;

  // Примерные коэффициенты (тонн CO2e на единицу)
  const factorDistance = 0.00021;   // 0.21 кг CO2e на км → 0.00021 т
  const factorMeat = 0.005;         // 5 кг CO2e за порцию → 0.005 т
  const factorElectricity = 0.000475; // 0.475 кг CO2e за кВт·ч → 0.000475 т

  const co2 = distance * factorDistance
             + meat * factorMeat
             + electricity * factorElectricity;

  document.getElementById('co2-output').textContent =
    `${co2.toFixed(2)} т CO₂ в выбранный период.`;

  // Простые советы
  const tips = [
    'Попробуйте ездить на велосипеде или ходить пешком.',
    'Уменьшите количество мясных блюд в рационе.',
    'Выключайте свет и бытовые приборы, когда они не нужны.'
  ];
  const tipsContainer = document.getElementById('tips');
  tipsContainer.innerHTML = tips.map(t => `<li>${t}</li>`).join('');
  document.getElementById('results').classList.remove('hidden');

  // Сохранение в localStorage при необходимости :contentReference[oaicite:8]{index=8}
  localStorage.setItem('ecoTrackerResult', JSON.stringify({ co2, timestamp: Date.now() }));
});
