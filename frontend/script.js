const API_URL = 'https://ton-render-url.onrender.com'; // Remplace par ton URL Render !

async function testHealth() {
  showLoading();
  try {
    const res = await fetch(`${API_URL}/`);
    const data = await res.json();
    document.getElementById('result').innerHTML = 
      `<strong>✅ OK !</strong><br>${JSON.stringify(data, null, 2)}`;
  } catch(e) {
    document.getElementById('result').innerHTML = `<strong>❌ Erreur:</strong> ${e.message}`;
  }
}

async function testDocs() {
  window.open(`${API_URL}/docs`, '_blank');
}

document.getElementById('backend-url').textContent = API_URL;
showLoading();

function showLoading() {
  document.getElementById('result').innerHTML = '⏳ Test en cours...';
}
