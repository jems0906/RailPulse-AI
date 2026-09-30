export default function RouteRiskMap({ routes = [] }) {
  return <div className="route-heatmap" aria-label="Route risk heatmap">{routes.map((route) => { const risk = route.risk > 0.4 ? 'high' : route.risk > 0.2 ? 'medium' : 'low'; return <div className={`route-cell ${risk}`} key={route.route}><strong>{route.route}</strong><span>{Math.round(route.risk * 100)} risk</span><small>{route.delay}h avg delay</small></div> })}</div>
}
