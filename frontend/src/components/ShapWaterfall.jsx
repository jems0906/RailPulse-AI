export default function ShapWaterfall({ factors = [] }) {
  if (!factors.length) return <p className="empty-explanation">Explanation values are not available for this prediction.</p>
  const maxImpact = Math.max(...factors.map((factor) => Math.abs(Number(factor.impact))), 1)
  return <div className="shap-waterfall">{factors.map((factor) => <div className="shap-row" key={factor.feature}><span>{factor.feature}</span><div className="shap-track"><i className={factor.direction === 'down' ? 'negative' : ''} style={{ width: `${Math.max(8, Math.abs(Number(factor.impact)) / maxImpact * 100)}%` }} /></div><b className={factor.direction === 'down' ? 'negative-text' : ''}>{Number(factor.impact) > 0 ? '+' : ''}{factor.impact}</b></div>)}</div>
}
