const test = require('node:test');
const assert = require('node:assert/strict');
const baseUrl = process.env.API_BASE_URL || 'http://127.0.0.1:18080';
async function request(path, options) {
  const response = await fetch(new URL(path, baseUrl), options);
  const body = await response.json();
  return { response, body };
}
test('GET /health returns healthy service metadata', async () => {
  const { response, body } = await request('/health');
  assert.equal(response.status, 200); assert.equal(body.status, 'ok');
  assert.equal(body.service, 'performance-lab-api'); assert.ok(body.version);
});
test('GET /api/products returns a non-empty product list', async () => {
  const { response, body } = await request('/api/products');
  assert.equal(response.status, 200); assert.ok(Array.isArray(body.products));
  assert.ok(body.products.length > 0); assert.equal(body.count, body.products.length);
});
test('GET /api/search respects bounded delay and returns query', async () => {
  const { response, body } = await request('/api/search?q=load-test&delayMs=0');
  assert.equal(response.status, 200); assert.equal(body.query, 'load-test');
  assert.equal(body.tookMs, 0); assert.ok(Array.isArray(body.results));
});
test('GET /api/report returns report metadata', async () => {
  const { response, body } = await request('/api/report?delayMs=0&work=10');
  assert.equal(response.status, 200); assert.equal(body.report, 'synthetic-performance-report');
  assert.equal(body.delayMs, 0); assert.equal(body.work, 10); assert.equal(typeof body.checksum, 'number');
});
test('POST /api/checkout accepts a JSON item list', async () => {
  const { response, body } = await request('/api/checkout', {
    method: 'POST', headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ items: [{ id: 101 }, { id: 102 }] })
  });
  assert.equal(response.status, 201); assert.equal(body.accepted, true);
  assert.equal(body.itemCount, 2); assert.match(body.orderId, /^ORD-/);
});
test('unknown routes return a JSON 404', async () => {
  const { response, body } = await request('/not-a-real-route');
  assert.equal(response.status, 404); assert.equal(body.error, 'not_found');
});
test('GET /metrics exposes Prometheus metrics', async () => {
  const response = await fetch(new URL('/metrics', baseUrl)); const body = await response.text();
  assert.equal(response.status, 200); assert.match(body, /http_requests_total/);
  assert.match(body, /http_request_duration_seconds_bucket/);
});
