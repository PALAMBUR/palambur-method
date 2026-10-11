// Extrait `const ARBRE` de outil_chaptal.html et l’écrit dans _cache/arbre.json.
// Pourquoi un scan d’accolades et pas une regex · l’objet fait près de 2 Mo et porte
// des chaînes avec accolades ; seule une lecture caractère par caractère, qui sait
// où elle est dans une chaîne, trouve la bonne fermeture (relevé du 11.10.2026).
// Code de sortie 2 si la source de l’atelier manque (dépôt cloné hors de l’atelier).
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const ATELIER = path.resolve(ICI, '..', '..', '..', '..');
const HTML = path.join(ATELIER, '1300_PRODUITS_IA', '05_CHAPTAL', 'outil_chaptal.html');
const CACHE = path.join(ICI, '_cache');
const SORTIE = path.join(CACHE, 'arbre.json');

if (!fs.existsSync(HTML)) {
  console.error(`source Palambur absente, fiches non regénérables ici · outil_chaptal.html attendu à ${HTML}`);
  process.exit(2);
}
const html = fs.readFileSync(HTML, 'utf8');
const i = html.indexOf('const ARBRE=');
if (i < 0) { console.error('ARBRE introuvable dans ' + HTML); process.exit(1); }
let j = html.indexOf('{', i); let depth = 0; let k = j; let inStr = null;
for (; k < html.length; k++) {
  const c = html[k];
  if (inStr) { if (c === '\\') { k++; continue; } if (c === inStr) inStr = null; continue; }
  if (c === '"' || c === "'" || c === '`') { inStr = c; continue; }
  if (c === '{') depth++;
  else if (c === '}') { depth--; if (depth === 0) { k++; break; } }
}
const ARBRE = eval('(' + html.slice(j, k) + ')');
fs.mkdirSync(CACHE, { recursive: true });
fs.writeFileSync(SORTIE, JSON.stringify(ARBRE, null, 1));

let n = 0; const rows = [];
for (const s of ARBRE.enfants) for (const m of s.enfants) {
  let c = 0; for (const f of m.enfants) c += f.enfants.length;
  n += c; rows.push([s.nom, m.nom, c, m.enfants.length]);
}
console.log(rows.map(r => r.join(' | ')).join('\n'));
console.log(`TOTAL pistes ${n} · métiers ${rows.length} · écrit ${SORTIE}`);
