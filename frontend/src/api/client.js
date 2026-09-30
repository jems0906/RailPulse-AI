const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, { headers: { 'Content-Type': 'application/json' }, ...options })
  if (!response.ok) throw new Error(`API request failed: ${response.status}`)
  return response.json()
}

export const api = {
  health: () => request('/dashboard/network-health'),
  routes: () => request('/dashboard/route-analysis'),
  yards: () => request('/dashboard/yard-analysis'),
  alerts: () => request('/dashboard/alerts'),
  models: () => request('/models/performance'),
  leaderUpdate: () => request('/dashboard/leader-update'),
  predict: (payload) => request('/predict-eta', { method: 'POST', body: JSON.stringify(payload) }),
}
